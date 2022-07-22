from datetime import date

class DateHandler:
    def __init__(self) -> None:
        pass

    def today_date(self):
        return date.today()

    def time_between_dates(self, d1, d2):
        return int(abs((d2 - d1).days))

