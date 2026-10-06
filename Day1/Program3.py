name = input("Enter your item name: ");
price = float(input("Enter your price: "));
quantity = input("Enter your quantity: ");

print("ITEM NAME ", name );
print("PRICE ", price );
print("QUANTITY ", quantity );

total = price * int(quantity);
print("TOTAL amount", total );

print("Thank you for shopping with us ...!");

print(type(name));
print(type(price));
print(type(quantity));