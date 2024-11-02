from flask import Flask as flask,render_template as render,request,jsonify,redirect,session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import requests, secrets,datetime
secret_key = secrets.token_hex(16)  # Generates a 32-character hexadecimal string
app=flask(__name__)
api_key='0eda083fd1bffbbfa30e3946e54ed9a2'
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///user.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key=secret_key
# initialize the app with the extension
db=SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    date=db.Column(db.DateTime,default=datetime.datetime.utcnow)
    def __repr__(self):
        return f'<User {self.name } - {self.email} - {self.password}>'
with app.app_context():
    db.create_all()
# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data['name']
    email = data['email']
    password = data['password']

    # Check if email already exists
    if User.query.filter_by(email=email).first():
        return jsonify({'success': False, 'message': 'User already exists!'})

    # Create a new user
    hashed_password = generate_password_hash(password)
    new_user = User(name=name, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'success': True})

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']

    # Find the user in the database
    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password, password):
        session['user_id'] = user.id
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'message': 'Incorrect email or password!'})

# Route for the weather page (protected)
@app.route('/index')
def weather():
    if 'user_id' in session:
        return render("weather.html")  # Replace with your weather page template or data
    else:
        return redirect('/')  # Redirect to login if not logged in

@app.route('/')
def renderinit():
    return render("login.html")
@app.route('/weatherfetch', methods=['GET'])
def get_weather():
    city_name = request.args.get('city')
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
            'q': city_name,
            'appid': api_key,
            'units': 'metric'
        }

    response = requests.get(base_url, params=params)
    weather_data = response.json()
        
    if response.status_code == 200:
        return weather_data
    else:
        return jsonify({'error': 'City not found'}), 404
if __name__=='__main__':

    app.run(debug=True,port="8000")
