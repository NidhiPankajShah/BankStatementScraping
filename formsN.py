from flask import Flask, render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

app = Flask(__name__)
app.config['SECRET_KEY'] ='dev'


class LoginForm(FlaskForm):
	username = StringField('username')
	password = PasswordField('password')
	
class RegisterForm(FlaskForm):
	username = StringField('username')
	password = PasswordField('password')
	email = StringField('email')
	
	
@app.route('/form',methods=['POST','GET'])
def form():
	form = LoginForm()
	
	if form.validate_on_submit():
		name=request.form['username']
		print(name)
		return "Hi"+name
		#return render_template('success.html')
		
	return render_template('forms.html',form=form)
	
@app.route('/register',methods=['POST','GET'])
def register():
	form1 = RegisterForm()
	
	if form1.validate_on_submit():
		name=request.form1['username']
		print(name)
		return "Hi"+name
		#render_template('success.html')
		
	return render_template('Registerform.html',form=form1)
	
	
if __name__=='__main__':
	app.run(debug=True)