


dr_banik =  {"name": "Banik", "rank": "COL", "area": "LEADERSHIP"}
dr_joshi =  {"name": "Joshi", "rank": "LTC", "area": "AI"}
dr_zareen = {"name": "Zareen", "rank": "CPT", "area": "AI"}
dr_v =      {"name": "Dr. V", "rank": "LTC", "area": None}

# list of dictionaries
# common keyset
faculty = [dr_banik, dr_joshi, dr_zareen, dr_v]

for prof in faculty:
    print(prof["name"], prof["rank"], prof["area"])



# make a dictionary of animals
# key: animal type
# value: your favorite animal of that type
# print it all out with a loop

animals = {"dog": "Dr. V's golden retriever, Jack.",
           "pig": "Porky"
           }
animals["cat"] = None
animals["horse"] = "Seabiscuit"

for cute_animal in animals:
    print(animals[cute_animal], "is the best", cute_animal, "in the whole world.")


