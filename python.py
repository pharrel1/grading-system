# names = ["John", "Paul", "Goe", "john"]
# print(dir(names))
# new_names = ["vincent", "james",]
# names.append("Mary")
# names.append("True")
# names.extend(new_names)
# names.append(new_names)
# names.insert(2, "shegun")
# names.clear()
# del(names)
# another_names = names.copy()
# names = "john"
# count_result = names.count(names)
# print(count_result)
# names.pop()
# poped = names.pop(2)
# names.remove("goe")
# print(poped)
# print(names)
# print(another_names)


# NESTING
# #        bmw         audi     toyota          benz
# cars = [["M5", "M6"] "audi", "toyota", ["gle","amg"]]
# cars[0][1] =" m1"

cars = {"bmw":"m5","audi":"a1","benz":"gle","number":4,"status" : True}
print(cars["bmw"])
# cars["status"] = False
# our_keys = list(cars.keys())
our_values = list(cars.values())
print(our_values)
# print(len(cars))
# print(dir(cars))