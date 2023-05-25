#FlasK

from flask import Flask, render_template, request

app = Flask(__name__)

items_for_sale = []

@app.route('/')
def index():
    return render_template('HTML.html')

@app.route('/sell', methods=['POST'])
def sell():
    item_name = request.form['item-name']
    item_description = request.form['item-description']
    item_price = request.form['item-price']
    
    item = {
        'name': item_name,
        'description': item_description,
        'price': item_price
    }
    
    items_for_sale.append(item)
    
    return 'Item added to sell list!'

if __name__ == '__main__':
    app.run(debug=True)

"""
import requests

url = "https://api.apilayer.com/fixer/convert?to=IRR&from=USD&amount=1"

payload = {}
headers= {
  "apikey": "y1nAFLy9Mt7kO9xglrjDuHKIz4GG7BbW"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
"""

