from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main_page():
    if request.method == 'GET':
        return render_template('main_page.html')
    elif request.method == 'POST':
        city = request.form['input_city']
        return render_template('main_page.html', city=city)




if __name__ == "__main__":
    app.run()