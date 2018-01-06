from app import app, db
from flask import send_file


@app.route('/home', methods=['GET', 'POST'])
def index():
    return send_file('templates/index.html')
