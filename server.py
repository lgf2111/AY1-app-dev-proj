from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/about')
def about():
    return render_template('about.html', title='About Us')


@app.route('/faq')
def faq():
    return render_template('workflow.html', title='Workflow')


@app.route('/login')
def login():
    return render_template('login.html', title='Login')


@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html', title="Sign Up")


if __name__ == '__main__':
    app.run(debug=True)
