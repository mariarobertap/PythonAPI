from flask import Flask

app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique = True)

    def __repr__(self) -> str:
        return f"{self.name}"

@app.route('/')
def index():
    return 'Hello Worldasds'

@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()
    output = []
    for drink in drinks:
        drink_data = {'name': drink.name}
        output.append(drink_data)
    return {"drinks": output}


@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)

    return {"name" : drink.name}

if __name__ == '__name__':
    app.run(debug=True)

app.run(debug=True)