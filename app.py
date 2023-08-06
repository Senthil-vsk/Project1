from flask import Flask,render_template

app = Flask(__name__)
li = [1,2,3,4,5,6,7]
@app.route('/')
def home():
    # global li
    
    # name = "Senthil"
    return render_template('index.html', lists = li)
@app.route('/about')
def about():
    return render_template('about.html', lists = li)



if __name__ == "__main__":
    app.run(debug=True)

