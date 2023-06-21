from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    user = {
        "name": "Человек паук",
        "age": 16
    }
    return render_template('index.html', user=user)

@app.route('/contact')
def contact():
    user = {
    "name": "Человек паук",
    "age": 16
    }
    return render_template('contact.html', user=user)



if __name__ == '__main__':
    app.run(debug=True)



