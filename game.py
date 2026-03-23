command = ""
while command.lower() != "quit":
    command=input(">").lower()

    if command =="start":
        print("Car starting")
    elif command== "stop":
        print("car stopped")    
    elif command == "help":
        print(""" 
         start -to start a car
         stop - to stop a car
         quit - to quit a car""")  
    elif command == "quit":
      break     
    else:
        print("pls i don't understand")    