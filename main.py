from flask import Flask, redirect, url_for, render_template, request
#wsgi application
app = Flask(__name__) #starting point

@app.route('/') #decorator and its binding function
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>') #dynamic
def success(score):
    res = ""
    if score >= 30:
        res="PASS"
    else:
        res="FAIL"
    result = {'score':score,'res':res}
    # if score > 30:
    #     res = "PASS"
    # else:
    #     res = "FAIL"
    return render_template('result.html', result = result)

# @app.route('/fail/<int:score>') #dynamic
# def fail(score):
#     return f"You've Failed and your score is {score}"

# @app.route('/result/<int:marks>') 
# def result(marks):
#     res = ""
#     if marks<30:
#         res = 'fail'
#     else:
#         res = 'success'
#     return redirect(url_for(res, score = marks))

@app.route('/submit', methods = ['POST', 'GET'])
def submit(): #read posted values
    total = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datasc = float(request.form['datascience'])
        total = (science+maths+c+datasc)/4

    # res = ""
    # if total > 30:
    #     res = "success"
    # else:
    #     res = "fail"
    return redirect(url_for('success', score = total))



if __name__ == '__main__':
    app.run(debug=True)