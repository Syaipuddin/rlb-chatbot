import re
import string
import os

from flask_cors import CORS
from nltk.chat.util import reflections
from chat import ChatExtended
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk.corpus import stopwords
from flask import Flask, request
from pairs import pairs
from pymongo import MongoClient, DESCENDING
from bson.json_util import dumps, loads
import json
from bson import ObjectId
from dotenv import load_dotenv, dotenv_values

load_dotenv()


import nltk
nltk.download('stopwords')

client = MongoClient(os.getenv("MONGO_URI"))
db = client['Cluster0']
collection = db['chatbot']

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

class Chatbot:



    # START CHATBOT
    def start(self, msg):
        cf = self.case_fold(msg)
        nn = self.no_noise(cf)
        stem = self.stemmer(nn)
        ns = self.no_stopwords(stem)
        
        text = ''
        for i in ns:
            text += i

        words = text.split()

        for pair in pairs:
            keys = pair[0].replace('(', "").replace(")", "").split("|")

        chat = ChatExtended(pairs, reflections)
        res = chat.respond(text)
        if not res:
            error = 'Mohon Maaf saya tidak bisa mengerti, Apakah anda bisa mengulangi?'
            return error
        
        return res

    # CASE FOLDING
    def case_fold(self, msg):
        case_folded = msg.lower()
        numberless = re.sub(r"\d+", "", case_folded)
        no_punc = numberless.translate(str.maketrans("", "", string.punctuation))
        no_ws = no_punc.strip()

        return no_ws
    
    # STOP WORDS REMOVAL
    def no_stopwords(self, msg_list):
        stopwords_list = set(stopwords.words('indonesian'))
        cleaned = []
        for words in msg_list:
            if words not in stopwords_list:
                cleaned.append(words)

        return cleaned 
    
    # STEMMING
    def stemmer(self, msg):
        stemFact = StemmerFactory()
        stemmer = stemFact.create_stemmer()
        stemmed_words = stemmer.stem(msg)

        return stemmed_words

    # NOISE REMOVAL
    def no_noise(self, msg):
        clean_text = re.sub(r'[\.\?\!\,\:\;\"]', '', msg)
        return clean_text
    

app = Flask(__name__)
CORS(app)
cb = Chatbot()

@app.route('/ask', methods=['POST'])
def start_bot():
    data = request.get_json()
    prompt = data['msg']
    room_id = data['roomId']

    print(prompt)
    print(room_id)

    data_user = {
        'roomId': room_id,
        'isUser': True,
        "msg": prompt
    }
    post_chat(data_user)

    text = cb.start(prompt)
    data_bot = {
        'roomId': room_id,
        'isUser': False,
        "msg": text
    }
    post_chat(data_bot)

    response = {
        "msg": text
    }

    return response


@app.route('/get-chat', methods=['POST'])
def get_db():
    data = request.get_json()
    room_id = data['roomId']
    data = db.collection.find({'roomId': room_id}).sort('_id', DESCENDING)
    list_data = list(data)
    json_data = dumps(list_data, indent=2)

    return json_data


@app.route('/get-chat-by-id/<id>')
def get_db_by_id(id):
    print(id)
    data = db.collection.find_one({'_id': id})
    json_data = dumps(data, indent=2)

    return json_data


@app.route('/post', methods=['POST'])
def post_chat(data):

    id = db.collection.insert_one(data).inserted_id

    data = {
        "_id": str(id)
    }

    return data