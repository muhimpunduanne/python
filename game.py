command = ""

started = False
while command.lower() != "quit":
    command=input(">").lower()

    if command =="start":
        if started:
          print("Car is already started!!!!")
        else:
           started = True
           print("Car starting")
    elif command== "stop":
        if not started:
           print("car is already stop")
        else:
            started = False
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