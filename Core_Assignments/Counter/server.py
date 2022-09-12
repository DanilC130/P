from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = "bgcounter"


@app.route('/') 
def display_page():
    if 'count' not in session:
        session['count'] = 0
    return render_template("index.html") 

@app.route('/counter')
def counting(): 
    session['count'] +=1
    return redirect ("/")

@app.route('/reset')
def reset_counter():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
