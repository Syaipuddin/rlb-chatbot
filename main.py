import re
import string
from nltk.chat.util import reflections
from chat import ChatExtended
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk.corpus import stopwords
from flask import Flask, request
from pairs import pairs
import jaro

import nltk
nltk.download('stopwords')


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
cb = Chatbot()

@app.route('/init', methods=['POST'])
def start_bot():
    text = cb.start(request.form['msg'])
    
    return text