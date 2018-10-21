import hotel
import room
import customer

h1 = hotel.hotel()
h2 = hotel.hotel()

r1 = room.room(h1)
r2 = room.room(h2)
r3 = room.room(h1)
r4 = room.room(h1)

c1 = customer.customer(132)
c2 = customer.customer(5454)

c1.book_room(h1)
c2.book_room(h1)

c1.checkout(r1)

r1.display_details()
r3.display_details()
