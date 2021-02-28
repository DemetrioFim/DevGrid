from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<city>')
def main_page(city=None):
    return render_template('main_page.html', city=city)

if __name__ == "__main__":
    app.run()