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
    "u buying window covers so we can get freaky n them not fitting",
    "the week b4 we started dating having those long convos",
    "o-week, spending all night doing random stuff",
    "being on call watching you play shadow of the colosus",
    "goin to new brighton n u pushing me on swing cuz u were too nonchalant to join",
    "randomly goin new brighton at night, quietly sitting on a bench on ur lap watchin the water n kissing you",
    "you taking us to mama mia night n me getting pmoed ab ss",
    "bathroom freaky time",
    "exam time, spending all day tryna study but getting distracted by u",
    "goin to httyd n the guy actin like he worked there",
    "stealin ur ring n giving it to my dad (he still got on his desk)"
    "our joined playlist",
    "morning after bnbs sittin in mm3 chilling eating mchickens",
    "when u gave me hello kitty burger n were acting all nonchalant (i was too)",
    "u givin me my jacket back b4 we started dating n me actin at awks",
    "first time we hung out tg in day",
    "u giving me ur teddy bear jacket, now i wear it every week",
    "u losing all ur rings in that field us drunkenly looking for them",
    "stayin at c-block so late the lights shut off",
    "playing scenarios w u like everyday",
    
    
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
    "everything about you",
    "the lil games u play on ps5",
    "how excited u are for gta",
    "when u start overexplaining things u like",
    "i love you",
    "that pretty dihh",
    "super duper freaky",
    "ur es",
    "ur tralalalalalala song",
    "the way ur eyes widen sometimes when u react or talk",
    "skinny ass waist",
    "big shoulders",
    "'they offered me 15.. 15 million..'",
    "when i say oi n u reply ee",
    "when u say da flip or copy me",
    "u lil stop n start thing w songs",
    "u act so nonchalant, but ur so funny n cute",
    "how u act when u sleepy",
    "how cute u were as baby",
    "ur weird ass antics like ur pen game",
    "u my unda",
    "ur voice gets higher when u talk louder",
    "u so warm"
]

@app.route('/get-memory')
def get_memory():
    return jsonify(random.choice(our_memories))

@app.route('/get-love')
def get_love():
    return jsonify(random.choice(about_you))
@app.route('/')
@app.route('/')
def home():
    return render_template(
        'index.html',
        days=days_together,
        hours=hours_together,
        memories=our_memories,
        about=about_you
    )



if __name__ == '__main__':
    app.run(debug=True, port=5001)
