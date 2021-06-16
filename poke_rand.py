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
    rand_poke = requests.get(f'https://pokeapi.co/api/v2/pokemon/{rand_id}').json()
    rand_poke_info = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{rand_id}/').json()
    dex_entry = ''
    for entry in rand_poke_info['flavor_text_entries']:
        if entry['language']['name'] == 'en':
            dex_entry = entry['flavor_text']
            break
    return render_template('poke.html.jinja', nav="random", title="Random", poke=rand_poke, dex=dex_entry)
