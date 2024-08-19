import tkinter as tk
from tkinter import messagebox
import json
import os

class FinanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Controle Financeiro")
        
        self.transactions = self.load_transactions()
        
        # Setup UI
        self.setup_ui()
        
        self.update_balance_values()

    def setup_ui(self):
        # Create UI elements
        self.transactions_listbox = tk.Listbox(self.root, height=10, width=50)
        self.transactions_listbox.pack(padx=10, pady=10)
        
        self.income_display = tk.Label(self.root, text="Receitas: R$ 0.00")
        self.income_display.pack(padx=10, pady=5)
        
        self.expense_display = tk.Label(self.root, text="Despesas: R$ 0.00")
        self.expense_display.pack(padx=10, pady=5)
        
        self.balance_display = tk.Label(self.root, text="Saldo: R$ 0.00")
        self.balance_display.pack(padx=10, pady=5)
        
        self.text_entry = tk.Entry(self.root)
        self.text_entry.pack(padx=10, pady=5)
        self.text_entry.insert(0, "Descrição")
        
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack(padx=10, pady=5)
        self.amount_entry.insert(0, "Valor")
        
        self.add_button = tk.Button(self.root, text="Adicionar Transação", command=self.add_transaction)
        self.add_button.pack(padx=10, pady=5)
        
        self.dark_mode = False
        self.toggle_button = tk.Button(self.root, text="Modo Escuro", command=self.toggle_dark_mode)
        self.toggle_button.pack(padx=10, pady=5)
        
    def load_transactions(self):
        if os.path.exists('transactions.json'):
            with open('transactions.json', 'r') as file:
                return json.load(file)
        return []

    def save_transactions(self):
        with open('transactions.json', 'w') as file:
            json.dump(self.transactions, file)

    def update_balance_values(self):
        total = sum(transaction['amount'] for transaction in self.transactions)
        income = sum(transaction['amount'] for transaction in self.transactions if transaction['amount'] > 0)
        expense = -sum(transaction['amount'] for transaction in self.transactions if transaction['amount'] < 0)
        
        self.balance_display.config(text=f"Saldo: R$ {total:.2f}")
        self.income_display.config(text=f"Receitas: R$ {income:.2f}")
        self.expense_display.config(text=f"Despesas: R$ {expense:.2f}")
        
        self.transactions_listbox.delete(0, tk.END)
        for transaction in self.transactions:
            operator = "+" if transaction['amount'] >= 0 else "-"
            self.transactions_listbox.insert(tk.END, f"{transaction['name']} {operator} R${abs(transaction['amount']):.2f}")
        
    def add_transaction(self):
        name = self.text_entry.get()
        amount = self.amount_entry.get()
        
        if not name or not amount:
            messagebox.showwarning("Entrada Inválida", "Por favor, preencha todos os campos.")
            return
        
        try:
            amount = float(amount)
        except ValueError:
            messagebox.showwarning("Entrada Inválida", "Por favor, insira um valor numérico válido.")
            return
        
        self.transactions.append({"id": len(self.transactions) + 1, "name": name, "amount": amount})
        self.save_transactions()
        self.update_balance_values()
        self.text_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode
        if self.dark_mode:
            self.root.config(bg='black')
            self.transactions_listbox.config(bg='grey', fg='white')
            self.income_display.config(bg='black', fg='white')
            self.expense_display.config(bg='black', fg='white')
            self.balance_display.config(bg='black', fg='white')
            self.toggle_button.config(text="Modo Claro")
        else:
            self.root.config(bg='white')
            self.transactions_listbox.config(bg='white', fg='black')
            self.income_display.config(bg='white', fg='black')
            self.expense_display.config(bg='white', fg='black')
            self.balance_display.config(bg='white', fg='black')
            self.toggle_button.config(text="Modo Escuro")

if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceApp(root)
    root.mainloop()
