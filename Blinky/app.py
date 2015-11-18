import os
from flask import Flask, jsonify, abort, g
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

# Database paths
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, '../blinky_db.sqlite')

# Configuration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DB_PATH
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
auth = HTTPBasicAuth()

# Database Models
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

# Authentication
@auth.verify_password
def verify_password(username, password):
    g.user = User.query.filter_by(username=username).first()
    if g.user is None:
        return False
    return g.user.verify_password(password)

@app.before_request
@auth.login_required
def before_request():
    pass

# Error handling
class ValidationError(ValueError):
    pass

@auth.error_handler
def unauthorized():
    response = jsonify({'status': 401, 'error': 'authorized',
                        'message': 'please authenticate'})
    response.status_code = 401
    return response

@app.errorhandler(ValidationError)
def bad_request(e):
    response = jsonify({'status': 400, 'error': 'bad request',
                        'message': e.args[0]})
    response.status_code = 400
    return response

@app.errorhandler(404)
def not_found(e):
    response = jsonify({'status': 404, 'error': 'not found',
                        'message': 'invalid resource URI'})
    response.status_code = 404
    return response

@app.errorhandler(500)
def internal_server_error(e):
    response = jsonify({'status': 500, 'error': 'internal server error',
                        'message': e.args[0]})
    response.status_code = 500
    return response

#  Api
@app.route('/api/root/', methods=['GET'])
def root_api():
    endpoints = [route.rule for route in app.url_map.iter_rules()
                 if route.endpoint !='static']
    return jsonify(dict(api_endpoints=endpoints))

@app.route('/api/led/<int:pin>/set/<state>/', methods=['POST'])
def set_led(pin, state):
    # Assume that GPIO setup is made
    if state in ['off']:
        return jsonify(dict(message="LED is set OFF", pin=pin))
    if state in ['on']
        return jsonify(dict(message="LED is set ON", pin=pin))
    return abort(404)

@app.route('/api/led/<int:pin>/status/', methods=['POST'])
def led_status(pin):
    # Led status is True (ON) / Falsw (OFF)
    # Assume that status is always False
    return jsonify(dict(status=False, pin=pin))

if __name__ == '__main__':
    db.create_all()
    if User.query.get(1) is None:
        u = User(username='blinky')
        u.set_password('blinky')
        db.session.add(u)
        db.session.commit()
    app.run(debug=True)
