class Booking:

    def __init__(self, member, session, date, time, id=None):
        self.member = member
        self.session = session
        self.date = date
        self.time= time
        self.id = id