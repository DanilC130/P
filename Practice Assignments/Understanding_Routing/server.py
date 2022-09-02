from flask import Flask, render_template
app = Flask(__name__)



@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def say(name): 
    return f'Hi, {name}!'

@app.route('/repeat/<int:times>/<phrase>')
def repeat(times, phrase):
    repeat = times * phrase
    return repeat






if __name__ == "__main__":
    app.run(debug=True)