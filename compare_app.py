from flask import Flask, render_template, request
import requests

app = Flask(__name__, template_folder='app/templates')

@app.route('/compare')
def compare():
    return render_template('compare.html')

@app.route('/compare-login', methods=['POST'])
def compare_login():
    username = request.form['username']
    password = request.form['password']

    # Post to insecure app
    insecure_response = requests.post('http://127.0.0.1:5000/login', data={
        'username': username,
        'password': password
    })

    # Post to secure app
    secure_response = requests.post('http://127.0.0.1:5001/login', data={
        'username': username,
        'password': password
    })

    return render_template('compare.html', username=username, password=password,
                           insecure_result=insecure_response.text,
                           secure_result=secure_response.text)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
