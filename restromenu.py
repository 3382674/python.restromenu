menu = {
    'pizza':400,
    'burger':300,
    'salad':80,
    'soda':100,
    'water':25,
    'fries':150
}
print("welcome to PYTHON restaurant")
print("Here is our menu:")
print("pizza:400\nburger:300\nsalad:80\nsoda:100\nwater:25\nfries:150")
order_total=0
item_1=input("Enter the name of item you want to order")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"your item {item_1} has added to your order")
else:
    print("Sorry, we don't have this item in our menu")
another_order=input("do you like to order anything else?(yes/no)")
if another_order=="yes":
    item_2=input("enter th ename of second item")
    if item_2 in menu:
        order_total+=menu[item_2]
        print(f"your item {item_1} has added to your order")
    else:
        print("Sorry, we don't have this item in our menu")
print(f"the total amount is:{order_total}")        






