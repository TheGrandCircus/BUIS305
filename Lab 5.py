number1 = int(input("Enter a number"))

if number1 % 3 == 0 and number1 % 5 == 0:
    print(f"{number1}, 'Tic Tac'")
elif number1 % 3 == 0:
    print(f"{number1}, 'Tic'")
elif number1 % 5 == 0:
    print(f"{number1}, 'Tac'")
else:
    print(f"{number1},'Number is not divisible by 3 or 5'")

number = 1
while number <= 20:
    if number % 3 == 0 and number % 5 == 0:
        print(f"{number1}, 'Tic Tac'")
