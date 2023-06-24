from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('mainpage_2.html')

@app.route('/mapView', methods=['POST', 'GET'])
def index():
    return render_template('index.html', a=35.17, b=126.9)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8000)

