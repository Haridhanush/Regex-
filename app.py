from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form['email']
    is_valid = re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email) is not None
    return render_template('index.html', email=email, is_valid=is_valid)
@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex_pattern']
    matches = re.findall(regex_pattern, test_string)
    return render_template('index.html', test_string=test_string, regex_pattern=regex_pattern, matches=matches)
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
