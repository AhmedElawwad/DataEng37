"""
Create a Budget class that can keep track of different budget categories like food, clothing, and entertainment.
These should allow for depositing and withdrawing funds from each category,
as well computing category balances and transferring balance amounts between categories

---
Requirements:

1. Method for depositing  - done
2. Method for withdrawing  - done
3. Method to check the current balance for each category  - done
4. Method to transfer the balance between the categories  - done

"""


class Categories:
    def __init__(self, category_name):
        self.category_name = category_name
        self.account = []

    def __repr__(self):
        return f" The category is {self.category_name}, and account is {self.account}"

    def __str__(self):
        return f"  {self.account}, total balance now is {self.get_total_amount()}"

    def depositing(self, amount, deposit_reason=""):
        self.account.append({"amount": amount, "deposit_reason": deposit_reason})

    def withdrawing(self, amount, withdraw_reason=""):
        if self.get_funds(amount):
            self.account.append({"amount": - amount, "withdraw_reason": withdraw_reason})

    def get_balance(self):
        total_cash = 0

        for i in self.account:
            total_cash += i["amount"]
        return total_cash

    def get_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        else:
            False

    def get_withdrawls(self):
        total = 0

        for each in self.account:
            if each["amount"] < 0:
                total += each["amount"]
        return total

    def transfer_to_categories(self, amount, category):

        if self.get_funds(amount):
            self.withdrawing(amount, "Transfer to " + category.category_name)
            category.depositing(amount, "Transfer from " + self.category_name)
            return True
        else:
            return False


    def get_total_amount(self):
        total = 0
        for item in self.account:
            total += item["amount"]
        output = "Total: " + str(total)
        return output


if __name__ == '__main__':
    shopping = Categories("shopping")
    shopping.depositing(3000, "first deposit")
    shopping.withdrawing(20, "To buy Veg")
    shopping.withdrawing(30.50, " To buy fruits")

    eating_out = Categories("shopping")
    eating_out.depositing(2000, "first deposit for eating out")
    shopping.transfer_to_categories(100, eating_out)

    print(shopping)
    print(eating_out)
