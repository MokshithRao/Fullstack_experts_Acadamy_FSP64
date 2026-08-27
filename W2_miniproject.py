menu_items = ["Burger", "Pizza", "Pasta", "Fries", "Coke"]
menu_prices = [120, 250, 180, 90, 50]

ordered_items = []
ordered_prices = []

while True:
    item = input("Enter items one by one (or 'done' to stop): ")
    if item == "done":
            print()
            break

    if item in menu_items:
        ordered_items.append(item)
        idx = menu_items.index(item)
        ordered_prices.append(menu_prices[idx])
    else:
         print("Invalid item does not exist in menu, Please chooose valid items.")


coupon_code = input("Enter a coupon code if have any: ")    

print("="*20)
print("        BILL         ")
print("="*20)

 
print("ITEMS PURCHASED:")

subtotal = 0
for i in range(len(ordered_items)):
      print(ordered_items[i], "-", ordered_prices[i])
      subtotal += ordered_prices[i]
print("-"*30)

print("Subtotal:", subtotal)

if coupon_code == "SAVE10":
    subtotal = subtotal - (subtotal*(10/100))
elif coupon_code == "WELCOME50":
    subtotal -= 50
else:
    print("Invalid Coupon")

print("subtotal after discount:", subtotal)  
gst = subtotal*(18/100)
print("18% GST:", gst)
print("Grand Total", subtotal+gst)


"""
Enter items one by one (or 'done' to stop): Burger
Enter items one by one (or 'done' to stop): Fries
Enter items one by one (or 'done' to stop): Coke
Enter items one by one (or 'done' to stop): done

Enter a coupon code if have any: SAVE10
====================
        BILL         
====================
ITEMS PURCHASED:
Burger - 120
Fries - 90
Coke - 50
------------------------------
Subtotal: 260
subtotal after discount: 234.0
18% GST: 42.12
Grand Total 276.12
"""