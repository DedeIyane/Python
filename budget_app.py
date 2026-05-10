class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description= ''):
        new_item = {'amount': amount, 'description' : description}
        self.ledger.append(new_item)

    def withdraw(self, amount, description= ''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for items in self.ledger:
            balance += items['amount']
        return balance

    def transfer(self, amount, destination):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {destination.name}")
            destination.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
        

    def check_funds(self, amount):
        return amount <= self.get_balance()
    

    def __str__(self):
        title = self.name.center(30, '*')
        items = ''

        for entry in self.ledger:
            description = entry['description'][:23]
            amount = f"{entry['amount']:.2f}"
            items += f"{description:<23}{amount:>7}\n"

        total = f"Total: {self.get_balance():.2f}"
        return title + "\n" + items.rstrip() + "\n" + total





def create_spend_chart(categories):
    spent = []

    # calculate total withdrawals per category
    for cat in categories:
        total = 0
        for item in cat.ledger:
            if item['amount'] < 0:
                total += -item['amount']
        spent.append(total)

    total_spent = sum(spent)

    percentages = [(s / total_spent * 100) for s in spent]

    chart = "Percentage spent by category\n"

    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "|"
        for p in percentages:
            chart += " o " if p >= i else "   "
        chart += " \n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(c.name) for c in categories)

    for i in range(max_len):
        chart += "     "
        for c in categories:
            chart += (c.name[i] if i < len(c.name) else " ") + "  "
        chart += "\n"

    return chart.rstrip("\n")
