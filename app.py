from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://d635ol9dqy:hjmSB6obEh@remotemysql.com:3306/d635ol9dqy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Bodol(db.Model):
    ''' 
    srn
    email
    msg
    date
    '''
    srn = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(20))
    message = db.Column(db.String(120))
    



@app.route("/")
def hello_world():
    return render_template("index.html")
    # return "<p>Hello, World!</p>"


@app.route("/contactus.html", methods = ['GET', 'POST'])
def contactus():
    if(request.method)=='POST':
        email = request.form.get('email')

        message = request.form.get('message')

        entry = Bodol(email=email, message=message)
        db.session.add(entry)
        db.session.commit()

    return render_template("contactus.html")

@app.route("/aboutus.html")
def aboutus():
    return render_template("aboutus.html")

if __name__ =="__main__":
    app.run(debug=True)