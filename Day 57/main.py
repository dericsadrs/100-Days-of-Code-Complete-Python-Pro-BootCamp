import random, datetime
from flask import Flask, render_template

app = Flask(__name__)

year_now = datetime.datetime.now().year

@app.route('/')
def home():
    random_number = random.randint(1,10)
    return render_template("index.html", num = random_number,year = year_now )


if __name__ == "__main__":
    app.run(debug=True)


