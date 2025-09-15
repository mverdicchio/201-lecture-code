

def main():
    # print(calculate_grade(75, 80))
    # print(calculate_grade(75, 0))
    # print(check_even_odd(14))
    # print(check_even_odd(15))

    print(check_loan_eligibility(17, 9999999999, 850))
    print(check_loan_eligibility(57, 24999, 850))
    print(check_loan_eligibility(47, 99999, 850))



def calculate_grade(score, total):
    if total == 0:
        return "What have you done?!?! Divide by zero? Not on my watch."

    percent = 100 * score / total
    return f"You scored {percent:.2f}%."

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


def check_loan_eligibility(age, income, credit):

#    if age >= 18 and income >= 25000 and credit >= 600:
    if age < 18 or income < 25000 or credit < 600:
        return "Not eligible"
    else:
        return "Eligible for loan"



def get_greeting(hour):
    match hour:
        case n if 6 <= n <= 11:
            return "Good morning!"
        case n if 12 <= n <= 17:
            return "Good Afternoon!"
        case n if 18 <= n <= 21:
            return "Good evening!"
        case _:
            return "Good night"

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def convert_temperature(temp, scale):
    if scale == "C": # convert to F
        return temp * (9/5) + 32
    else:
        return (temp - 32) * (5/9)

def find_largest(a, b, c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    if c > b and c > a:
        return c

def calculate_discount(price, code):
    match code:
        case "SALE10":
            price = price * 0.9
        case "SALE20":
            price = price * 0.8
        case "SALE30":
            price *= 0.7
    return f"Final price: ${price:.2f}"

def simple_calculator(a, b, op):
    match op:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a / b
        case _:
            return "error"


if __name__ == "__main__":
    main()
