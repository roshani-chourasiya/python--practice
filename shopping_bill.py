product=input("enter product name:")
price=float(input("enter price:"))
quantity=int(input("enter quantity:"))
total=price*quantity
print("product:",product)
print("total:",total)
discount=total*0.10
final_bill=total-discount
print("discount:",discount)
print("final bill:",final_bill)
