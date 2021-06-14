import json
import random
import requests
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html.jinja')


@app.route("/search")
def poke_search():
    return render_template('search.html.jinja')


@app.route("/random")
def poke_rand():
    rand_id = str(random.randint(0, 897))
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{rand_id}')
    rand_poke = r.json()
    return render_template('poke.html.jinja', poke=rand_poke)
