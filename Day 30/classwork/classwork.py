mentor_names = ["John", "Alice", "Bob", "Eve"]
regular_names = []

while True:
    name = input("Enter a name (type 'quit' to stop): ")

    if name.lower() == 'quit':
        break
    
    if name in mentor_names:
        print(f"{name} is a mentor, adding to mentor list.")
        mentor_names.append(name)
    else:
        print(f"{name} is a regular name, adding to regular list.")
        regular_names.append(name)

print("Mentors:", mentor_names)
print("Regular Names:", regular_names)
