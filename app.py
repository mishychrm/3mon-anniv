from flask import Flask, render_template, jsonify
from datetime import date
import random

app = Flask(__name__)

anniversary = date(2025, 3, 7)
today = date.today()
days_together = (today - anniversary).days
hours_together = days_together * 24

our_memories = [
    "meeting u at mm2, talkin ab streetlights when u tried 2 kiss me",
    "how i felt the day u asked me 2 be ur girlfriend and hugging u after",
    "u taking us to a beach then getting lost",
    "all the bnbs 🫦",
    "my mum running out 2 meet u n talking ab my dead grandpa",
    "going to armageddon together",
    "after toga watchin u fail at geometry dash and u kissing me each time u died",
    "seeing u giggle like a lil kid watching corykenshin",
    "our son working at maccas",
    "getting freaky tg 24/7",
    "my dad catching us at mm3",
    "u buying window covers so we can get freaky n them not fitting"
]

about_you = [
    "big curly hair i love",
    "ur eyelashes that curl by themselves",
    "all black fits my lil emo",
    "ur teddy bear jacket",
    "that lil part under ur beard where the hairs like disconnect",
    "the way u say 'nope",
    "the face you make when you're trying not to laugh",
    "how u make those hand gestures whenever you talk",
    "u always so patient when idk what to say",
    "how u love chocolate shakes",
    "ur laugh",
    "how u yawn like a whale",
    "when u repeat that lil tiktok thing 'they offered me 4 mil'",
    "everything about you",
    "the lil games u play on ps5",
    "how excited u are for gta",
    "when u start overexplaining things u like",
    "i love you",
    "that pretty dihh",
    "super duper freaky"
]

@app.route('/get-memory')
def get_memory():
    return jsonify(random.choice(our_memories))

@app.route('/get-love')
def get_love():
    return jsonify(random.choice(about_you))
@app.route('/')
def home():
    return render_template('index.html', days=days_together, hours=hours_together)



if __name__ == '__main__':
    app.run(debug=True, port=5001)
