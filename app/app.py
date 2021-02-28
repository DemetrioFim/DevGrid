from flask import Flask, render_template, request
from weather_tools import get_city

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main_page():
    if request.method == 'GET':
        return render_template('main_page.html')
    elif request.method == 'POST':
        city_name = request.form['input_city']
        city = get_city(city_name=city_name)

        cities_names = ['London', 'Rio de Janeiro', 'Toronto', 'Dubai', 'New York']
        list_cities = []
        for name in cities_names:
            city_name = get_city(city_name=name)
            list_cities.append(city_name)

        return render_template('main_page.html', city=city, list_cities=list_cities)




if __name__ == "__main__":
    app.run()
