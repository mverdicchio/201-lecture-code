

def get_number():
    while True:
        n = int(input("What is n? "))
        if n >= 0:
            return n

def pop_off(n):
    for _ in range(n):
        print("sir yes sir")

def main():
    reps = get_number()
    pop_off(reps)

main()

