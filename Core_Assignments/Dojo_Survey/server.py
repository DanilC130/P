from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "survey" 

@app.route ('/')
def main_page():
    return render_template("index.html")
    

@app.route ('/process', methods=['post'])
def form_submission():
    session['form_data'] = request.form
    # print(request.form)
    return redirect ('/result')

@app.route ('/result')
def results():
    print (session['form_data'])
    return render_template('index2.html', data=session['form_data'])
    
    


if __name__ == "__main__":
    app.run(debug=True)