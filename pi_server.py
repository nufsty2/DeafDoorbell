from flask import Flask

app = Flask(__name__)

@app.route('/ring')
def ring():
    return "Hello from the raspberry Pi!"

app.run(host='0.0.0.0', port=8090)
