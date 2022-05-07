from flask import Flask, render_template, request, redirect
from db_ex import Base, Contact, create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

def open_db():
    engine = create_engine('sqlite:///db.sqlite', echo=True)
    s = sessionmaker(bind=engine)
    return s()

def save_contact(name,phone,address,message):
    db = open_db()
    c = Contact(name=name, phone=phone, address=address, message=message)
    db.add(c)
    db.commit()
    db.close()

@app.route('/')
def index():
    db = open_db()
    contacts = db.query(Contact).all()
    db.close()
    return render_template('index.html', cnts=contacts)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    phone = request.form['phone']
    address = request.form['address']
    message = request.form['message']
    save_contact(name,phone,address,message)
    return redirect('/') 

if __name__ == '__main__':
  app.run(debug=True)
 