from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


app.debug = False
if __name__ == "__main__":
    app.run()
