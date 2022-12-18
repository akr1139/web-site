from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')

def index():
    return render_template("index.html")


@app.route('/page 1/')

def index1():
    return "page 1"

@app.route('/page 2/')

def index2():
    return "page 2"




if __name__ == '__main__':
    app.run(debug=True)
