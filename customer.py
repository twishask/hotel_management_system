import hotel

class customer(object):
  id = 123467
  
  def __init__(self,aadhar):
  #  self.name = "ABC"
    self.aadhar = aadhar
    self.id = customer.id
    customer.id += 1
    
  def book_room(self,hotel):
    for room in hotel.list_of_rooms:
      if room.availability == True:
        room.availability = False
        room.customer_id = self.id
        break
   
  def checkout(self,room):
    room.availability = True
    room.customer_id = 0
    
