from flask import Flask, jsonify, abort

app = Flask(__name__)

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

