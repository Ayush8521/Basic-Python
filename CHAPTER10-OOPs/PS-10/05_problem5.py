'''
write a class train which has method to book a ticket, get status(no of seats)
and get fare information oa train running under indian railways.
'''

from random import randint

class Train:

    def _init_(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket booked in train no: {self.trainNo} from {fro} to {to}")

    def getStatus(self, trainNo):
        print(f"Train no: {self.trainNo} is running on time ")

    def getFare(self,trainNo, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222,5555)}")

t = Train(12345)
#t.book("Gorakhpur", "New Delhi")

t.getStatus(12345)
#t.getFare(12345, "Gorakhpur", "New Delhi")