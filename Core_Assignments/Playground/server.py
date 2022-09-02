from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def Hello():
    return 'Hello'


@app.route('/play/<int:times>/<color>')
def playbox(times, color):
    return render_template('index.html', times=times, color=color)




if __name__ =="__main__":
    app.run(debug=True)