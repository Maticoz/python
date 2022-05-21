from unittest import result
import requests
from MyModel import ResultModelLastRecord


class StatsService:
    @staticmethod
    def get_stats(country):
        result = requests.get(f"https://api.covid19api.com/total/dayone/country/{country}").json()
        
        rs = ResultModelLastRecord(country,
        result[-1]['Confirmed'],
        result[-1]['Deaths'],
        result[-1]['Date'][0:10],
        result[-1]['Active'],
        )

        return rs

    @staticmethod
    def get_deaths_for_all_countries(countriesList):
        tab=[]
        
        for c in countriesList:
            stats = StatsService.get_stats(c)
            tab.append(stats.mystats['deaths'])
            
        return tab