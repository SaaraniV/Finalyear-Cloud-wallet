from app import Flask , render_template , request , redirect , url_for , session , flash
# import pymongo
import os
from pymongo import MongoClient


app = Flask(__name__)

app.secret_key='user-client'


cluster = MongoClient("mongodb+srv://sharanalwarswamy:sharanalwarswamy@cluster0.tu1qjxp.mongodb.net/?retryWrites=true&w=majority")
db = cluster['CloudWallet']
collection = db['users-collection']

# collection.insert_one(yukesh)

# db defs and methods

def insertdata(data): # create user and add to database 
    collection.insert_one(data)

def finddata(user): # returns is data is present in collection
    if user in collection:
        return True
    else:
        return False

# routing !!!

@app.route("/")
def indexPage():
    return render_template("indexPage.html")

@app.route("/create_account",methods=['POST','GET'])
def create_account():
    if request.method == 'POST':
        data = {
            "username":request.form['username'],
            "gmail":request.form['gmail'],
            "password":request.form['password'],
            "fileNames":[]
        }
        insertdata(data)
        print(request.form['username'] + "data inserted to database")
        # alert message kudakanum that account is created nu 
        return redirect(url_for('login'))

    return render_template("create_account.html")

@app.route("/login",methods=['POST','GET'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['gmail'] = request.form['gmail']
        session['password'] = request.form['password']
        user = collection.find_one({"username":session['username'] ,"gmail":session['gmail'] , "password":session['password']})
        if user :
            flash("you have loggedIN!!")
            return redirect(url_for('homepage'))
        else:
            flash("Wrong Credentials!!")
            return redirect(url_for("login"))
    return render_template("login.html")

@app.route("/homepage",methods=['POST','GET'])
def homepage():
    if "username" in session:
        if request.method == 'POST':
            if 'file' not in request.files:
                return 'No file part'

            file = request.files['file']

            if file.filename == '':
                return 'No selected file'

            if file:
                destination_folder = './uploads'
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)
                file = request.files['file']
                filename = os.path.join(destination_folder,file.filename)
                file.save(filename)
                print("file saved: "+file.filename)
                #add file name to mongo
                user1 = collection.find_one({"username": session['username'], "password": session['password']})
                fileArray = user1['fileNames']
                temp = session['username']+"-"+file.filename
                fileArray.append(temp)
                collection.update_one({"username": session['username'], "password": session['password']},{"$set": {"fileNames": fileArray}})
                flash("file added to your account!!")
                # AWS code to send to send file to s3
                # while adding to s3 add username before it <temp>
                os.remove('./uploads/'+file.filename)
                return render_template("homepage.html")
        return render_template("homepage.html")
    # prompt that user is out of session
    return redirect(url_for('indexPage'))

@app.route("/signout",methods=['POST','GET'])
def signout():
    if request.method == 'POST':
        flash("you have loggedOUT!!")
        session.pop('username',None)
        session.pop('gmail',None)
        session.pop('password',None)
        return redirect(url_for('indexPage'))
    return redirect(url_for('indexPage'))


# @app.route("/statichosting")
# def staticwebpage():
#     return render_template("statichosting.html")

if __name__=="__main__":
    app.run(host='0.0.0.0',port=8080,debug=True)