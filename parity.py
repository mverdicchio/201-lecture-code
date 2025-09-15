

def main():
    x = int(input("What is x? "))
    if is_even(x):
        print("even")
    else:
        print("odd")    # "odd" is a literal string

def is_even(n):
    if n % 2 == 0:      # 0 and 2 are literal integers
        return True     # boolean literal
    else:
        return False

#pythonic version of is_even
def is_even2(n):
    return True if n % 2 == 0 else False

# practical version of is_even
def is_even3(n):
    return n % 2 == 0

