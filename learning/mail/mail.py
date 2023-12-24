from flask import Flask, render_template , request ,redirect,url_for
from flask_mail import Mail,Message
import os

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'sharanalwar57@gmail.com'
app.config['MAIL_PASSWORD'] = 'hlrc bmfq qkel wezl'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
otp = "1234"
def random():
    return 1234

# @app.route('/home',methods=['GET','POST'])
@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        msg = Message("hey",sender='sharanalwar57@gmail.com',recipients=['sharanalwarswamy@duck.com'])
        msg.body = "Your otp is: 1234"
        mail.send(msg)
        return redirect(url_for('chumma'))
    return render_template('index.html')

@app.route('/chumma',methods=['GET','POST'])
def chumma():
    if request.method == 'POST':
        dotp = 1234
        if request.form['otp'] == str(dotp):
            return "good"
        else:
            return "bad"

    return render_template('chumma.html')

if __name__ == '__main__':
    app.run(debug=True)

    ##

# With reference to the telephonic conversation yesterday (9th December 2023) with you regarding my onboarding date at AVASOFT. 

# As discussed, I am a finalist in the prestigious Smart India Hackathon (SIH) , Meerut and my participation dates is from 18th December to 21st December (4 days only).

# I would be grateful if you could consider my onboarding date from January to accommodate my participation in SIH

# I understand that this may cause inconvenience, and I apologize for the same.

# Please let me know if I should fill out the onboarding form now and mention my temporary absence during the SIH dates?

# Thank you for your time and understanding. I look forward to your response.

# Sincerely,

# Sharan Alwarswamy
# ph: 6382117902