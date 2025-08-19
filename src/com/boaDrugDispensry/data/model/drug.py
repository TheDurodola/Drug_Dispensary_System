import datetime


class Drug:
    def __init__(self ):
        self._quantity = None
        self._id = None
        self._name = None
        self._id:int
        self._name:str
        self._type = 0
        self._category = 0
        self._expiry_date:datetime = None
        self._manufactured_date:datetime = None
        self._date_added:datetime = datetime.datetime.now()
        self._quantity:int


    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value


    @property
    def expiry_date(self):
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, value):
        self._expiry_date = value

    @property
    def manufactured_date(self):
        return self._manufactured_date

    @manufactured_date.setter
    def manufactured_date(self, value):
        self._manufactured_date = value

    @property
    def date_added(self):
        return self._date_added

    @date_added.setter
    def date_added(self, value):
        self._date_added = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

















