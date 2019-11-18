from Employee import Employee 

e=Employee("Michael","Janet","345-456-2219","E443")

#list + strip files
def loadRecs(filename):
  list=[]
  try:
    thefile=open(filename,'r')
    for line in thefile:
      line=line.strip().split()
      e=Employee(line[0],line[1],line[2],line[3])
      list.append(e)
      
#find errors
  except:
    print("Error reading:",filename)
  
  return(list)


#define catorgories
def inputRecs():
  num=1
  list=[]
  while True:
    print("Enter employee",num," (leave first name blank when done)")
    first=input("First name: ")
    if len(first)<1:
      break
    last=input("Last name: ")
    phone=input("Phone Number: ")
    room=input("Room: ")
    e=Employee(first,last,phone,room)
    list.append(e)
    
  return list


#print string
def displayRecs(list):
  for e in list:
    print(e.DirString())

EmpList=[]



#prompt user for file
def main():
  print("Enter 'F' to read employees from file, or 'I' to input directly,")
  op=input("Or anything else to exit: ")
  if op == 'F':
    filename=input("Enter filename? ")
    EmpList=loadRecs(filename)
  elif op == 'I':
    EmpList=inputRecs()
  displayRecs(EmpList)
    
main()
