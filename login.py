from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('3-5.html')

@app.route('/result', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        result = request.form
        print([[key, value] for key, value in result.items()])
    return render_template('3-5_result.html', result = result)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8000)

