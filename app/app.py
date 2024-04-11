from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    coding_lang = request.form['coding_lang']
    company_names = {
        'python': ['Microsoft', 'Google', 'Facebook'],
        'java': ['Microsoft', 'Oracle', 'IBM'],
        'javascript': ['Microsoft', 'Google', 'Facebook']
    }
    if coding_lang.lower() in company_names:
        return render_template('result.html', companies=company_names[coding_lang.lower()])
    else:
        return render_template('result.html', companies=[])

if __name__ == '__main__':
    app.run(debug=True)
