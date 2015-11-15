from flask import Flask, jsonify, abort

# Configuration
app = Flask(__name__)

# Error handling 
class ValidationError(ValueError):
    pass

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
@app.route('/api/root/')
def root_api():
    endpoints = [route.rule for route in app.url_map.iter_rules()
                 if route.endpoint !='static']
    return jsonify(dict(api_endpoints=endpoints))

@app.route('/api/led/<int:pin>/set/<state>/')
def set_led(pin, state):
    # Assume that GPIO setup is made
    if state in ['off']:
        return jsonify(dict(message="LED is set OFF", pin=pin))
    if state in ['on']:
        return jsonify(dict(message="LED is set ON", pin=pin))
    return abort(404)

@app.route('/api/led/<int:pin>/status/')
def led_status(pin):
    # Led status is True (ON) / Falsw (OFF)
    # Assume that status is always False
    return jsonify(dict(status=False, pin=pin))

@app.route('/api/login/')
def login():
    return "Login User"

@app.route('/api/logout')
def logout():
    return "Logout User"

if __name__ == '__main__':
    app.run(debug=True)

