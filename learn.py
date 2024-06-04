from flask import Flask, redirect, url_for
#wsgi application
app = Flask(__name__) #starting point

@app.route('/') #decorator and its binding function
def welcome():
    return "welcome to my page"

# @app.route('/projects')
# def projects():
#     return "These are my projects"

@app.route('/success/<int:score>') #dynamic
def success(score):
    return f"You've passed and your score is {score}" #pass html noice

@app.route('/fail/<int:score>') #dynamic
def fail(score):
    return f"You've Failed and your score is {score}"

@app.route('/result/<int:marks>') 
def result(marks):
    res = ""
    if marks<30:
        res = 'fail'
    else:
        res = 'success'
    return redirect(url_for(res, score = marks))


if __name__ == '__main__':
    app.run(debug=True)