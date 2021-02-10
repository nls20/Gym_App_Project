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

member1 = Member('Jan Metelski')
member_repository.save(member1)

member2 = Member('Brian Bell')
member_repository.save(member2)

member3 = Member('Alex Rabisse')
member_repository.save(member3)

member4 = Member('Andrew Hunter')
member_repository.save(member4)

member5 = Member('David Taylor')
member_repository.save(member5)

member6 = Member('James Beedle')
member_repository.save(member6)

member7 = Member('Jenny Bulford')
member_repository.save(member7)

member8 = Member('Mark Burns')
member_repository.save(member8)

member9 = Member('Simon Elmslie')
member_repository.save(member9)

session1 = Session('Lower Body HIIT', 'Cardio', '2021-01-14', '06:00:00')
session_repository.save(session1)

session2 = Session('Kettlebells', 'Strength', '2021-01-15', '07:30:00')
session_repository.save(session2)

session3 = Session('Unwind', 'Stretch', '2021-01-16', '09:00:00')
session_repository.save(session3)

session4 = Session('Ab & Core Blitz', 'Tone', '2021-01-16', '18:00:00')
session_repository.save(session4)

session5 = Session('Upper Body', 'Strength', '2021-01-17', '18:30:00')
session_repository.save(session5)

booking1 = Booking(member1, session1, '2021-01-17', '18:30:00')
booking_repository.save(booking1)

booking2 = Booking(member2, session2, session2.date, session2.time)
booking_repository.save(booking2)

print(member_repository.sessions(member1))
print(session_repository.members(session1))
# member1.name='Malcolm'
# member_repository.update(member1)

pdb.set_trace()