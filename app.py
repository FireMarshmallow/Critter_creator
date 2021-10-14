"""
Code by
  __  __      _ _                 _____ _          
 |  \/  | ___| | | _____      __ |  ___(_)_ __ ___ 
 | |\/| |/ _ \ | |/ _ \ \ /\ / / | |_  | | '__/ _ \
 | |  | |  __/ | | (_) \ V  V /  |  _| | | | |  __/
 |_|  |_|\___|_|_|\___/ \_/\_/   |_|   |_|_|  \___|
check out my stuff on https://linktr.ee/Mellowfire
"""
from flask import Flask, render_template, request
import Critter_Creator

url = "http://127.0.0.1:5000"
app = Flask(__name__)


@app.route("/")
def CritterCreator():
    Critter_Creator.run()
    imagess = Critter_Creator.imagess
    links = Critter_Creator.links
    names = Critter_Creator.names
    return render_template(
        "Critter_Creator.html",
        url=url,
        name_of_animal_1=names[0],
        name_of_animal_2=names[1],
        name_of_animal_3=names[2],
        name_of_animal_4=names[3],
        name_of_animal_5=names[4],
        name_of_animal_6=names[5],
        name_of_animal_7=names[6],
        name_of_animal_8=names[7],
        image_of_animal_1=imagess[0],
        image_of_animal_2=imagess[1],
        image_of_animal_3=imagess[2],
        image_of_animal_4=imagess[3],
        image_of_animal_5=imagess[4],
        image_of_animal_6=imagess[5],
        image_of_animal_7=imagess[6],
        image_of_animal_8=imagess[7],
        link_to_animal_1=links[0],
        link_to_animal_2=links[1],
        link_to_animal_3=links[2],
        link_to_animal_4=links[3],
        link_to_animal_5=links[4],
        link_to_animal_6=links[5],
        link_to_animal_7=links[6],
        link_to_animal_8=links[7],
    )


app.run(host="0.0.0.0")
