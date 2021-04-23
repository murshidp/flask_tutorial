from flask import Flask,render_template, url_for
app = Flask(__name__)

posts =  [
    {
        'author' : "murshid",
        'title' : 'blog post 1',
        'content' : "first blog content",
        'date' : "20-04-2020"
    },
      {
        'author' : "sam",
        'title' : 'blog post 2',
        'content' : "second blog content",
        'date' : "20-03-2020"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",posts=posts)


@app.route("/about")
def about():
    return render_template("about.html",title="about")

if __name__ == '__main__':
    app.run(debug=True)