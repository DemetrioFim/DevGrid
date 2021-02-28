from flask import Flask, render_template, request
from weather_tools import get_city, get_standarted_info

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main_page():
    if request.method == 'GET':
        return render_template('main_page.html')
    elif request.method == 'POST':
        city_name = request.form['input_city']
        city, list_cities = get_standarted_info(city_name)
        return render_template('main_page.html', city=city, list_cities=list_cities)


if __name__ == "__main__":
    app.run()
