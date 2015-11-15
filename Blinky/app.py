from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/root/')
def root_api():
    return "List api endpoints"

@app.route('/api/led/<int:pin>/on/')
def set_led_on(pin):
    # Assume that GPIO setup is made
    return jsonify(dict(message="LED is set 'ON'", pin=pin)

@app.route('/api/led/<int:pin>/off/')
def set_led_off(pin):
    # Assume that GPIO setup is made
    return jsonify(dict(message="LED is set 'OFF'", pin=pin)

@app.route('/api/led/status/')
def led_status():
    # Led status is True (ON) / Falsw (OFF)
    # Assume that status is always False
    return jsonify(dict(status=False))

@app.route('/api/login/')
def login():
    return "Login User"

@app.route('/api/logout')
def logout():
    return "Logout User"

if __name__ == '__main__':
    app.run(debug=True)

