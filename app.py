from flask import Flask,render_template,request,redirect,session
from flask_pymongo import PyMongo
import datetime
from pymongo import MongoClient



app=Flask(__name__)



app.config["MONGO_URI"] = "uri"
mongo = PyMongo(app)


cluster = MongoClient("your_account_connection_link")
db = cluster["db"]
collection = db["userdata"]
collection2=db["projectdetail"]

# app.config["SECRET_KEY"]="grp01"
# app.config["MONGO_URI"] = "mongodb+srv://bondjames181920:Shreyash18@cluster0.d3op3bw.mongodb.net/?retryWrites=true&w=majority"
# mongo = PyMongo(app)
# db=mongo.db



@app.route('/')
def home():
	

	return render_template('login.html')    
   

@app.route('/registration')
def registration():
	return render_template('registration.html')

@app.route('/login',methods=['GET', 'POST'])
def login():
	prn=request.form.get('prn')
	password=request.form.get('password')
	# user = auth.sign_in_with_email_and_password(email,password)
	# username = db.child(user['localId']).child("Username").get().val()

	# if user:
	# 	return render_template('dashboard.html')    #return f"Welcome {username}!"

	note = collection.find_one({"prn":prn , "password":password})
	if note:
		session['prn']=prn
		return redirect("/dashboard")

	else:
		return "Invalid credentials"



@app.route('/registration1',methods=['GET', 'POST'])
def registration1():
	email=request.form.get('email')
	password=request.form.get('password')
	username=request.form.get('username')
	prn=request.form.get('prn')
	# user = auth.create_user_with_email_and_password(email, password)
	# user = auth.sign_in_with_email_and_password(email, password)
	# db.child(user['localId']).child("Username").set(username)
	user=mongo.db
	collection.insert_one({"email":email,"password":password,"username":username,"prn":prn})
	session['prn']=prn


	return redirect("/dashboard")

    

	
	#return redirect('/dashboard')

	# if user:
	# 	return render_template("dashboard.html")



@app.route('/adddata',methods=['GET', 'POST'])
def adddata():
	year=request.form.get('year')
	intro=request.form.get('intro')
	createdAt = datetime.datetime.now()
	domain=request.form.get('domain')
	achievement=request.form.get('achievement')
	# noteId = request.form['_id']
	if 'prn' in session:
		#uid=session[id]
		collection2.insert_one({"year":year,"intro":intro,"date":createdAt,"prn":session['prn'],"domain":domain,"achievement":achievement})

	else:
		return redirect("/")
	return redirect("/dashboard")

	
	
	
	# db.child(auth.current_user['localId']).child("Intro").set(intro)
	# db.child(auth.current_user['localId']).child("year").set(year)
	
@app.route('/getdata',methods=['GET','POST'])
def getdata():
	if 'prn' in session:
		notes=list(collection2.find({"prn":session['prn']}).sort("date",-1))
		return render_template("account.html",notes=notes)

	else:
		return redirect("/")
	# notes = list(mongo.db.projectdetail.find({}).sort("date",-1))

    # # render a view
	# return render_template("account.html",notes=notes)
	 
@app.route('/search',methods=['GET','POST'])
def search():
	query=request.form.get("query")
	if 'prn' in session:
		notes=list(collection2.find({"domain":query}).sort("date",-1))
		return render_template("account.html",notes=notes)
	else:
		return "No such project"



@app.route("/logout",methods=['GET','POST'])	
def logout():
	if "prn" in session:
		session.pop("prn",None)
		return redirect("/")



@app.route('/dashboard')
def dashboard():
	# if 'prn' in session:
	# 	return "you are logged in as" + session['prn']
    return render_template("dashboard.html")

@app.route('/addproject')
def addproject():
    return render_template("addproject.html")

@app.route('/team')
def team():
    return render_template("team.html")

@app.route('/account')
def account():
	return render_template('account.html')


if __name__ == '__main__':
	app.secret_key='grp01'
	app.run(debug=True)
	
