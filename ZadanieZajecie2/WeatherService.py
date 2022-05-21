import requests


class   WeatherService:
    @staticmethod
    def getWeather(year, month, day):
        response        =   requests.get(f"https://www.metaweather.com/api/location/523920/{year}/{month}/{day}/").json()
        firstTemp       =   response[0]['the_temp']
        return firstTemp
