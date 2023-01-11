from flask import Flask
from flask import render_template, redirect, url_for
from flask import request
from block import *

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        lender = request.form['lender']
        key = request.form['key']
        num = request.form['num']

        write_block(name=lender, amount=key, to_whom=num)
        return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/checking', methods=['GET'])
def check():
    results = check_integrity()
    return render_template('index.html', ch_res=results)


if __name__ == '__main__':
    app.run(debug=True)




