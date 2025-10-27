from flask import Flask, request, render_template
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('form.html')
@app.route('/submit',methods=['GET','POST'])
def submit():
    name=request.form('name')
    rollno=request.form('rollno')
    email=request.form('email')
    year=request.form('year')
    return render_template('result.html',name=name,rollno=rollno,email=email,year=year)
if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)