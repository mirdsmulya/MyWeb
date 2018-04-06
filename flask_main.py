from flask import Flask,request,redirect, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap =Bootstrap(app)

@app.route('/')
def main():
	return render_template('main_home.html')


@app.route('/user-agent')
def user():
	user_agennt = request.header.get('User-agent')
	return '<p> Your browser is %s </p>'% user_agennt

@app.route('/profile')
def profile():
	name = 'Mirdan Syahid'
	return render_template('user.html')


if __name__ == '__main__':
	app.run()