from flask import Flask, render_template, request 
import requests

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html.j2')

@app.route('/pokemon', methods=['GET', 'POST'])
def pokemon():
    if request.method == 'POST':
        name = request.form.get('poke')
        url = f"https://pokeapi.co/api/v2/pokemon/{name}"
        response = requests.get(url)
        if not response.ok:
            error_string= "Please enter a valid pokemon"
            return render_template('pokemon.html.j2', error=error_string)
        
        if not response.json():
            error_string = "We had an error loading your data"
            return render_template('pokemon.html.j2', error=error_string)

        poke = response.json()
        poke_dict={
                "poke_name":poke['name'],
                "attack_base_stat":poke ["stats"][1]["base_stat"],
                "hp_base_stat": poke["stats"][0]["base_stat"],
                "defense_base_stat": poke["stats"][2]["base_stat"],
                "front_shiny": poke["sprites"]["front_shiny"],
                "ability_name": poke["abilities"][0]["ability"]["name"],
                "base_experience": poke["base_experience"],
            }

        return render_template('pokemon.html.j2', poke=poke_dict)
    
    return render_template('pokemon.html.j2')