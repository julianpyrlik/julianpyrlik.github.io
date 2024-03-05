from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
import os

app = Flask(__name__)
# essential for securing your application's sessions, cookies, and cryptographic functions
app.config['SECRET_KEY'] = "njsl284552nonwgsff840nf893yf8f3"
Bootstrap5(app)





# --------------------------------create functions---------------------------------------

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5002)