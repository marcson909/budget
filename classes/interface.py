from budget.classes.budget import Budget

class BudgetInterface:
  
    def __init__(self, budget_name):
        self.budget = Budget(budget_name)

    def run(self):
        while mode != '5':
            mode = input(self.menu())

            if mode == '1':
                self.budget.list_transactions()
            elif mode == '2':
                self.find_transaction()
            elif mode == '3':
                self.add_transaction()
            elif mode == '4':
                self.remove_transaction()
            elif mode == '5':
                break  
    
    def menu(self):
        return "\nWhat would you like to do?\nOptions:\n1. List All Transactions\n2. View Individual Transaction <transaction_id>\n3. Add a Transaction\n4. Remove a Transaction <transaction_id>\n5. Quit\n"
        
    def find_transaction(self):
        transaction_id = input('Enter transaction id:')
        transaction_string = str(self.budget.find_transaction_by_id(transaction_id))
        print(transaction_string)

    def add_transaction(self):
        transaction_data = { 'date': input('Enter transaction date:\n')}
        transaction_data['name'] = input('Enter transaction name:\n')
        transaction_data['amount'] = input('Enter transaction amount: \n')
        #transaction_data['balance'] = calculate_balance()
        transaction_data['category'] = input('Enter transaction category: \n')

        self.budget.add_transaction(transaction_data)

    def remove_transaction(self):
        transaction_id = input("Please enter the transaction id:\n")
        self.budget.delete_transaction(transaction_id)