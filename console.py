import pdb

from models.session import Session
from models.member import Member 
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.session_repository as session_repository
import repositories.booking_repository as booking_repository

booking_repository.delete_all()
member_repository.delete_all()
session_repository.delete_all()

member1 = Member('Jarron Green')
member_repository.save(member1)

member2 = Member('Adam Simpson')
member_repository.save(member2)

member3 = Member('Louise Henderson')
member_repository.save(member3)

session1 = Session('Lower Body', 'Strength', '2021-12-21', '06:00:00')
session_repository.save(session1)

session2 = Session('Upper Body', 'Strength', '2021-12-21', '06:00:00')
session_repository.save(session2)

# session3 = Session('30 minute HIIT workout', 2021-12-21)

booking1 = Booking(member1, session1, 'I have a sore leg')
booking_repository.save(booking1)

booking2 = Booking(member2, session2, 'I pulled a muscle')
booking_repository.save(booking2)

print(member_repository.sessions(member1))
print(session_repository.members(session1))

pdb.set_trace()