class Parkinggarage():
    def __init__(self):   
            
        self.Ticket =list(range(20))
        self.parkingSpace=[range(20)]
        self.currentTicket = {"paid":[]}
        print(""" 
                1. check if there parking availabe:
                2. pay for parking space
                3. leaving the parking
                4. exit program """)
    def ParkingLot(self):
        
        print(f'Here is your available tickets list: {self.Ticket}')
        if self.Ticket != []:
            yourSpot = self.Ticket.pop()
            print(f'Here is your Spot: {yourSpot}')
            print(f'\nHere are the spots left over: {self.Ticket}.')
            
        else:
            print('Sorry to say it, there are no spots left here. Try one of my other garages, please!')
                
    def payForParking(self):
 
        user_input= input("Please type 'pay' for parking: ")
        if user_input.lower() == 'pay':
            payment=input("Enter the ticket number for payment: ")
            self.Ticket.pop(len(self.Ticket)-1)
            self.parkingSpace.pop(len(self.parkingSpace)-1)
            print(f"Ticket number {payment} successfully paid")
        else:
            print("incorrect option")

    def leavingGarage(self):
        user= input("Is the ticket have been paid? yes/no: ")
        if user.lower() =='yes':
            print('Thank you, have a nice day')
        elif user.lower()== 'no':
            payhere = input("Please make payment by type 'paid':")
            if payhere.lower() == 'paid':
                self.currentTicket["paid"].append([payhere])
            else:
                print('You have no pay yet')
                
            print("The payment have been make. Thank you, have a nice day")
            self.Ticket.pop(len(self.Ticket)+1)
            self.parkingSpace.pop(len(self.parkingSpace)+1)
        else: 
            print("You make a wrong selection")
    def checking(self):

        while True:
            checking =input("Please make a selection:")
            if checking =='1':
                p.ParkingLot()
            
            elif checking=='2':
                p.payForParking()
            elif checking == '3':
                p.leavingGarage()
            elif checking =='4':
                break
            else:
                print("You make a wrong option")
p=Parkinggarage()

p.checking()