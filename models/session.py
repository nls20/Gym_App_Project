class Session:

    def __init__(self, name, category, date, time, id=None):
        self.name = name
        self.category = category
        self.date = date
        self.time = time
        self.id = id