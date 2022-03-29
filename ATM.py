class Atm(object):
    def __init__(self, cardNumber,pinNumber):
        self.cardNumber= cardNumber
        self.pinNumber= pinNumber

    def cashWithdrawl(self):
        print(" Your cashWithdrawl")

    def balanceEnquiry(self):
         print("balanceEnquired")


rohit=Atm(1275,0000)
print(rohit.cashWithdrawl())