from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', name = 'Khanh')

@app.route('/login')
def login():
   return 'Login Page'

@app.route('/register')
def register():
    return 'Register Page'

if __name__ == '__main__':
   app.run()
