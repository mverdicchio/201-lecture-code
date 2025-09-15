
# void function (doesn't return any value)
def hello(to="world"):
    print("Hello", to)

# def hello():
#     print("Hello world")


def main():
    name = input("What's your name? ").strip().title()
    hello(name)
    hello()

main()
