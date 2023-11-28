from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> Hello </h1>'

@app.route('/contact')
def contact():
    return 'Estoy en la ruta contact'

@app.route('/about')
def about():
    return '<h3> About me </h3>'

if __name__ == '__main__':
    app.run(debug= True)