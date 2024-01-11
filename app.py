app = Flask(__name__)

# Load the trained Word2Vec model
model = Word2Vec.load("AE2_MODEL.model")
# need to change the location #
@app.route("/FlaskApp/Template", methods=["GET", "POST"])
def index():
    opposite_words = []

    if request.method == "POST":
        word = request.form["word"]
        if word:
            try:
                # Get the opposite words
                opposite_words = model.wv.most_similar(negative=[word], topn=1)
            except KeyError:
                opposite_words = ["Word not found in the model."]

    return render_template("index.html", opposite_words=opposite_words)

if __name__ == "__main__":
    app.run(debug=True)