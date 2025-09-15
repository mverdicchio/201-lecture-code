
def do_the_work(value1, value2):
    x = value1 / value2
    return x

x = float(input("enter x: "))
y = float(input("enter y: "))
number = do_the_work(x, y)

print(round(number, 2))
print(f"the answer is {number:,.2f}")
