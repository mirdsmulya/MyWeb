from flask import Flask,request,redirect, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap =Bootstrap(app)
app._static_folder = "/home/mirdsm/project/flasky"

@app.route('/')
def main():
	return render_template('main_home.html')

@app.route('/para')
def parra():
	return render_template('parralax.html')


@app.route('/user-agent')
def user():
	user_agent = request.header.get('User-agent')
	return '<p> Your browser is %s </p>'% user_agent

@app.route('/profile')
def profile():
	name = 'Mirdan Syahid'
	return render_template('user.html')

@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/demo')
def demo():
	return render_template('parallax-demo.html')


if __name__ == '__main__':
	app.run()