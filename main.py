
class Star_Cinema:
      _hall_list =[]
      def entry_hall(self,rows,cols,hall_no):
            Star_Cinema._hall_list.append({f"rows {rows},cols {cols} ,hall_no {hall_no} "})

class Hall(Star_Cinema) :
      def __init__(self,rows,cols,hall_no) -> None:
            self._seats={}
            self._show_list =[]
            self.__rows=rows
            self.__cols=cols
            self.hall_no=hall_no
            self.entry_hall(rows,cols,hall_no)

      def view_available_seats(self,id):
            check=False
            for key in self._seats:
                  
                  if key ==id:
                        check =True
                        seat_list=self._seats[id]
                        for i in self._show_list:
                              if i[0]==id:
                                    print(f"MOVIE NAME:{i[1]}              TIME :{i[2]}")
                        k=0
                        print("X seats are already booked")
                        print("----------------------------------------------------------------")
                        
                        for i in seat_list:
                              if i[1]==True:
                                    print("X",end="          ")
                              else:
                                    print(i[0],end="          ")
                              k+=1
                              if(k== self.__rows+1):
                                          print()
                                          k=0
                        print("----------------------------------------------------------------")
            if(check ==False):
                  print("INVALID SHOW ID")                

      def book_seat_function(self,id,seat_name):
             for key in self._seats:
                  if key ==id:
                        
                        seat_list=self._seats[id]
                        for i in seat_list:
                              if i[0] == seat_name:
                                          i[1]=True
                                          
                

      def check_seats(self,id,seat_name): 
            che=False
            for key in self._seats:
                  if key ==id:
                        
                        seat_list=self._seats[id]
                        for i in seat_list:
                              if i[0] == seat_name:
                                    che=True
                                    if i[1]==True:
                                          return -1
                                    else:
                                          
                                          return 1
            if che ==False:
                  return 0   



      def entry_show(self,id,movie_name,time):
            add =(id,movie_name,time)
            self._show_list.append(add)
            new_seat =[]
            
            for i in range(self.__rows) :
                  for j in range(self.__cols):
                        dirc=[f"{chr(65+i)}{j}" ,False]
                        new_seat.append(dirc)
            self._seats[id]=new_seat
      def book_seats(self,id,name,phone_num):
            detection =False
            for key  in self._seats:
                  if id ==key:
                        detection=True
            if(detection):
                  self.view_available_seats(id)
                  num =input("ENTER NUMBER OF TICKETS : ")
                  
                  if (num.isnumeric()):
                        num=int(num)
                        succ=True
                        seat_name=input("ENTER SEAT NO : ")
                        seat_name=seat_name.split(" ")
                        for seat in seat_name:
                              check =self.check_seats(id,seat)
                              if(check==-1):
                                     print(f"THIS {seat} SEAT IS ALREADY BOOKES")
                                     succ=False
                              elif (check ==0):
                                    print(f"INVALID SEAT {seat} .")
                                    succ=False
                                  
                                     

                        if (succ):
                              for seat in seat_name:
                                    self.book_seat_function(id,seat)

                              print("YOUR SEATS HAS BEEN BOOKED SUCCESSFULLY. ")
                              print(f"THANK YOU {name} ")
                        else:
                              print("TRY AGAIN")
                  else:
                        print("INVALID NUMBER")
            else:
                  print("INVALID ID")
                              
                  

      def view_show_list(self):
            print("--------------------------------------------------------------------------------------")
            print("SHOW ID       \t\tMOVIE NAME                 \t\tTime")
            for i in self._show_list:
                  print(i[0],"                  ",i[1],"            ",i[2],"                      ")


      
      
h = Hall(3,4,"HALL-1")
h.entry_show("ae12","Black Addam"," oct 30 10:00 am to 1.00 pm")
h.entry_show("ae50","Superman  ", " oct 30  02:00 am to 5.00 pm")


while(True):
      print("1. VIEW ALL SHOWS TODAY")
      print("2. VIEW AVAILABLE SEATS")
      print("3. BOOK SEATS")
      option =int(input("ENTER OPTION : "))
      
      if (option ==1):
            h.view_show_list()
      elif (option ==2):
            show_id=input("ENTER SHOW ID : ")
            h.view_available_seats(show_id)
      elif(option==3):
            customer_name =input("ENTER CUSTOMER NAME : ")
            customer_PHONE =input("ENTER CUSTOMER PHONE NUMBER : ")
            show_id=input("ENTER SHOW ID : ")
            h.book_seats(show_id,customer_name,customer_PHONE)
      else:
            print("INVALID INPUT")

      



