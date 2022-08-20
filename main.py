from flask import Flask, render_template

from gradecalc import compute_grade


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

    
    
@app.route("/user/<username>")
def username(username):
    return render_template('namereader.html', username = username)

    

@app.route("/grade/<int:gradenumber>")
def grade(gradenumber):
    gradeNo = compute_grade(gradenumber)
    return render_template('grade.html', grade = gradeNo)


    
if __name__ == '__main__':
    app.run(debug=True, port=8000)
