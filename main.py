from flask import Flask, render_template, request,redirect, url_for
from block import *

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        lender = request.form.get('Lender')
        amount = request.form.get('Amount')
        borrower = request.form.get('Borrower')

        write_block(name=lender, amount=amount, to_whom=borrower)
   
    return render_template('index.html')


@app.route('/check', methods=['GET'])
def check():
    results = check_integrity()
    return render_template('index.html', results=results)



if __name__ == '__main__':
    app.run(debug=True)
