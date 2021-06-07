import csv
import os
#from budget.class.income import Income
from budget.classes.transaction import Transaction


class Budget:

    def __init__(self, name):
        self.name = name
        #self.income = Income.objects()
        self.transactions = Transaction.objects()


    def add_transaction(self, transaction_data):
        self.transactions.append(Transaction(**transaction_data))