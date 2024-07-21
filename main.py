from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/do-login',methods=["POST"])
def do_login():
    username= request.form['username']
    password = request.form['password']

    return f"my username is {username} and password is {password}"

@app.route('/speed')
def speed():
    return render_template('speed.html')

@app.route('/find-speed', methods=["POST"])
def find_speed():
    distance = int(request.form['distance'])
    time = int(request.form['time'])
    result = distance/time
    return render_template("speed.html", result=result, distance = distance, time = time)

if __name__ == "__main__":
    app.run(debug=True)