import locale
locale.setlocale( locale.LC_ALL, '' )
class Wallet:
    def __init__(self,money):
        self.money=money
    def __str__(self):
        return "I am a wallet with "+str(locale.currency(self.money))+" dollars"
    def spend(self, cost):
        self.money-=cost
        return "You now have "+str(locale.currency(self.money))+" dollars"




w=Wallet(4.5)
print w
print w.spend(2.1)
print w
        
