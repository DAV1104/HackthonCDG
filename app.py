from flask import Flask, Blueprint, render_template
from config.db import db, ma, app

@app.route('/', methods=['GET'])
def index():
    return render_template("layout.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')