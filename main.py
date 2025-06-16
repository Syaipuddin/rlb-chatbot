import re
import string
import os

from flask_cors import CORS
from nltk.chat.util import reflections
from chat import ChatExtended
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from flask import Flask, request
from pairs import pairs
from pymongo import MongoClient, DESCENDING
from bson.json_util import dumps, loads
import json
from util import extend_text, similarity_score
from bson import ObjectId
from dotenv import load_dotenv

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

    def get_rules_group(self, str):
        group_rules = [
            [ r'(ktp|tanda pengenal|kartu tanda penduduk)','ktp'],
            [ r'(surat pindah|surat terang pindah)', 'surat_pindah'],
            [ r'(datang|terang datang)', 'keterangan_datang'],
            [ r'(skl|lahir|terang lahir)', 'keterangan_lahir'],
            [ r'(kk|kartu keluarga)', 'kk'],
            [ r'(skrt|rumah tangga)', 'skrt'],
            [ r'(skk|surat terang mati)', 'skk'],
            [ r'(skck|catat polisi)', 'skck'],
            [ r'(skm|sktm|terang mampu)', 'sktm'],
            [ r'(sku|terang usaha)', 'sku'],
            [ r'(kia|identitas|anak)', 'kia'],
            [ r'(profil|daerah)', 'profil'],
            [ r'(domisili)', 'domisili'],
            [ r'(riwayat tanah)', 'surat_tanah'],
            [ r'(buka|administratif)', 'umum'],
        ]

        input_str = str.lower()
        matches = []

        for keyword, label in group_rules:
            max_score = 0

            keyword = keyword.replace('(', '')
            keyword = keyword.replace(')', '')
            for word in keyword.split('|'):
                if word in input_str:
                    score = similarity_score(input_str, word)
                    if score > max_score:
                        max_score = score
                    
            matches.append(max_score)
            
        # print(matches)
        # Ambil indeks dengan skor tertinggi
        max_index = matches.index(max(matches))
        # Ambil label yang sesuai
        return group_rules[max_index][1] 


    # START CHATBOT
    def start(self, msg):
        cf = self.case_fold(msg)
        print("case fold: " + cf)
        nn = self.no_noise(cf)
        print("no noise: " + nn)
        ns = self.no_stopwords(nn)
        text = ' '.join(ns)
        print("no stop words: " + text)
        extended = extend_text(text)
        print("extended text: " + extended)
        stem = self.stemmer(extended)
        print("stem: " + stem)

        rule_group =  self.get_rules_group(stem)
        print("rule group: " + str(rule_group))

        res = 'Mohon Maaf saya tidak bisa mengerti, Apakah anda bisa mengulangi?'
        if rule_group:
            chat = ChatExtended(pairs[rule_group], reflections)
            res = chat.respond(stem)
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

        from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
        factory = StopWordRemoverFactory()
        stopwords = factory.get_stop_words()
        additional_sw = ['apa', 'bagaimana']
        for sw in additional_sw:
            stopwords.append(sw)

        cleaned = []
        for words in msg_list.split():
            if words not in stopwords:
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

@app.route('/')
def home():

    return "Backend Ready"

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
