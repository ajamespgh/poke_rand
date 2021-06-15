import random
import requests
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html.jinja')


@app.route("/search")
def poke_search():
    return render_template('search.html.jinja')


@app.route("/random")
def poke_rand():
    rand_id = str(random.randint(0, 899))
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{rand_id}')
    rand_poke = r.json()
    return render_template('poke.html.jinja', nav="random", title="Random", poke=rand_poke)
