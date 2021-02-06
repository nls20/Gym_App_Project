class Booking:

    def __init__(self, member, session, comment, id=None):
        self.member = member
        self.session = session
        self.comment = comment
        self.id = id