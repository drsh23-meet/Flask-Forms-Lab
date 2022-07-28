from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)
app.config['SECRET_KEY'] = 'super-secret-key'
login1={'dror':'123','a':'2122','b':'3233'}
password={}
username = "dror"
password = "123"
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]
friends_exits='name'

@app.route('/', methods=['GET','POST'])  # '/' for the default page
def login():
	if request.method=='POST':
		for i in login1:
			if request.form['username']==i and request.form['password']==login1[i]:
				return redirect(url_for('home'))
			else:
				return render_template('login.html')		
	else:
		return render_template('login.html')

@app.route('/home')
def home():
	return render_template("home.html",facebook_friends=facebook_friends)

	
@app.route('/friends_exits/<string:name>',methods=['GET','POST'])
def friends_exits(name):
	return render_template('friend_exists.html',facebook_friends=name)



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		debug=True
	)