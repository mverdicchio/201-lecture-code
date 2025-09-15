

# dictionaries, or associative arrays/lists
# map keys to values

faculty = ["Banik", "Joshi", "Zareen", "Dr. V"]
ranks   = ["COL", "LTC", "CPT", "LTC"]

faculty_ranks = {"Banik": "COL",
                 "Joshi": "LTC",
                 "Zareen": "CPT",
                 "Dr. V": "LTC"
                 }

for prof in faculty_ranks:
    print(prof, "has rank:", faculty_ranks[prof])

# keys must be unique
faculty_ranks["Lil' Banik"] = "CPT"
print(faculty_ranks["Lil' Banik"])

for prof in faculty_ranks:
    print(prof, "has rank:", faculty_ranks[prof])
