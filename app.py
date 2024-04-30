<<<<<<< HEAD
from flask import Flask, Blueprint, render_template
from config.db import db, ma, app

@app.route('/', methods='GET')
def index():
    return render_template('')
=======
from config.db import db, ma, app
from flask import Flask, render_template, request, json, jsonify

@app.route('/', methods=['GET'])
def index():
    return render_template("layout.html")

>>>>>>> b8d0d1b051cb0624112a56fce6277bff6e583ad5

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')