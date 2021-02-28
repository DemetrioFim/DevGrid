import requests

def get_city(city_name, lang='en', units='metric', TOKEN='68dcc09865f92950175effb9381ee5d1'):
    """

    :param city_name: The city name witch will be searched
    :param lang: The language than will be returned ('en' for English, 'fr' for French, 'pt_br' for Brazilian Portuguese)
    :param units: Type of weath will return ('metric' for Celsius, 'imperial' for fahrenheit, 'standard' for Kelvin)
    :param TOKEN: The token used to access the 'open weather api'.
    :return: A list with city name in title case, the temperature, the weath description.
    """
    city = city_name.title()
    api_city_name = ','.join(city.split())
    url = f'https://api.openweathermap.org/data/2.5/weather?q={api_city_name}&units={units}&lang={lang}&appid={TOKEN}'
    data = requests.get(url).json()
    temp = data['main']['temp']
    description = data['weather'][0]['description']
    final_result = [city, temp, description]
    print(final_result)
    return final_result