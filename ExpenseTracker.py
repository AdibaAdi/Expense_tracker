from expense import Expense
import calendar
import datetime


# Define ANSI color codes
RED = "\033[91m"
GREEN = "\033[92m"
ENDC = "\033[0m"


def main():
    print(f"🎯 Running expence Tracker!")
    #declare file name and path
    expense_file_path= "expense.csv"
    budget= 2000
    
    
    #Get Uer input for expense
    expense= get_user_expense()
    # print(expense)
    
    
    #Write their expense to a file
    save_expense_to_file(expense, expense_file_path)
    
    #read the file and summarize expenses
    summarize_expense(expense_file_path, budget)
    


def get_user_expense():
    print(f"get user expense")
    #input function
    Expense_name= input("Enter Expense Name:")
    #input is always string, so we convert the amount to float
    expense_amount = float(input("Enter expense amount:"))
    
    
    #for category make the user choose from the list
    expense_category= [
        "🍲 Food", 
        "🏡 Home", 
        "🏢 Work", 
        "🎉 Fun", 
        "✨ Misc"
    ]
    while True:
        print("Select a category: ")
        for i, cat_name in enumerate(expense_category): #enumerate iterated through a list (,1) means will start from 1 instead 0
            print(f" {i+1}.{cat_name}") 
            
        #store the selected index
        value_range= f"[1 - {len(expense_category)}]" #will be 1 to 5
        
        selected_index= int(input(f"Enter a category Number {value_range}: ")) -1 #so that user won't put 0 index starting
        
        if selected_index in range(len(expense_category)):
            selected_category= expense_category[selected_index]
            new_expense=Expense(
                name=Expense_name, category=selected_category, amount=expense_amount) 
            #importing from expense class and construct values
            
            return new_expense
        else:
            print("Invalid Category!! Please try again.")
            
    


def save_expense_to_file(expense: Expense, expense_file_path):#expense: Expense is a type hint to get suggestions 
    print(f"Saving expense: {expense} to {expense_file_path}")
    #open the file
    with open(expense_file_path, "a", encoding="utf-8") as f:
        #since its csv, comma spe value, seprate all with comma
        f.write(f"{expense.name},{expense.amount}, {expense.category}\n")
  


def summarize_expense(expense_file_path, budget):
    #read the file, gather all data, turn them into obj and calculate the total and return it
    print(f"summarising expense")
    expense: list[Expense]=[]
    with open(expense_file_path, "r", encoding="utf-8") as f:
        #read each line with readline func
        lines= f.readlines()
        for line in lines:
            #print(line)
            strippped_line =line.strip()
            #split line by comma in python
            expense_name, expense_amount, expense_category= line.strip().split(",")
            #print(expense_name, expense_amount, expense_category)
            line_expense= Expense( name=expense_name, amount=float(expense_amount), category=expense_category)
            #print(line_expense)
            expense.append(line_expense)
    #print(expense)
    
    #get expenses by category using dictionary
    amount_by_category={}
    for expen in expense:
        key = expen.category
        if key in amount_by_category:
            amount_by_category[key]+= expen.amount
        else:
            amount_by_category[key]= expen.amount #creating new entry, starting value
    
    print(amount_by_category)

    
    print("Expenses by Category")
    for key, amount in amount_by_category.items():
        print(f" {key}: ${amount:.2f}")
            
    total_spent =sum([ex.amount for ex in expense])
    print(f"{RED}You have spent ${total_spent:.2f} this month!{ENDC}")
    
    
        #budget remaining
    remaining_budget= budget-total_spent
    print(f"{GREEN}Budget Remaining: ${remaining_budget:.2f}{ENDC}")

#how many days remaining in the month for the remaining budget
    #get the current date
    now = datetime.datetime.now()
        
    #get the number of days in the current month
    days_in_month= calendar.monthrange(now.year, now.month)[1]
        
    #calculate the remaining number of days in the current month
    remaining_days= days_in_month-now.day
        
    #print("Remaining days in the current month:", remaining_days)
        
        
    daily_budget= remaining_budget/remaining_days
    print(f"Daily Budget: {daily_budget}")



if __name__ =="__main__": #app will run only when we run it directly not import
    main()
    
    
    
#possible modifications: can turn the amounts in different colors