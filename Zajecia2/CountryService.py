import requests

class CountriesService:
    @staticmethod
    def get_countries():
        tab=[]

        result = requests.get(f"https://api.covid19api.com/countries").json()

        for x in result:
            tab.append(x['Country'])

        tab.sort()
        
        return tab