import datetime as dt
import json

from currency_retrieve.backends import NbuBackend
from currency_retrieve.exceptions import InvalidBackendAlias, CurrencyRetrieveException


class CurrencyService:
    backends = {
        NbuBackend.alias: NbuBackend
    }

    def download(self, backend_alias, start_date, end_date):
        backend_cls = self.backends.get(backend_alias, None)
        if backend_cls is None:
            raise InvalidBackendAlias('Invalid backend alias: {}'.format(backend_alias))

        backend = backend_cls()
        result = backend.extract(start_date, end_date)

        return result


service = CurrencyService()

end_date = dt.date.today()
start_date = end_date - dt.timedelta(days=365)

#df["start_date"] = ((df["today"] - df["date"]).map(lambda x: round(x.days/30)))
try:
    data = service.download('nbu', start_date, end_date)
except InvalidBackendAlias as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(data)
finally:
    print('finally')



#print(type(data))
#print(data[0]["date"])
""""""
#filename = 'privat.csv'
#myfile = open(filename, mode='w', encoding='Latin')
#json.dump(data, myfile)

#for datee in data

#print("Daty vymiry" + str(date['date']))