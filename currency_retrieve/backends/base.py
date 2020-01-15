class BaseBackend:
    alias = None  # class attribute

    def extract(self, start_date, end_date, currencies=None):
        raise NotImplementedError()

    def transform(self):
        raise NotImplementedError()

    def load(self):
        raise NotImplementedError()
