import requests
import datetime as dt
# import currency_retrieve.backends.base as base
from currency_retrieve.backends.base import BaseBackend


class NbuBackend(BaseBackend):
    alias = 'nbu'
    api_url = 'https://api.privatbank.ua/p24api/exchange_rates?json&date={date}'

    def extract(self, start_date, end_date):
        assert isinstance(start_date, dt.date), '`start_date` must be of type `date`'
        assert isinstance(end_date, dt.date), '`end_date` must be of type `date`'

        min_date = min(start_date, end_date)
        max_date = max(start_date, end_date)

        next_date = min_date
        result = []

        while True:
            data = self._download_data(next_date)
            result.append(data)

            next_date = next_date + dt.timedelta(days=30)
            if next_date > max_date:
                break

        return result

    def transform(self):
        pass

    def load(self):
        pass

    def _download_data(self, on_date):
        """
        datetime formating https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
        :param on_date:
        :return:
        """
        date_str = on_date.strftime('%d.%m.%Y')
        request_url = self.api_url.format(date=date_str)
        response = requests.get(request_url)

        if response.status_code == 200:
            return response.json()
        else:
            return None
