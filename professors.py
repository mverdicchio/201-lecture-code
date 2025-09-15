

# lists as a data structure
# lists are INDEXED - every item has a position, or "index"

faculty = ["Banik", "Joshi", "Zareen", "Dr. V"]

# you can read/write individual items using index in square brackets
# the list name as street, and index as the address
print(faculty[1])           # read access
faculty[3] = "Verdicchio"   # write access

for prof in faculty:
    print(prof)

# length always gives the count
print("The length is:", len(faculty))

for i in range(len(faculty)): # [0, 1, 2, 3]
    print(i + 1, faculty[i])

# write some code to create a list of your friends' names
# print them out one by one
# challenge: print the list backwards
i = 3
while i >= 0:
    print(faculty[i])
    i -= 1

# creating a list of user input of unknown length
user_data = []
data = int(input("Enter a number, zero to quit: "))
while data != 0:
    user_data.append(data)
    data = int(input("Enter a number, zero to quit: "))

print(user_data)
