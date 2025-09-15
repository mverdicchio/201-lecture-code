# countdown #
def countdown():
    n = int(input("enter countdown "))
    while n > 0:
        print(n, "...")
        n -= 1  # n = n - 1
    print("BLASTOFF!!!")


# sum of numbers #
def sum_of_numbers():
    total = 0
    n = int(input("Enter numbers, zero to stop. "))
    while n != 0:
        total = total + n    # total += n
        n = int(input("Enter numbers, zero to stop. "))

    print(total)

# average of list #
def avg_of_list():
    scores = [99, 94, 97, 98, 89, 92]

    total = 0
    for num in scores:
        total += num

    print(total / len(scores))
    # print(sum(scores)/len(scores))

# factorial calculator #
def factorial():
    n = int(input("enter factorial "))
    fact = 1
    while n > 0:
        fact = fact * n   # fact *= n
        n -= 1

    print(f"the answer is {fact}")



def main():
    # countdown()
    # sum_of_numbers()
    # avg_of_list()
    factorial()

main()
