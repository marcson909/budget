import csv
import os

class Transaction:

    def __init__(self, date, name, amount, category):
        self.date = date
        self.name = name
        self.amount = amount
        self.category = category
        #transaction_categories = BudgetCategory.categories

   
    @classmethod
    def objects(cls):
        transactions = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/account.csv")

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                transactions.append(Transaction(**dict(row)))

        return transactions

