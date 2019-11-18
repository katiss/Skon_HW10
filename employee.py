
class Employee:

  def __init__(self,FirstName,LastName,TelNumber,RoomNumber):
    self.FirstName=FirstName
    self.LastName=LastName
    self.TelNumber=TelNumber
    self.RoomNumber=RoomNumber

  def DirString(self):
    result=self.LastName+", "+self.FirstName+" - Room "+self.RoomNumber+" - "+self.TelNumber
    return result
