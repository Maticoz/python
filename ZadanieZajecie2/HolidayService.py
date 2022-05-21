import requests


class   HolidayService:
    @staticmethod
    def getHolidays():
        response = requests.get(f"https://date.nager.at/api/v3/PublicHolidays/2022/PL").json()
        uniqueHolidays  =   []
        for x in response:
            if x['localName'] in uniqueHolidays:
                continue
            uniqueHolidays.append(x['localName'])

        return uniqueHolidays

    @staticmethod
    def getHolidayDates(fromYear, toYear, holiday):
        holidayDates  =   []
        for year in range(fromYear, toYear+1):
            response = requests.get(f"https://date.nager.at/api/v3/PublicHolidays/{year}/PL").json()
            for x in response:
                if x['localName'] == holiday:
                    holidayDates.append(x['date'])

        return holidayDates

