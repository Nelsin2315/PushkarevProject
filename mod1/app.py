import datetime
import os
import re
import random

from random import choice
from flask import Flask

app = Flask(__name__)

visits = 0
datatime = "%d-%m-%Y %H:%M:%S"
cars = ["Chevrolet", "Renault", "Ford", "Lada"] #Массив с машинами
cats = ["корниш-рекс", "русская голубая", "шотландская вислоухая", "мейн-кун", "манчкин"] #коты

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')

# Список слов из книги
with open(BOOK_FILE, 'r', encoding='utf-8') as book:
    text = book.read()
    words = re.findall(r'\b\w+\b', text)

@app.route('/hello_world')
def index1():
    return "Привет, мир!"

@app.route('/cars')
def index2():
    return ', '.join(cars)

@app.route('/cats')
def random_cats():
    return choice(cats)

@app.route('/get_time/now')
def get_current_time():
    now = datetime.datetime.now()
    current_time_str = now.strftime(datatime)
    time_message = "Время: " + current_time_str
    return time_message

@app.route('/get_time/future')
def index5():
    now = datetime.datetime.now()
    future_time = now + datetime.timedelta(hours=1)
    future_time_str = future_time.strftime(datatime)
    future_message = "Точное время через час: " + future_time_str
    return future_message


@app.route('/get_random_word')
def get_random_word():
     return random.choice(words)

@app.route('/counter')
def counter():
   global visits
   visits += 1
   return f"Страница открыта кол-во: {visits}"

if __name__ == "__main__":
    app.run(debug=True)