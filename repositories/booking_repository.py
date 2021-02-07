from db.run_sql import run_sql
from models.booking import Booking
import repositories.member_repository as member_repository
import repositories.session_repository as session_repository

def save(booking):
    sql = "INSERT INTO bookings ( member_id, session_id, date, time) VALUES ( %s, %s, %s, %s) RETURNING id"
    values = [booking.member.id, booking.session.id, booking.date, booking.date]
    results = run_sql( sql, values )
    booking.id = results[0]['id']
    return booking

def select_all():
    bookings = []

    sql = "SELECT * FROM bookings"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row['member_id'])
        session = session_repository.select(row['session_id'])
        booking = Booking(member, session, row['date'], row ['date'], row['id'])
        bookings.append(booking)
    return bookings

def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)
