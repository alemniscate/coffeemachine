class CoffeMachine:

    stock = []
    status = ""

    def __init__(self, stock):
        self.stock = stock
        self.menu()

    def show_stock(self):
        print(f"""The coffee machine has:
{self.stock[0]} of water
{self.stock[1]} of milk
{self.stock[2]} of coffee beans
{self.stock[3]} of disposable cups
${self.stock[4]} of money""")
        print()
        self.menu()

    def sale_espresso(self):
# 250 ml of water and 16 g of coffee beans. It costs $4.
        onecup = [250, 0, 16, 1, 4]
        self.update_stock(onecup)

    def sale_latte(self):
# 350 ml of water, 75 ml of milk, and 20 g of coffee beans. It costs $7.
        onecup = [350, 75, 20, 1, 7]
        self.update_stock(onecup)

    def sale_cappuccino(self):
# 200 ml of water, 100 ml of milk, and 12 g of coffee beans. It costs $6.
        onecup = [200, 100, 12, 1, 6]
        self.update_stock(onecup) 

    def update_stock(self, onecup):
        new_stock = [0] * 5
        for i in range(0, len(self.stock)):
            if i == 4:
                new_stock[i] = self.stock[i] + onecup[i]
            else:
                new_stock[i] = self.stock[i] - onecup[i]
        if min(new_stock) < 0:
            print("Sorry, not enough water!")
            return False
        for i in range(0, len(self.stock)):
            self.stock[i] = new_stock[i]
        print("I have enough resources, making you a coffee!")
        return True

    def fill(self):
        print("Write how many ml of water do you want to add:")
        self.status = "fill water"

    def fill_water(self, supply):
        self.stock[0] += int(supply)
        print("Write how many ml of milk do you want to add:")
        self.status = "fill milk"
    
    def fill_milk(self, supply):
        self.stock[1] += int(supply)
        print("Write how many grams of coffee beans do you want to add:")
        self.status = "fill beans"

    def fill_beans(self, supply):
        self.stock[2] += int(supply)
        print("Write how many disposable cups of coffee do you want to add:")
        self.status = "fill cups"

    def fill_cups(self, supply):
        self.stock[3] += int(supply)
        print()
        self.menu()

    def take(self):
        print(f"I gave you {self.stock[4]}")
        self.stock[4] = 0
        print()
        self.menu()

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        self.status = "buy"

    def select_kind(self, kind):
        if kind == "1":
            self.sale_espresso()
        elif kind == "2":
            self.sale_latte()
        elif kind == "3":
            self.sale_cappuccino()
        elif kind == "back":
            self.menu()
            return
        print()
        self.menu()

    def menu(self):
        print("Write action (buy, fill, take, remaining, exit):")
        self.status = "menu"
        
    def exit(self):
        self.status =""

    def select_menu(self, action):
        print()
        if action == "buy":
            self.buy()
        elif action == "fill":
            self.fill()
        elif action == "take":
            self.take()
        elif action == "remaining":
            self.show_stock()
        elif action == "exit":
            self.exit()
            return
    
    def input(self, input_):
        if self.status == "menu":
            self.select_menu(input_)
        elif self.status == "buy":
            self.select_kind(input_)
        elif self.status == "fill water":
            self.fill_water(input_)
        elif self.status == "fill milk":
            self.fill_milk(input_)
        elif self.status == "fill beans":
            self.fill_beans(input_)
        elif self.status == "fill cups":
            self.fill_cups(input_)

# the coffee machine has $550, 400 ml of water, 540 ml of milk, 120 g of coffee beans, and 9 disposable cups.
water = 400
milk = 540
beans = 120
cups = 9
money = 550

stock = [water, milk, beans, cups, money]
cm = CoffeMachine(stock)
while cm.status:
    cm.input(input())
