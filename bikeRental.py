import datetime

class BikeRental:
    def __init__(self,stock=0):
        """ Constructor that instantiates bike rental shop"""
        
        self.stock = stock
    
    def display_stock(self):
        """ Displays the bikes currently available for rental """
        
        print(f"We currently have {self.stock} bikes available for rent in the shop")
        return self.stock
    
    def Rent_bike_on_hourly_basis(self,n):
        """ Rents bikes on Hourly basis to the customers """
        
        #Reject invalid input
        if n <= 0:
            print("Number of bikes is invalid")
            return None
        
        #Do not rent bikes if requested number is greater than stock
        elif n > self.stock:
            print(f"Sorry! We currently have {self.stock} bikes available to rent. ")
            return None
        
        #Rent bikes
        else:
            now = datetime.datetime.now()
            print(f"You have rented {n} bikes on hourly basis today at {now.hour} hours.")
            print("You will be charged $5 for each hour per bike")
            print("We hope that you enjoy our service")
                  
            self.stock -= n
            return now
                  
    def Rent_bike_on_daily_basis(self,n):
        """ Rents bikes on Daily basis to the customers """
        
        #Reject invalid input
        if n <= 0:
            print("Number of bikes is invalid")
            return None
        
        #Do not rent bikes if requested number is greater than stock
        elif n > self.stock:
            print(f"Sorry! We currently have {self.stock} bikes available to rent. ")
            return None
        
        #Rent bikes
        else:
            now = datetime.datetime.now()
            print(f"You have rented {n} bikes on daily basis today at {now.hour} hours.")
            print("You will be charged $20 for each day per bike")
            print("We hope that you enjoy our service")
                  
            self.stock -= n
            return now
          
    def Rent_bike_on_weekly_basis(self,n):
        """ Rents bikes on Weekly basis to the customers """
        
        #Reject invalid input
        if n <= 0:
            print("Number of bikes is invalid")
            return None
        
        #Do not rent bikes if requested number is greater than stock
        elif n > self.stock:
            print(f"Sorry! We currently have {self.stock} bikes available to rent. ")
            return None
        
        #Rent bikes
        else:
            now = datetime.datetime.now()
            print(f"You have rented {n} bikes on weekly basis today at {now.hour} hours.")
            print("You will be charged $60 for each week per bike")
            print("We hope that you enjoy our service")
                  
            self.stock -= n
            return now
         
    def return_bike(self,request):
        """ Accept rented bikes from customer, replenish the inventory, return a bill """
        #extract the tuple and initiate bill
        rentalBasis, rentalTime, numOfBikes = request
        bill = 0
         
                  
         #issue a bill if all parameters are not null
        if rentalTime and rentalBasis and numOfBikes:
                self.stock += numOfBikes
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime
                  
                #hourly bill
                if rentalBasis == 1:
                     bill = round(rentalPeriod.seconds / 3600) *5 * numOfBikes
                  
                #daily bill
                elif rentalBasis == 2:
                     bill = round(rentalPeriod.days) *20 * numOfBikes
                  
                 #weekly bill
                elif rentalBasis == 3:
                     bill = round(rentalPeriod.days / 7) *60 * numOfBikes
                  
                #family discount
                if (3<= numOfBikes <=5):
                    print("You are eligible for family rental promotion for 30% discount")
                    bill = bill * 0.7
                  
                print("Thanks for returning your bike. Hope you enjoyed our service")
                print(f"That would be ${bill}")
                return bill
        else:
            print("Are you sure you rented a bike with us?")
            return None
                
class Customer:
        def __init__(self):
            """constructor for customer objects"""
            self.bikes = 0
            self.rentalBasis = 0
            self.rentalTime = 0
            self.bill = 0

        def request_bike(self):
            """Takes request for number of bikes"""

            bikes = input("How many bikes would you like to rent: ")
             
            #invalid input
            try:
                  bikes = int(bikes)
             
            except ValueError:
                print("Enter a valid number")
                return -1
             
            if bikes <1:
                print("Enter a valid number")
                return -1
            else:
                  self.bikes = bikes
            return self.bikes
                  
        def return_bike(self):
            """Allows customer to return a bike"""
            
            if self.rentalBasis and self.rentalTime and self.bikes:
                return self.rentalBasis, self.rentalTime, self.bikes
            else:
                return 0,0,0