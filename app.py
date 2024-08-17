from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import random
import string

app = Flask(__name__)
app.secret_key = 'your_unique_secret_key'  # Change this to a random string

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Pavan%4012@localhost/registration'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.Text, nullable=False)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, name, email, phone, address, username, password):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.username = username
        self.password = generate_password_hash(password)

@app.route('/')
def index():
    return render_template('welcome.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/submit_registration', methods=['POST'])
def submit_registration():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    address = request.form['address']
    username = request.form['username']
    password = request.form['password']

    existing_user = Student.query.filter((Student.username == username) | (Student.email == email)).first()
    if existing_user:
        flash('Username or email already exists. Please choose a different one.')
        return redirect(url_for('register'))

    new_student = Student(name, email, phone, address, username, password)
    db.session.add(new_student)
    db.session.commit()

    flash(f'Thank you for registering, {name}!')
    return redirect(url_for('index'))

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    user = Student.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        flash('Login successful! Welcome, ' + username)
        return redirect(url_for('content_viewer'))  # Redirect to content viewer after login
    else:
        flash('Invalid username or password.')
        return redirect(url_for('login_page'))

@app.route('/content_viewer')
def content_viewer():
    return render_template('content_viewer.html')  # New route for content viewer

@app.route('/pythonmain')
def pythonmain():
    return render_template('pythonmain.html')  # New route for the Python main page

@app.route('/about')
def about():
    return render_template('about.html')  # New route for the about page

@app.route('/Python_Intro')
def Python_Intro():
    return render_template('Python_Intro.html')  # New route for the Python_Intro page

@app.route('/pythonget')
def pythonget():
    return render_template('pythonget.html')  # New route for the pythonget page

@app.route('/Python_syntax')
def Python_syntax():
    return render_template('Python_syntax.html')  # New route for the Python_syntax page

@app.route('/forgot_username', methods=['GET', 'POST'])
def forgot_username():
    if request.method == 'POST':
        email = request.form['email']
        user = Student.query.filter_by(email=email).first()
        if user:
            flash(f'Your username is: {user.username}')
        else:
            flash('Email not found.')
        return redirect(url_for('login_page'))
    return render_template('forgot_username.html')

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        username = request.form['username']
        user = Student.query.filter_by(username=username).first()
        if user:
            new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            user.password = generate_password_hash(new_password)
            db.session.commit()
            flash(f'Your temporary password is: {new_password}. Please use it to log in and change your password.')
            return redirect(url_for('change_password', username=username, temp_password=new_password))
        else:
            flash('Username not found.')
        return redirect(url_for('login_page'))
    return render_template('forgot_password.html')

@app.route('/change_password/<username>/<temp_password>', methods=['GET', 'POST'])
def change_password(username, temp_password):
    if request.method == 'POST':
        new_password = request.form['new_password']
        user = Student.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, temp_password):
            user.password = generate_password_hash(new_password)
            db.session.commit()
            flash('Your password has been changed successfully!')
            return redirect(url_for('login_page'))
        else:
            flash('Temporary password is incorrect or user not found.')
            return redirect(url_for('login_page'))
        
    return render_template('change_password.html', username=username)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
