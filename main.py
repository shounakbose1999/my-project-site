from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/Contacts')
def layout():
    return render_template('Contacts.html')
@app.route('/Trainings')
def Training():
    return render_template('Trainings.html')
@app.route('/projects')
def projects():
    return render_template('projects.html')
@app.route('/Academics')
def academics():
    return render_template('Academics.html')


app.run(debug=True)