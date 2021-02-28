import requests
from threading import Thread

def get_city(city_name, lang, units, TOKEN, list_cities=None, index=None):
    """
    :param city_name: The city name witch will be searched
    :param lang: The language than will be returned ('en' for English, 'fr' for French, 'pt_br' for Brazilian Portuguese)
    :param units: Type of weath will return ('metric' for Celsius, 'imperial' for fahrenheit, 'standard' for Kelvin)
    :param TOKEN: The token used to access the 'open weather api'.
    :param list_cities: If a list is passed, indicates a Thread process and the output will be passed in the list, else'
            just a city info is getting and the info will be returned
    :param index: A index if the list_cities is passed, to access by index the list_cities.

    :return: A list with city name in title case, the temperature, the weath description if list_cities is not passed
    """
    city = city_name.title()
    api_city_name = ','.join(city.split())
    url = f'https://api.openweathermap.org/data/2.5/weather?q={api_city_name}&units={units}&lang={lang}&appid={TOKEN}'
    data = requests.get(url).json()
    temp = data['main']['temp']
    description = data['weather'][0]['description']
    city_info = [city, int(temp), description]

    if list_cities:
        list_cities[index] = city_info
    else:
        return city_info

def get_standarted_info(city_name, lang='en', units='metric', TOKEN='68dcc09865f92950175effb9381ee5d1'):
    """
    :param city_name: The city name witch will be searched
    :param lang: The language than will be returned ('en' for English, 'fr' for French, 'pt_br' for Brazilian Portuguese)
    :param units: Type of weath will return ('metric' for Celsius, 'imperial' for fahrenheit, 'standard' for Kelvin)
    :param TOKEN: The token used to access the 'open weather api'.
    :return: The info of city than was setted and a list with 5 cities infos.
    """
    city = get_city(city_name, lang=lang, units=units, TOKEN=TOKEN)
    cities_names = ['London', 'Rio de Janeiro', 'Toronto', 'Dubai', 'New York']
    list_cities = [None for _ in range(len(cities_names))]
    list_threads = []
    for key, name in enumerate(cities_names):
        thread = Thread(target=get_city, args=(name, lang, units, TOKEN, list_cities, key))
        list_threads.append(thread)
        thread.start()

    for thread in list_threads:
        thread.join()

    return city, list_cities
