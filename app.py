from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/submit',methods=['post'])

def greet():
    lname=request.form['lname']
    fname=request.form['fname']
    age=request.form['age']
    phno=request.form['phno']
    return render_template('greet.html',lname=lname,fname=fname,age=age,phno=phno)
if __name__=="__main__":
    app.run(debug=True)