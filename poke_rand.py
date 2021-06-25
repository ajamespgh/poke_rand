import json
import random
import requests
from flask import Flask
from flask import request
from flask import render_template
from functools import lru_cache

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html.jinja')


@app.route("/search")
def poke_search():
    return render_template('search.html.jinja')


@app.route("/search", methods=['POST'])
def search_handler():
    searches = {
        'poke': poke_display
    }
    if request.method == 'POST':
        return searches[request.form['lookupType']](request.form['searchValue'])


@lru_cache
def get_poke_info(poke: str):
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{poke}')
    return r.text if r.status_code == requests.codes.ok else False


@lru_cache
def get_dex_info(poke: str):
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{poke}')
    if r.status_code == requests.codes.ok:
        for entry in r.json()['flavor_text_entries']:
            if entry['language']['name'] == 'en':
                return entry['flavor_text']
    return False


def poke_display(poke: str):
    poke_info = get_poke_info(poke)
    dex_info = get_dex_info(poke)
    if poke_info and dex_info:
        return render_template('poke.html.jinja', nav='search', title='Search', poke=json.loads(poke_info), dex=dex_info)
    return render_template('not_found.html.jinja', title='Error', page='pokémon')


@app.route("/random")
def poke_rand():
    rand_id = str(random.randint(0, 899))
    return poke_display(rand_id)
