from Employee import Employee 

e=Employee("Michael","Janet","345-456-2219","E443")

#list + strip files

#find errors

#define catorgories

#print string

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
