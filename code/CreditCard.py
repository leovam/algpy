class CreditCard:
    def __init__(self, customer, bank, acnt, limit, balance=0):

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance
    
    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price):
        if type(price) == int or type(price) == float: 
            if price + self._balance > self._limit:
                return False
            else:
                self._balance += price
        else:
            raise ValueError('Price must be numeric...')
    
    def make_payment(self, amount):
        if type(amount) == int or type(amount) == float:
            if amount >= 0:
                self._balance -= amount
            else:
                raise ValueError('Payment must be a positive number ... ')
        else:
            raise ValueError('Paymemnt must be a number...')
#test
if __name__ == '__main__':
    cc = CreditCard('John Doe', '1st Bank', '5391 0375 5309', 1000, 100)
    print cc.get_balance()
    # cc.charge(400)
    # print cc.get_balance()
    # cc.make_payment(-100)
    # print cc.get_balance()
