from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), nullable=False)

    def __repr__(self) -> str:
        return f"{self.name}"



@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/products")
def get_drinks():
    products = Product.query.all()
    output = []
    for pro in products:
        product_data = {'name': pro.name, 'Description': pro.description}
        output.append(product_data)
    return {"Products": output}


