from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/welcome")
def welcome():
    return render_template('welcome.html')

@app.route("/regForm")
def RegForm():
    return render_template('regForm.html')

@app.route("/profile")
def Profile():
    return render_template('profile.html')

@app.route("/about")
def About():
    return render_template('About.html')

@app.route("/todo")
def todo():
    return render_template('todo.html')




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
