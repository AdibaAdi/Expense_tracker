class Expense:
    #init function to assign values to class 
    #None means funtion doesn't return anything
    def __init__(self, name, category, amount)-> None:
        self.name= name
        self.category=category
        self.amount=amount
        
        
        #represent  memory address in string
        
    def __repr__(self):
        #will print following string instead random memory address
        return f"<Expense: {self.name}, {self.category}, ${self.amount:.2f}>"