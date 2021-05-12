class interest:
    ''' sets the interest rate and the principal loan amount '''
    def __init__(self, rate, principal):
        self.rate = rate
        self.principal = principal
        
p1 = interest(2.5, 300000)

def total_interest(x,y):
    total = (x/100) * y
    print(total)
    
total_interest(p1.rate, p1.principal)
