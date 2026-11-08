

first_room = input("Название 1й аудитории: ")
second_room = input("Название 2й аудитории: ")

print(f"До обмена:    first_room = {first_room}, second_room = {second_room}")

temp = first_room
first_room = second_room
second_room = temp

print(f"После обмена: first_room = {first_room}, second_room = {second_room}")