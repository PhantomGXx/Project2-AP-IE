#FlasK

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///SQL.sql'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)

@app.route('/')
def index():
    return render_template('MainPage.html')

@app.route('/add-item', methods=['POST'])
def sell():
    item_name = request.form['item-name']
    item_description = request.form['item-description']
    item_price = float(request.form['item-price'])
    item_category = request.form['item-category']

    item = Item(name=item_name, description=item_description, price=item_price, category=item_category)
    
    db.session.add(item)
    db.session.commit()

    return 'Item added to sell list!'

@app.route('/')
def index():
    # create a list of items to display
    items = [
        {'name': 'Item 1', 'description': 'This is item 1', 'price': '$19.99','category':'electronics'},
        {'name': 'Item 2', 'description': 'This is item 2', 'price': '$29.99','category':'electronics'},
        {'name': 'Item 3', 'description': 'This is item 3', 'price': '$39.99','category':'electronics'}
    ]
    
    # render the item_section.html template for each item in the list
    return render_template('Index.html', items=items)

@app.route('/sell', methods=['POST'])
def sell_item():
    # process the form data and put the item up for sale
    # ...
    # redirect the user to MainPage.html with a success message
    return redirect(url_for('main_page', success=True))

@app.route('/MainPage.html')
def main_page():
    success = request.args.get('success')
    if success:
        return '''
            <html>
            <body>
                <h1>Your item was put up for sale successfully!</h1>
            </body>
            </html>
        '''
    else:
        return '''
            <html>
            <body>
                <h1>Item was unable to be put up for sale. Sorry!</h1>
            </body>
            </html>
        '''

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