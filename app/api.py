from flask import Flask, request, jsonify

app = Flask(__name__)

# list
hadiths = [
    {"number": 1, "source": "Sahih Bukhari", "text": "The best among you are those who learn the Quran and teach it."},
    {"number": 2, "source": "Sahih Muslim", "text": "The strong believer is better and more beloved to Allah than the weak believer."},
    {"number": 3, "source": "Tirmidhi", "text": "The best of you are those who have the best manners and character."},
    {"number": 4, "source": "Abu Dawood", "text": "When one of you prays, he should not spit in front of him, for Allah is in front of him when he prays."},
    {"number": 5, "source": "Ibn Majah", "text": "Allah does not look at your bodies nor your forms but He looks at your hearts and your deeds."}
    ]

# this function will retrieve a specific hadith
def get_hadith(number):
    chosen_hadith = next((i for i in hadiths if i['number'] == number), None)
    return chosen_hadith

# Flask route to use the standalone function
@app.route("/get-hadith/<int:number>")
def get_hadith_route(number):
    chosen_hadith = get_hadith(number)
    if chosen_hadith is not None:
        return jsonify(chosen_hadith), 200
    else:
        return jsonify({'error': 'Hadith not found'}), 404


@app.route("/")
def get_all_hadiths():
    return jsonify(hadiths), 200


if "__name__" == "__api__":
    app.run(debug=True) 
    