import random
import requests
from flask import Flask
from flask import request
from flask import render_template

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


@app.route("/poke")
def poke_display(poke: str):
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{poke}')
    if r.status_code == requests.codes.ok:
        poke_basic_info = r.json()
        poke_dex_info = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{poke}').json()
        dex_entry = ''
        for entry in poke_dex_info['flavor_text_entries']:
            if entry['language']['name'] == 'en':
                dex_entry = entry['flavor_text']
        return render_template('poke.html.jinja', nav='search', title='Search', poke=poke_basic_info, dex=dex_entry)
    else:
        return render_template('not_found.html.jinja', title='Error', page='pokémon')


@app.route("/random")
def poke_rand():
    rand_id = str(random.randint(0, 899))
    return poke_display(rand_id)
