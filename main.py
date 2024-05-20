
#here is the class for the hotel which will be used as the parent class for a couple other classes.
class Hotel(object):
      def __init__(self, name, email, phone, avai_room, full_rooms, checkin, checkout):
         self.name = name
         self.email = email
         self.phone = phone
         self.avai_rooms = avai_room
         self.full_rooms = full_rooms
         self.checkin = checkin 
         self.checkout = checkout

H_info=Hotel("Sierra Madre Hotel", "sierrahelp@gamil.com", "0123456789", 150, 50, "12:00pm", "01:00pm")

#added a welcome message to make it more genuine 
print("Hello and welcome to",H_info.name,"booking system, Please fill in the customer name, contact details and billing details.")

print("\nFor more informations please contact our support team for any help or questions:\n")
print("Business Email:", H_info.email)
print("Customer Service Number:", H_info.phone)

#The firt while true statement for the first 4 options in the menu.
while True:
  #i added several try and except functions to make sure the user enters a number and not letters
  try:
    
     print("------------------------------------------------------------------------------")
     print("Here you can select the rooms you would like to book or have a look at our various on site events and facilities or look at payment options:")
     
     print("\n1) Rooms\n2) Facilities\n3) Events\n4) Checking In/Out and Payment Options\n")
    
     option = int(input("Type the number that you would like to go to: "))
    
     
     
     #ROOMS
     if option==1:
       
       while True:
         try:
          print("------------------------------------------------------------------------------")
          print("The Room Options:")
           
          print("\n1) Standard Room\n2) Silver Room\n3) Gold Room\n4) Return to Main Menu\n")
      
       
          #the input has to be a number or its not valid
          roomchoice=int(input("Please type the number of the room that you would like more information on: "))
  
          #the class room inherits several of the attributes from the hotel class whilst adding another 
          class Room(Hotel):
              def __init__(self, name, avai_rooms, full_rooms, checkin, checkout, room_cost):
               #adding None made it so this class could inherit the attributes from the hotel class and ignore the ones it didnt need.
               super().__init__(name, None, None, avai_rooms, full_rooms, checkin, checkout)
  
               self.room_cost = room_cost
  
  
          #all the different room given their attributes so they can be implimented into the code
          stan_room=Room("Standard", 135, 65, "12:00pm", "01:00pm", 70)
          silv_room=Room("Silver", 0, 20, "12:00pm", "01:00pm", 350)
          gold_room=Room("Gold",12 , 3 ,"12:00pm", "01:00pm", 1000)
           
           #STANDARD ROOM
          if roomchoice == 1:
            
              
               #the {} nad .format is put in so that the bits of information will appear in the right place and in the order that theyve been typed..
               print("------------------------------------------------------------------------------")
               print("You have selected the {} Room, this room costs £{} currently {} are booked and there are {} rooms available. You are able to book this room for {} but must leave by {}.".format(stan_room.name, stan_room.room_cost, stan_room.full_rooms, stan_room.avai_rooms, stan_room.checkin, stan_room.checkout))
             
          #SILVER ROOM
          elif roomchoice == 2:
                 
                 print("------------------------------------------------------------------------------")
                 print("You have selected the {} Room, this room costs £{} currently {} are booked and there are {} rooms available. You are able to book this room for {} but must leave by {}.".format(silv_room.name, silv_room.room_cost, silv_room.full_rooms, silv_room.avai_rooms, silv_room.checkin, silv_room.checkout))        
          #GOLD ROOM
          elif roomchoice == 3:
  
                 print("------------------------------------------------------------------------------")
                 print("You have selected the {} Room, this room costs £{} currently {} are booked and there are {} rooms available. You are able to book this room for {} but must leave by {}.".format(gold_room.name, gold_room.room_cost, gold_room.full_rooms, gold_room.avai_rooms, gold_room.checkin, gold_room.checkout))
      
          #this choice will return the user to the main menu instead of it just being enter
          elif roomchoice == 4:   
            
            break
          
          
          #if the user enters a number that isnt any in the elif statement it will be invalid and the user will be asked to enter
          else:
            print("------------------------------------------------------------------------------")
            print("THAT IS NOT A VALID OPTION PLEASE TRY AGAIN:")
  
        #this makes it so the code is still running even if the user enters a letter or a float
         except ValueError:
          print("------------------------------------------------------------------------------")
          print("THAT IS NOT A VALID OPTION PLEASE TRY AGAIN:")
  
         
     #FACIIITIES
     elif option == 2:
    
      while True:
        try:
          print("------------------------------------------------------------------------------")
          print("These are the facilities that the hotel provides: ")
          
          print("\n1) On-site Gym\n2) Swimming Pool\n3) Return to Main Menu\n")
          
          facil=int(input("Please type the number of the facility for more information: "))
         #i decided to just makes these strings so it just prints the infomation out there to see which of the 3 information types is more efficient for the user.
  
          #GYM
          if facil == 1:
                print("------------------------------------------------------------------------------")
                print("You have selected the On-Site Gym, this facility is located at the back of the hotel and is open 24/7. The gym is equipped with a variety of equipment including a treadmill, weights, a rowing machine and a sauna.")
            
          #POOL
          elif facil == 2:
            print("------------------------------------------------------------------------------")
            print("You have selected the Swimming Pool, this facility is located in the centre of the hotel and is open 7am-10pm and is closed on Tuesdays.")
  
          
          elif facil == 3:
      
           break
            
          else:
           print("------------------------------------------------------------------------------")
           print("THAT IS NOT A VALID OPTION PLEASE TRY AGAIN:")
           
        except ValueError:
         print("------------------------------------------------------------------------------")
         print("THAT IS NOT A VALID OPTION PLEASE TRY AGAIN:")
  
     #EVENTS
     elif option == 3:
    
          
              print("------------------------------------------------------------------------------")
              print("Here are the events that the hotel provides and information on them:")
             #i made the third option a dictionary to compare to the other 2 option is efficiency, reliability and userability
              hotel_event={
                "event type": "Conferences,",
                "location": "Banquet Hall",
                "start": "09:00am",
                "end": "12:00pm",
                "days": "Mondays, Wednesdays, Fridays.",
                  }   
       
              print("\n1) You are given the opportunity to have", hotel_event["event type"], "this event will be held at the", hotel_event["location"], "from", hotel_event["start"], "till" , hotel_event["end"], "on", hotel_event["days"])
            
              hotel_event["event type"] = "Meetings"
              hotel_event["days"]="Tuesdays, Thursdays."
       
              print("\n2) We also hold spaces for", hotel_event["event type"], "whcih can be held at the", hotel_event["location"], "from", hotel_event["start"], "till" , hotel_event["end"], "on", hotel_event["days"])
       
              hotel_event["event type"] = "Workshops,"
              hotel_event["start"]="01:00pm."
              hotel_event["end"]="04:00pm"
              hotel_event["days"] = "Monday-Friday."
              
              print("\n3) Customers may also book spaces for", hotel_event["event type"], "this event is held at the", hotel_event["location"], "from", hotel_event["start"], "till" , hotel_event["end"], "on", hotel_event["days"])
       
     #CECKIN IN/OUT PAYMENTS
     elif option == 4:
       
       
  
          #gave the payment options and balance a class so that the money owed and how they were paying could easily be tracked
           
       
           class payment(object):
             
             def __init__ (self, payoption1, payoption2, payoption3, balance,):
                self.payoption1 = payoption1
                self.payoption2 = payoption2
                self.payoption3 = payoption3
                self.balance=balance
                
  
           #this object class is similar to the other one with similar inheritance.
           class roombooking(Hotel):
            def __init__(self, name, avai_rooms, full_rooms, checkin, checkout, room_cost):
              super().__init__(name, None, None, avai_rooms, full_rooms, checkin, checkout)
              self.room_cost=room_cost
  
          #all the room information is here
           standard=roombooking("Standard Room", 135, 65, "12:00pm", "01:00pm", 70)
           silver=roombooking("Silver Room", 0, 20, "12:00pm", "01:00pm", 350)
           gold=roombooking("Gold Room", 12, 3, "12:00pm", "01:00pm", 1000)
          #payment options are given their names and the balance is set to 0 so that more can be added
           pay=payment("Paypal", "ATM Card", "Bitcoin", 0,)
          #here the selected benefits is empty but when an option is selected it will be added to the list
           selected_benefits=[]
            
           print("------------------------------------------------------------------------------")
  
          
           while True:
               try:
                   
                    print("Before we continue with your room please select any benefits that you would like to add to your stay:")
                    print("\n1) Breakfast - £10\n2) Lunch - £15\n3) Dinner - £17\n4) Buffet - £30\n5) continue\n")
                    benefit=int(input("Please select an option: ")) 
                    #this is to stop the option from being used multiple times and will bring an error message if its already in the list
                    if benefit==1 and benefit not in selected_benefits:
                     (pay.balance) = (pay.balance) + 10
                     selected_benefits.append(benefit)
                     print("------------------------------------------------------------------------------")
                     print("You have added Breakfast, your balance is now £", pay.balance)
                     print("------------------------------------------------------------------------------")
                      
                    elif benefit==2 and benefit not in selected_benefits:
                       (pay.balance) = (pay.balance) + 15
                       selected_benefits.append(benefit)
                       print("------------------------------------------------------------------------------")
                       print("You have added Lunch, your balance is now £", pay.balance)
                       print("------------------------------------------------------------------------------")
  
                    elif benefit==3 and benefit not in selected_benefits:
                       (pay.balance) = (pay.balance) + 17
                       selected_benefits.append(benefit)
                       print("------------------------------------------------------------------------------")
                       print("You have added Dinner, your balance is now £", pay.balance)
                       print("------------------------------------------------------------------------------")
  
                    elif benefit==4 and benefit not in selected_benefits:
                        (pay.balance) = (pay.balance) + 30
                        selected_benefits.append(benefit)
                        print("------------------------------------------------------------------------------")
                        print("You have added Lunch, your balance is now £", pay.balance)
                        print("------------------------------------------------------------------------------")
  
                    elif benefit==5 and benefit not in selected_benefits:
                       print("------------------------------------------------------------------------------")
                       print("You have selected to continue, your balance is now £", pay.balance)
                       print("Now it is stime to book in")
                       break
  
                      
                    else:
                      print("------------------------------------------------------------------------------")
                      print("THAT IS NOT A VALID OPTION PLEASE TRY AGAIN:")
                      print("------------------------------------------------------------------------------")
  
               except ValueError:
                print("------------------------------------------------------------------------------")
                print("THAT IS NOT A VALID OPTION PLEASE TRY AGAIN:")
                print("------------------------------------------------------------------------------")
        
          
       
           while True:
             try:
                print("------------------------------------------------------------------------------")
                print("Here are the rooms that you can select:\n")
                                 
                print("1) Standard Room\n2) Silver Room\n3) Gold Room\n")
                room_type=int(input("Please type the number of the room type you would like to book: "))
                             
                #standard room
                if room_type == 1:
                      print("------------------------------------------------------------------------------")   
                      while True:
                        try:
          
                         
                              choice=input("You have selected the standard room, is this correct Y/N?: ")
                              #choice.lower makes it so eithert capital or lower case y is a valid option but will only go through if the rooms are available
                              if choice.lower() == "y" and standard.avai_rooms > 0:
                                      #this adds the room cost to the balance         
                                      (pay.balance) = (pay.balance) + 70
                                      print("------------------------------------------------------------------------------")
                                
                                      print("Your balance is now £", pay.balance)
                                
                              elif standard.avai_rooms==0:
                                   print("unfortunately you cannot book this room at this time")
                                   break
      
                              elif choice.lower() == "n":
                                   print("------------------------------------------------------------------------------")
                                   print("Returning you to options")
                                   break
      
                              else:
                                   print("------------------------------------------------------------------------------")
                                   print("THAT IS NOT A VALID OPTION PLEASE TRY AGAIN:")
                                   break
                        except ValueError:
                          print("------------------------------------------------------------------------------")
                          print("THAT IS NOT A VALID OPTION PLEASE TRY AGAIN:")
                    
                                      #here is to input the day and date there was probably a better way but i couldnt figure it out yet, hope to learn in the future
                        while True:
                          try:
                              print("Please input the date that you will be arriving e.g (dd/mm)")
                              day = int(input("Enter the day into our system: "))
                              month = int(input("Enter the month into our system: "))
            
                              print("------------------------------------------------------------------------------")
                              #here the prevous day and month placed together with the options from the class added for the specific room type
                              if day <=31 and month <=12: 
                                 print("Your room is booked for", day, "/", month, "at", standard.checkin, "you will sadly have to part from us at", standard.checkout, "at the end of your stay and your total comes to £" , pay.balance)
                                                        
                                 while True:
                                      try:
                                        print("------------------------------------------------------------------------------")
                                        #here the payment options are presented for the customer using the object classes from before
                                        print("what method of payment will you be using")
                                        print("1) Paypal\n2) ATM Card\n3) Bitcoin\n")
                                        payoption = int(input("Please select an option: "))
                                                   
                                        if payoption == 1:
                                         print("------------------------------------------------------------------------------")
                                         print("You have selected", pay.payoption1, "You will shortly recieve a deducation from your account, thnk you for staying with the" , H_info.name, "and we look forward to seeing you soon!")
                                          #this ends the code 
                                         quit()
                  
                                                  
                                        elif payoption == 2:
                                          print("------------------------------------------------------------------------------")
                                          print("You have selected", pay.payoption2, "You will shortly recieve a deducation from your account, thnk you for staying with the" , H_info.name, "and we look forward to seeing you soon!")
                                          quit()
                  
                                        elif payoption == 3:
                                          print("------------------------------------------------------------------------------")
                                          print("You have selected", pay.payoption3, "You will shortly recieve a deducation from your account, thnk you for staying with the" , H_info.name, "and we look forward to seeing you soon!")
                                          quit()
                  
                                        else:
                                          print("------------------------------------------------------------------------------")
                                          print("THAT IS NOT A VALID OPTION PLEASE TRY AGAIN:")
                
                                      except ValueError:
                                          print("------------------------------------------------------------------------------")
                                          print("THAT IS NOT A VALID OPTION PLEASE TRY AGAIN:")

                              else:
                               print("THAT IS NOT A VALID OPTION PLEASE TRY AGAIN:")
                               print("------------------------------------------------------------------------------")


                          except ValueError:
                             print("------------------------------------------------------------------------------")
                             print("THAT IS NOT A VALID OPTION PLEASE TRY AGAIN:")
                             print("------------------------------------------------------------------------------")
                                                                
               
               #i could not figure out how to make this a lot more streamlined so i basically had to repeat it 3 times which is not ideal but i couldnt figure out a better way, hope to learn how to make it more efficient in the future
                #silver room
                elif room_type == 2:
                        print("------------------------------------------------------------------------------")   
                        while True:
                          
                          try:                      
                            
                            choice=input("You have selected the Silver room, is this correct Y/N?: ")
                            if choice.lower() == "y" and silver.avai_rooms > 0:
                                (pay.balance) = (pay.balance) + 350
                                print("------------------------------------------------------------------------------")
                                print("Your balance is now £", pay.balance)
                                break
              
                            elif silver.avai_rooms==0 :
                               print("------------------------------------------------------------------------------")
                               print("unfortunately you cannot book this room at this time")
                               break
              
                            elif choice.lower() == "n":
                               print("------------------------------------------------------------------------------")
                               print("Returning you to options")
                               break
              
                            else:
                               print("------------------------------------------------------------------------------")
                               print("THAT IS NOT A VALID OPTION PLEASE TRY AGAIN:")
              
                          except ValueError:
                             print("------------------------------------------------------------------------------")
                             print("THAT IS NOT A VALID OPTION PLEASE TRY AGAIN:")    
                            
                #gold room
                elif room_type == 3:
                   print("------------------------------------------------------------------------------")   
                   while True:
                     try:
  
  
                           choice=input("You have selected the Gold room, is this correct Y/N?: ")
                        
                           if choice.lower() == "y" and gold.avai_rooms > 0:
                                           
                                   (pay.balance) = (pay.balance) + 1000
                                   print("------------------------------------------------------------------------------")
  
                                   print("Your balance is now £", pay.balance)
                                  
                                   while True:
                                    try:
                                      print("Please input the date that you will be arriving e.g (dd/mm)")
                                      day = int(input("Enter the day into our system: "))
                                      month = int(input("Enter the month into our system: "))
          
                                      print("------------------------------------------------------------------------------")
          
                                      if day <=31 and month <=12: 
                                         print("Your room is booked for", day, "/", month, "at", gold.checkin, "you will sadly have to part from us at", gold.checkout, "at the end of your stay and your total comes to £" , pay.balance)
                            
                                         while True:
                                              try:
                                                print("------------------------------------------------------------------------------")
          
                                                print("what method of payment will you be using")
                                                print("1) Paypal\n2) ATM Card\n3) Bitcoin\n")
                                                payoption = int(input("Please select an option: "))
          
                                                if payoption == 1:
                                                 print("------------------------------------------------------------------------------")
                                                 print("You have selected", pay.payoption1, "You will shortly recieve a deducation from your account, thnk you for staying with the" , H_info.name, "and we look forward to seeing you soon!")
          
                                                 quit()
          
          
                                                elif payoption == 2:
                                                  print("------------------------------------------------------------------------------")
                                                  print("You have selected", pay.payoption2, "You will shortly recieve a deducation from your account, thnk you for staying with the" , H_info.name, "and we look forward to seeing you soon!")
                                                  quit()
          
                                                elif payoption == 3:
                                                  print("------------------------------------------------------------------------------")
                                                  print("You have selected", pay.payoption3, "You will shortly recieve a deducation from your account, thnk you for staying with the" , H_info.name, "and we look forward to seeing you soon!")
                                                  quit()
          
                                                else:
                                                  print("------------------------------------------------------------------------------")
                                                  print("THAT IS NOT A VALID OPTION PLEASE TRY AGAIN:")
          
                                              except ValueError:
                                                  print("------------------------------------------------------------------------------")
                                                  print("THAT IS NOT A VALID OPTION PLEASE TRY AGAIN:")
          
                                      else:
                                        print("------------------------------------------------------------------------------")
                                        print("THAT IS NOT A VALID OPTION PLEASE TRY AGAIN:")
                                        print("------------------------------------------------------------------------------")
                                    except ValueError:
                                      print("------------------------------------------------------------------------------")
                                      print("THAT IS NOT A VALID OPTION PLEASE TRY AGAIN:")
                                      print("------------------------------------------------------------------------------")
                           
                           
                           
                           elif standard.avai_rooms==0:
                                print("unfortunately you cannot book this room at this time")
                                break
  
                           elif choice.lower() == "n":
                                print("------------------------------------------------------------------------------")
                                print("Returning you to options")
                                break
  
                           else:
                                print("------------------------------------------------------------------------------")
                                print("THAT IS NOT A VALID OPTION PLEASE TRY AGAIN:")
                                break
                     except ValueError:
                       print("------------------------------------------------------------------------------")
                       print("THAT IS NOT A VALID OPTION PLEASE TRY AGAIN:")
  
                                 
                       
                else:
                  print("------------------------------------------------------------------------------")
                  print("THAT IS NOT A VALID OPTION PLEASE TRY AGAIN:")
                  
                  
             except ValueError:
                print("------------------------------------------------------------------------------")
                print("THAT IS NOT A VALID OPTION PLEASE TRY AGAIN:")
  
     else:
       print("------------------------------------------------------------------------------")
       print("THAT IS NOT A VALID OPTION PLEASE TRY AGAIN:")
 
  
  except ValueError:
    print("------------------------------------------------------------------------------")
    print("THAT IS NOT A VALID OPTION PLEASE TRY AGAIN:")


