#!/usr/bin/env python
from Tkinter import *
import csv
import sys
'''reader = csv.reader(open('Budgetcsv.csv', 'rb'))
mydict = dict(reader)'''

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        '''self.mydict = {
        "Mortgage":0.0,
        "Electric/Gas":0.0,
        "Water":0.0,
        "Phone/Internet/Cable":0.0,
        "Insurance":0.0,
        "Vehicle":0.0,
        "Groceries":0.0,
        "Entertainment":0.0,
        "Savings":0.0,
        }
        writer = csv.writer(open('Budgetcsv.csv', 'wb'))
        for key, value in self.mydict.items():
           writer.writerow([key, value])
        sys.exit()'''
        reader = csv.reader(open('Budgetcsv.csv', 'rb'))
        self.mydict = dict(reader)
    
    def create_widgets(self):
        Label(self, text = "Budget Tracker").grid(row=0,column=0,sticky=W)
        Radiobutton(self, text = "Enter the amount of last paycheck", variable=self.create_widgets, value="1", command = self.amount).grid(row=2,column=0,sticky=W)
        Radiobutton(self, text = "Enter a personal expense", variable=self.create_widgets, value="2", command = self.expense).grid(row=3,column=0,sticky=W)
        Radiobutton(self, text = "Check the balances of the expenditure accounts", variable=self.create_widgets, value="3", command = self.balance).grid(row=4,column=0,sticky=W)
        Button(self, text = "Exit", command = self.exit).grid(row=5,column=0,sticky=W)
    
    def amount(self):
        for widget in self.winfo_children():
            widget.grid_forget()
        
        Label(self, text = "Enter the amount of your latest paycheck: (No dollar sign) ").grid(row=0,column=0,sticky=W)
        
        self.paycheck2 = Entry(self)
        self.paycheck2.grid(row=1,column=0,sticky=W)
        
        self.submit_button = Button(self, text = "Submit", command = self.submit)
        self.submit_button.grid(row=2,column=0,sticky=W)
        
        self.result = Text(self, width=40, height=5, wrap=WORD)
        self.result.grid(row=3, column=0, columnspan=2)
        
        self.back_button = Button(self, text = "Back", command = self.back)
        self.back_button.grid(row=4,column=0,sticky=W)
        
    def submit(self):
        self.paycheck = float(self.paycheck2.get())
        self.mortgage = self.paycheck*0.32
        self.electric_gas = self.paycheck*0.07
        self.water = self.paycheck*0.02
        self.phone_internet_cable = self.paycheck*0.04
        self.insurance = self.paycheck*0.12
        self.vehicle = self.paycheck*0.15
        self.groceries = self.paycheck*0.15
        self.entertainment = self.paycheck*0.03
        self.savings = self.paycheck*0.10
        
        message = "Thank you, the money has been distributed into your accounts as designated."
        self.result.delete(0.0, END)
        self.result.insert(0.0, message)  
        
    def expense(self):
        for widget in self.winfo_children():
            widget.grid_forget()
        
        Label(self, text = "Indicate which category the expense is from: ").grid(row=0,column=0,sticky=W)
        
        self.personal_expense = Entry(self)
        self.personal_expense.grid(row=1,column=0,sticky=W)
        
        Label(self, text = "Cost: ").grid(row=3,column=0,sticky=W)
        
        self.cost2 = Entry(self)
        self.cost2.grid(row=4,column=0,sticky=W)
        
        self.submit_button2 = Button(self, text = "Submit", command = self.submit2)
        self.submit_button2.grid(row=5,column=0,sticky=W)
    
        self.result = Text(self, width=40, height=5, wrap=WORD)
        self.result.grid(row=6, column=0, columnspan=2)
        
        self.back_button = Button(self, text = "Back", command = self.back)
        self.back_button.grid(row=7,column=0,sticky=W)
        
    def submit2(self):
        self.category = self.personal_expense.get()
        self.cost = self.cost2.get()
        
        if self.category.lower() == "mortgage":
            self.mortgage = float(self.mydict['Mortgage']) - float(self.cost)
        self.mydict['Mortgage'] = self.mortgage     
        
        if self.category.lower() == "electric/gas" or self.category.lower() == "electric" or self.category.lower() == "gas":
            self.electric_gas = float(self.mydict['Electric/Gas']) - float(self.cost)
        self.mydict['Electric/Gas'] = self.electric_gas
        
        if self.category.lower() == "water":
            self.water = float(self.mydict['Water']) - float(self.cost)
        self.mydict['Water'] = self.water
        
        if self.category.lower() == "phone" or self.category.lower() == "internet" or self.category.lower() == "cable" or self.category.lower() == "phone/internet/cable":
            self.phone_internet_cable = float(self.mydict['Phone/Internet/Cable']) - float(self.cost)
        self.mydict['Phone/Internet/Cable'] = self.phone_internet_cable
    
        if self.category.lower() == "insurance":
            self.insurance = float(self.mydict['Insurance']) - float(self.cost)
        self.mydict['Insurance'] = self.insurance
    
        if self.category.lower() == "vehicle":
            self.vehicle = float(self.mydict['Vehicle']) - float(self.cost)
        self.mydict['Vehicle'] = self.vehicle
            
        if self.category.lower() == "groceries":
            self.groceries = float(self.mydict['Groceries']) - float(self.cost)
        self.mydict['Groceries'] = self.groceries
            
        if self.category.lower() == "entertainment":
            self.entertainment = float(self.mydict['Entertainment']) - float(self.cost)
        self.mydict['Entertainment'] = self.entertainment
            
        if self.category.lower() == "savings":
            self.savings = float(self.mydict['Savings']) - float(self.cost)
        self.mydict['Savings'] = self.savings
            
        message = "Thank you, the account balance has been updated."
        self.result.delete(0.0, END)
        self.result.insert(0.0, message)  
    
    def balance(self):
        for widget in self.winfo_children():
            widget.grid_forget()
            
        Label(self, text = "Indicate the account you would like the balance of: ").grid(row=0,column=0,sticky=W)
        
        self.account_balance = Entry(self)
        self.account_balance.grid(row=1,column=0,sticky=W)
        
        self.submit_button = Button(self, text = "Submit", command = self.submit3)
        self.submit_button.grid(row=2,column=0,sticky=W)
        
        self.result = Text(self, width=40, height=5, wrap=WORD)
        self.result.grid(row=3, column=0, columnspan=2)
        
        self.back_button = Button(self, text = "Back", command = self.back)
        self.back_button.grid(row=4,column=0,sticky=W)
        
    def submit3(self):
        self.account = self.account_balance.get()
        
        if self.account.lower() == "mortgage":
            message = "The balance of this account is: $"+str(self.mydict['Mortgage'])+"."
            
        if self.account.lower() == "electric/gas" or self.account.lower() == "electric" or self.account.lower() == "gas":
            message = "The balance of this account is: $"+str(self.mydict['Electric/Gas'])+"."
        
        if self.account.lower() == "water":
            message = "The balance of this account is: $"+str(self.mydict['Water'])+"."
        
        if self.account.lower() == "phone" or self.account.lower() == "internet" or self.account.lower() == "cable" or self.account.lower() == "phone/internet/cable":
            message = "The balance of this account is: $"+str(self.mydict['Phone/Internet/Cable'])+"."
    
        if self.account.lower() == "insurance":
            message = "The balance of this account is: $"+str(self.mydict['Insurance'])+"."
    
        if self.account.lower() == "vehicle":
            message = "The balance of this account is: $"+str(self.mydict['Vehicle'])+"."
            
        if self.account.lower() == "groceries":
            message = "The balance of this account is: $"+str(self.mydict['Groceries'])+"."
            
        if self.account.lower() == "entertainment":
            message = "The balance of this account is: $"+str(self.mydict['Entertainment'])+"."
            
        if self.account.lower() == "savings":
            message = "The balance of this account is: $"+str(self.mydict['Savings'])+"."

        self.result.delete(0.0, END)
        self.result.insert(0.0, message) 
    
    def back(self):
        for widget in self.winfo_children():
            widget.grid_forget()
        Label(self, text = "Budget Tracker").grid(row=0,column=0,sticky=W)
        Radiobutton(self, text = "Enter the amount of last paycheck", variable=self.create_widgets, value="1", command = self.amount).grid(row=2,column=0,sticky=W)
        Radiobutton(self, text = "Enter a personal expense", variable=self.create_widgets, value="2", command = self.expense).grid(row=3,column=0,sticky=W)
        Radiobutton(self, text = "Check the balances of the expenditure accounts", variable=self.create_widgets, value="3", command = self.balance).grid(row=4,column=0,sticky=W)
        Button(self, text = "Exit", command = self.exit).grid(row=5,column=0,sticky=W)
            
    def exit(self):
        
        writer = csv.writer(open('Budgetcsv.csv', 'wb'))
        for key, value in self.mydict.items():
           writer.writerow([key, value])
        sys.exit()
        
        
root=Tk()
root.title("Budget Tracker")
root.geometry("600x500")
app=Application(root)
root.mainloop()