print(10 * 5)
print(10 ** 2)
print(15 / 10)
print(15 // 10)
print(-15 // 10)
print(15 % 10)
print(10 % 15)
print(10 % 10)
print(0 % 10)
print(10 / 15)
# the last one creates a number that repeats forever so this causes an error as the number printed does not continue forever and is not properly rounded. 

#asks the user for exchange rate from euro to usd
rate = float(input("Input exchange rate from Euro to USD:"))
#asks for the amount of money 
amount = int(input("Input amount of money:"))
#convert euro to USD
total = rate * amount
#subtracts service fee
result = total - 3.00
print(result)