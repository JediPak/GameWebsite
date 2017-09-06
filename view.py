from flask import *

app = Flask(__name__)

@app.route('/')
def pick_game():
    return render_template('index.html')
