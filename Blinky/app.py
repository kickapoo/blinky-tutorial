from flask import Flask

app = Flask(__name__)

@app.route('/api/root/')
def root_api():
    return "List api endpoints"

@app.route('/api/led/<int:pin>/on/')
def set_led_on(pin):
    return "Set led attach to {} pin ON".format(pin)

@app.route('/api/led/<int:pin>/off/')
def set_led_off(pin):
    return "Set led attach to {} pin OFF".format(pin)

@app.route('/api/led/status/')
def led_status():
    return "Response led status"

@app.route('/api/login/')
def login():
    return "Login User"

@app.route('/api/logout')
def logout():
    return "Logout User"

if __name__ == '__main__':
    app.run(debug=True)

