import hotel
import customer

class room(object):
  id = 101
  
  def __init__(self,object):
    self.room_type = "Deluxe"
    self.max_capacity = 2
    self.availability = True
    self.id = room.id
    room.id += 1
    self.customer_id = 0
    self.hotel_id = object.id
    object.list_of_rooms.append(self)
    
  def display_details(self):
    print "Room ID:",self.id,"Hotel:",self.hotel_id,"Capaity:",self.max_capacity,"Type:",self.room_type,"Availability:",self.availability,"Customer ID:",self.customer_id
