import tkinter
import tkinter.ttk
from tkinter import *
import requests
import json
from bs4 import BeautifulSoup

poke_id_name = {}
pokemon_name_list = []
poke_url = []


def on_combobox_select(event):
    visible_gui()
    selected_item = p_name.get()
    if selected_item == "bulbasaur":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/001.png")
        get_stats("Images/001stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
    elif selected_item == "ivysaur":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/002.png")
        get_stats("Images/002stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
    elif selected_item == "venusaur":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/003.png")
        get_stats("Images/003stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
    elif selected_item == "charmander":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/004.png")
        get_stats("Images/004stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
    elif selected_item == "charmeleon":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/005.png")
        get_stats("Images/005stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
    elif selected_item == "charizard":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/006.png")
        get_stats("Images/006stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
    elif selected_item == "squirtle":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/007.png")
        get_stats("Images/007stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
    elif selected_item == "wartortle":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/008.png")
        get_stats("Images/008stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
    elif selected_item == "blastoise":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/009.png")
        get_stats("Images/009stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
    elif selected_item == "caterpie":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/010.png")
        get_stats("Images/010stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
    elif selected_item == "metapod":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/011.png")
        get_stats("Images/011stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
    elif selected_item == "butterfree":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/012.png")
        get_stats("Images/012stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
    elif selected_item == "weedle":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/013.png")
        get_stats("Images/013stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
    elif selected_item == "kakuna":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/014.png")
        get_stats("Images/014stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
    elif selected_item == "beedrill":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/015.png")
        get_stats("Images/015stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
    elif selected_item == "pidgey":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/016.png")
        get_stats("Images/016stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
    elif selected_item == "pidgeotto":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/017.png")
        get_stats("Images/017stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
    elif selected_item == "pidgeot":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/018.png")
        get_stats("Images/018stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
    elif selected_item == "rattata":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/019.png")
        get_stats("Images/019stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
    elif selected_item == "raitcate":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/020.png")
        get_stats("Images/020stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
    elif selected_item == "spearow":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/021.png")
        get_stats("Images/021stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
    elif selected_item == "fearow":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/022.png")
        get_stats("Images/022stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
    elif selected_item == "ekans":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/023.png")
        get_stats("Images/023stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
    elif selected_item == "arbok":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/024.png")
        get_stats("Images/024stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
    elif selected_item == "pikachu":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/025.png")
        get_stats("Images/025stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
    elif selected_item == "raichu":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/026.png")
        get_stats("Images/026stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
    elif selected_item == "sandshrew":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/027.png")
        get_stats("Images/027stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
    elif selected_item == "sndslash":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/028.png")
        get_stats("Images/028stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
    elif selected_item == "nidoran-f":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/029.png")
        get_stats("Images/029stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
    elif selected_item == "nidorina":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/030.png")
        get_stats("Images/030stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
    elif selected_item == "nidoqueen":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/031.png")
        get_stats("Images/031stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
    elif selected_item == "nidoran-m":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/032.png")
        get_stats("Images/032stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
    elif selected_item == "nidorino":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/033.png")
        get_stats("Images/033stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
    elif selected_item == "nidoking":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/034.png")
        get_stats("Images/034stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
    elif selected_item == "clefairy":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/035.png")
        get_stats("Images/035stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
    elif selected_item == "clefable":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/036.png")
        get_stats("Images/036stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
    elif selected_item == "vulpix":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/037.png")
        get_stats("Images/037stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
    elif selected_item == "ninetales":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/038.png")
        get_stats("Images/038stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
    elif selected_item == "jigglypuff":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/039.png")
        get_stats("Images/039stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
    elif selected_item == "wigglytuff":
        get_height(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_ability(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_weight(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")
        get_logo("Images/040.png")
        get_stats("Images/040stats.png")
        get_category(f"https://pokeapi.co/api/v2/pokemon-species/{selected_item}")
        get_types(f"https://pokeapi.co/api/v2/pokemon/{selected_item}")


def get_poke_name():
    new_color = "gray"
    p_name.configure(background=new_color)
    p_name.place(x=20, y=75)
    pokemon_name_list.clear()
    get_pokemon_req = requests.get("https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0")
    poke_name = get_pokemon_req.json()["results"]
    i = 1
    pokemon_name_list.append("Seçiniz...")
    for poke in poke_name:
        if i < 41:
            pokemon_name_list.append(poke["name"])
            poke_url.append((poke["url"]))
            i += 1
        else:
            continue
    p_name.config(values=pokemon_name_list)
    p_name.current(0)
    a = 1
    for x in pokemon_name_list:
        poke_id_name[a] = x
        a += 1
    p_name.update()
    window.update()
    p_name.bind("<<ComboboxSelected>>", on_combobox_select)


def get_ability(_url):
    req = requests.get(_url)
    abilities = [req.json()["abilities"][0]]
    get_ability_name = abilities[0]["ability"]["name"]
    # print(get_ability_name)
    abilities_label.config(text=get_ability_name.title())
    abilities_label.place(x=600, y=230)


def get_height(url):
    req = requests.get(url)
    height = req.json()["height"]
    height = height * 10
    height_inc = round(height / 2.54)
    height_ft = int(height_inc / 12)
    height_rem_inc = round(height_inc % 12)
    if height_rem_inc < 10:
        height_rem_inc = "0" + f"{height_rem_inc}"
    height = f"{height_ft}"+"'"+f"{height_rem_inc}"+'"'
    height_label.config(text=height)
    height_label.place(x=330, y=150)


def get_weight(url):
    req = requests.get(url)
    weight = req.json()["weight"]
    weight = weight / 10
    weight_lb = str(round(weight / 0.45359237, 1)) + " lbs"
    weight_label.config(text=f"{weight_lb}")
    weight_label.place(x=330, y=230)


def get_logo(file):
    global logo, logo_canvas
    logo_canvas = Canvas(height=215, width=215, bg="white", highlightthickness=1, highlightbackground="white")
    logo = PhotoImage(file=file)
    logo_canvas.create_image(107.5, 107.5, image=logo)
    logo_canvas.place(x=50, y=120)


def get_stats(file):
    global stats, stats_canvas
    stats_canvas = Canvas(width=260, height=168, bg="gray", highlightthickness=2, highlightbackground="black")
    stats = PhotoImage(file=file)
    stats_canvas.create_image(130, 85, image=stats)
    stats_canvas.place(x=20, y=365)


def get_types(url):
    global images, img_canvas, img_canvas_2, images_2
    img_canvas = Canvas(width=136, height=30, bg="lightblue", highlightthickness=1, highlightbackground="lightblue")
    img_canvas_2 = Canvas(width=136, height=30, bg="lightblue", highlightthickness=1, highlightbackground="lightblue")
    img_canvas_2.delete('all')
    req = requests.get(url)
    if len(req.json()["types"]) == 1:
        images_2 = PhotoImage(file="Images/bg.png")
        type_1 = req.json()["types"][0]["type"]["name"]
        if type_1 == "grass":
            images = PhotoImage(file="Images/grass.png")
            img_canvas.create_image(68, 15, image=images)
            img_canvas_2.create_image(68, 15, image=images_2)
            img_canvas_2.place(x=330, y=510)
            img_canvas.place(x=330, y=410)
        if type_1 == "fire":
            images = PhotoImage(file="Images/fire.png")
            img_canvas.create_image(68, 15, image=images)
            img_canvas_2.create_image(68, 15, image=images_2)
            img_canvas_2.place(x=330, y=510)
            img_canvas.place(x=330, y=410)
        if type_1 == "water":
            images = PhotoImage(file="Images/water.png")
            img_canvas.create_image(68, 15, image=images)
            img_canvas_2.create_image(68, 15, image=images_2)
            img_canvas_2.place(x=330, y=510)
            img_canvas.place(x=330, y=410)
        if type_1 == "poison":
            images = PhotoImage(file="Images/poison.png")
            img_canvas.create_image(68, 15, image=images)
            img_canvas_2.create_image(68, 15, image=images_2)
            img_canvas_2.place(x=330, y=510)
            img_canvas.place(x=330, y=410)
        if type_1 == "normal":
            images = PhotoImage(file="Images/normal.png.png")
            img_canvas.create_image(68, 15, image=images)
            img_canvas_2.create_image(68, 15, image=images_2)
            img_canvas_2.place(x=330, y=510)
            img_canvas.place(x=330, y=410)
        if type_1 == "bug":
            images = PhotoImage(file="Images/bug.png")
            img_canvas.create_image(68, 15, image=images)
            img_canvas_2.create_image(68, 15, image=images_2)
            img_canvas_2.place(x=330, y=510)
            img_canvas.place(x=330, y=410)
        if type_1 == "electric":
            images = PhotoImage(file=f"Images/electric.png")
            img_canvas.create_image(68, 15, image=images)
            img_canvas_2.create_image(68, 15, image=images_2)
            img_canvas_2.place(x=330, y=510)
            img_canvas.place(x=330, y=410)
        if type_1 == "ground":
            images = PhotoImage(file=f"Images/ground.png")
            img_canvas.create_image(68, 15, image=images)
            img_canvas_2.create_image(68, 15, image=images_2)
            img_canvas_2.place(x=330, y=510)
            img_canvas.place(x=330, y=410)
        if type_1 == "fairy":
            images = PhotoImage(file=f"Images/fairy.png")
            img_canvas.create_image(68, 15, image=images)
            img_canvas_2.create_image(68, 15, image=images_2)
            img_canvas_2.place(x=330, y=510)
            img_canvas.place(x=330, y=410)
        if type_1 == "flying":
            images = PhotoImage(file=f"Images/flying.png")
            img_canvas.create_image(68, 15, image=images)
            img_canvas_2.create_image(68, 15, image=images_2)
            img_canvas_2.place(x=330, y=510)
            img_canvas.place(x=330, y=410)
        else:
            type_text_1.config(text="")

    # '''
    elif len(req.json()["types"]) == 2:
        type_1 = req.json()["types"][0]["type"]["name"]
        type_2 = req.json()["types"][1]["type"]["name"]
        if type_1 == "grass":
            images = PhotoImage(file="Images/grass.png")
            img_canvas.create_image(68, 15, image=images)
            img_canvas_2.create_image(68, 15, image=images_2)
            img_canvas_2.place(x=330, y=510)
            img_canvas.place(x=330, y=410)
        if type_1 == "fire":
            images = PhotoImage(file="Images/fire.png")
            img_canvas.create_image(68, 15, image=images)
            img_canvas.place(x=330, y=410)
        if type_1 == "water":
            images = PhotoImage(file="Images/water.png")
            img_canvas.create_image(68, 15, image=images)
            img_canvas.place(x=330, y=410)
        if type_1 == "poison":
            images = PhotoImage(file="Images/poison.png")
            img_canvas.create_image(68, 15, image=images)
            img_canvas.place(x=330, y=410)
        if type_1 == "normal":
            images = PhotoImage(file="Images/normal.png")
            img_canvas.create_image(68, 15, image=images)
            img_canvas.place(x=330, y=410)
        if type_1 == "bug":
            images = PhotoImage(file="Images/bug.png")
            img_canvas.create_image(68, 15, image=images)
            img_canvas.place(x=330, y=410)
        if type_1 == "electric":
            images = PhotoImage(file=f"Images/electric.png")
            img_canvas.create_image(68, 15, image=images)
            img_canvas.place(x=330, y=410)
        if type_1 == "ground":
            images = PhotoImage(file=f"Images/ground.png")
            img_canvas.create_image(68, 15, image=images)
            img_canvas.place(x=330, y=410)
        if type_1 == "fairy":
            images = PhotoImage(file=f"Images/fairy.png")
            img_canvas.create_image(68, 15, image=images)
            img_canvas.place(x=330, y=410)
        if type_1 == "flying":
            images = PhotoImage(file=f"Images/flying.png")
            img_canvas.create_image(68, 15, image=images)
            img_canvas.place(x=330, y=410)

#-----------------------------------------------------------------------------------

        if type_2 == "grass":
            images_2 = PhotoImage(file=f"Images/grass.png")
            img_canvas_2.create_image(68, 15, image=images_2)
            img_canvas_2.place(x=330, y=510)
        if type_2 == "fire":
            images_2 = PhotoImage(file=f"Images/fire.png")
            img_canvas_2.create_image(68, 15, image=images_2)
            img_canvas_2.place(x=330, y=510)
        if type_2 == "water":
            images_2 = PhotoImage(file=f"Images/water.png")
            img_canvas_2.create_image(68, 15, image=images_2)
            img_canvas_2.place(x=330, y=510)
        if type_2 == "poison":
            images_2 = PhotoImage(file=f"Images/poison.png")
            img_canvas_2.create_image(68, 15, image=images_2)
            img_canvas_2.place(x=330, y=510)
        if type_2 == "normal":
            images_2 = PhotoImage(file=f"Images/normal.png")
            img_canvas_2.create_image(68, 15, image=images_2)
            img_canvas_2.place(x=330, y=510)
        if type_2 == "bug":
            images_2 = PhotoImage(file=f"Images/bug.png")
            img_canvas_2.create_image(68, 15, image=images_2)
            img_canvas_2.place(x=330, y=510)
        if type_2 == "electric":
            images_2 = PhotoImage(file=f"Images/electric.png")
            img_canvas_2.create_image(68, 15, image=images_2)
            img_canvas_2.place(x=330, y=510)
        if type_2 == "ground":
            images_2 = PhotoImage(file=f"Images/ground.png")
            img_canvas_2.create_image(68, 15, image=images_2)
            img_canvas_2.place(x=330, y=510)
        if type_2 == "fairy":
            images_2 = PhotoImage(file=f"Images/fairy.png")
            img_canvas_2.create_image(68, 15, image=images_2)
            img_canvas_2.place(x=330, y=510)
        if type_2 == "flying":
            images_2 = PhotoImage(file=f"Images/flying.png")
            img_canvas_2.create_image(68, 15, image=images_2)
            img_canvas_2.place(x=330, y=510)
        else:
            type_text_1.config(text="")
            type_text_2.config(text="")
        # '''


def get_category(url):
    global category_label, category_
    category_label.config(text="")
    req = requests.get(url)
    category_ = req.json()["genera"][7]["genus"]
    category_ = category_.split(" ")[0]
    category_label.config(text=category_.title())
    category_label.place(x=600, y=150)


def visible_gui():
    info_canvas.place(x=300, y=100)
    height_text_label.place(x=330, y=120)
    weight_text_label.place(x=330, y=200)
    category_text_label.place(x=600, y=120)
    abilities_text_label.place(x=600, y=200)
    type_canvas.place(x=300, y=360)
    type_text_label.place(x=340, y=375)


window = Tk()
window.title("PokéDex")
window.config(bg="white")
window.minsize(width=800, height=680)


p_name = tkinter.ttk.Combobox(window, width=42)

# INFORMATION CANVAS
info_canvas = Canvas(height=250, width=400)
info_canvas.config(bg="lightblue", highlightthickness=2, highlightbackground="black")


img_canvas = None
img_canvas_2 = None
images_2 = None
images = None
logo = None
logo_canvas = None
stats = None
stats_canvas = None
category_ = None


get_poke_name()

height_text_label = Label(text="Height", bg="lightblue",font=("Helvetica", 12, "bold"), fg="white")


abilities_label = Label(text="", bg="lightblue", font=("Helvetica", 12, "bold"))
height_label = Label(text="", bg="lightblue", font=("Helvetica", 12, "bold"))

category_text_label = Label(text="Category", bg="lightblue", font=("Helvetica", 12, "bold"), fg="white")
category_label = Label(text="", bg="lightblue", font=("Helvetica", 12, "bold"))

weight_text_label = Label(text="Weight", bg="lightblue", font=("Helvetica", 12, "bold"), fg="white")

weight_label = Label(text="", bg="lightblue", font=("Helvetica", 12, "bold"))


abilities_text_label = Label(text="Abilities", bg="lightblue", font=("Helvetica", 12, "bold"), fg="white")


type_canvas = Canvas(height=250, width=400)
type_canvas.config(bg="lightblue", highlightthickness=2, highlightbackground="black")


type_text_label = Label(text="Type", font=("Helvetica", 12, "bold"), bg="lightblue",fg="white")


type_text_1 = Label(text="deneme", font=("Helvetica", 12, "bold"),width=10)
type_text_2 = Label(text="poison", font=("Helvetica", 12, "bold"), width=10)

header_text = Label(text="Welcome To PokéDex", fg="Red", font=("Helvetica", 24, "bold"), bg="white")
header_text.pack(padx=15, pady=15)


window.mainloop()
