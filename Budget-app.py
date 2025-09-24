# John Marsland budget app project, last updated 9/24/25
class Category():
    # initialize a budget category along with its respective 
    # ledger
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def __str__(self):
        # create title 
        len_title = len(self.category)
        star_num = (30 - len_title)//2
        title = '*'*star_num + self.category + '*'*star_num
        transactions = ''
        # for loop to format transactions
        for trans in self.ledger:
            transaction_des = trans['description'][:23]
            transaction_amount = f"{trans['amount']:.2f}"
            spaces = ' '*(30-len(transaction_des)-len
                            (transaction_amount))
            transaction = transaction_des + spaces + transaction_amount
            transactions += f'{transaction}\n'
        balance = str(self.get_balance())
        total = 'Total: '+ balance
        message = f'{title}\n{transactions}{total}'
        return message

    # method to determine whether enough funds are  
    # present for an amount to withdraw/transfer
    def check_funds(self, amount):
        return amount <= self.get_balance()

    # method to add money to a category's ledger
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': 
                            description})

    # method to use money from a category's ledger
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 
                                'description': description})
            return True
        return False

    # method to check the balance of the category's ledger
    def get_balance(self):
        return sum(self.ledger[i]['amount'] for i
                   in range(len(self.ledger)))

    # method to transfer funds from one category to another
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.category}')
            category.deposit(amount, 
                             f'Transfer from {self.category}')
            return True
        return False
    


def create_spend_chart(categories):
    real_categories = [category.category for category in categories]
    # Calculate percentages
    category_spend = {}
    category_percentages = {}
    for category in categories:
        category_spend[category.category] = 0
        category_transactions = []
        for transaction in category.ledger:
            if transaction['amount'] < 0:
                category_transactions.append(-transaction['amount'])
        category_spend[category.category] = sum(category_transactions)
    total_spend = sum(category_spend[str(i.category)] for i in 
                      categories)
    for category in categories:
        category_percentages[category.category] = int(category_spend[category.category]/total_spend*100)// 10 * 10

    name_list = [name for name in category_percentages]
    name_lengths = [len(name) for name in category_percentages]
    longest = max(name_lengths)
    num_names = len(category_percentages)

    title = 'Percentage spent by category\n'
    chart = ''
    line_length = 3 * len(name_list)

    for num in range(100, -10, -10):
        line = ' ' + str(num)
        if num == 100:
            line = str(num)
        elif num == 0:
            line = ' ' + line
        chart += line + '| '

        dots = ''
        for name in category_percentages:
            if category_percentages[name] >= num:
                dots += f'o  '
            else:
                dots += '   '
        while len(dots) < line_length:
            dots += ' '
        chart += dots
        chart += '\n'

    dashes = '    '+ '-'*(len(dots)+1)
    names = ''
    for i, name in enumerate(name_list):
        if len(name) < longest:
            name_list[i] += ' '*(longest-len(name))
    for i in range(longest):
        num = 1 
        for name in name_list:
            if num == 1:
                names += '\n     ' + name[i]
            elif num == len(name_list):
                names += '  ' + name[i] + '  '
            else:
                names += '  '+name[i]
            num += 1
    message = title + chart + dashes + names
    lines = message.split('\n')
    line_len = [len(line) for line in lines]
    return message
response = 1
stored_categories = {}
intro = True
while response != 0:
    if intro:
        print("Welcome to the budget app. To begin, please enter new budeget categories")
        print("Enter number of categories to be added below (2-4).")
        num_cat = int(input("Enter number of categories you will add: "))
        for i in range(num_cat):
            name = input(f'Enter name for category {i+1}: ')
            stored_categories[i+1] = Category(name)
        intro = False

    print("\nEnter number corresponding to your choice:")
    print("0: Exit app")
    print("1: deposit money into an existing category")
    print("2: withdraw money from an existing category")
    print("3: print transactions and total for category")
    print("4: generate spending chart of current categories")
    response = input("Your choice: ")
    print('\n')
    response = int(response)
    
    if response == 1:
        print("Enter the number of which category you would like to deposit in.")
        message = ''
        for i, category in stored_categories.items():
            message += f'{i}: {category.category}\n'
        print(message)
        depo_cat = int(input("Enter category number: "))
        depo_amount = int(input("Enter amount to deposit: "))
        stored_categories[depo_cat].deposit(depo_amount)
    
    if response == 2:
        print("Enter the number of which category you would like to withdraw from.")
        message = ''
        for i, category in stored_categories.items():
            message += f'{i}: {category.category}\n'
        print(message)
        with_cat = int(input("Enter category number: "))
        with_amount = int(input("Enter amount to withdraw: "))
        stored_categories[with_cat].withdraw(with_amount)
    
    if response == 3:
        print("Enter the number of which category you would like to display.")
        message = ''
        for i, category in stored_categories.items():
            message += f'{i}: {category.category}\n'
        print(message)
        display_cat = int(input("Enter category number: "))
        print(stored_categories[display_cat])
        
    if response == 4:
        categories_tot = stored_categories.values()
        print(create_spend_chart(categories_tot))
