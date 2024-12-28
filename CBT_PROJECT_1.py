print("Welcome to Contact Manager!")
print("How can I help you with?")
print("Choose the following:")
print("\t 1. Add contacts")
print("\t 2. Delete contacts")
print("\t 3. Search contacts")
print("\t 4. Display contacts")
print("\t 5. Quit")
      
contacts = {}
while True:
    choice = input("How can we assist you?").lower()
    if choice in "add contact":
        def add_contact():
            name = input("Enter the Name:").lower()
            mob = int(input("Enter Mobile Number:"))
            if name in contacts:
                print("Contact already exists")      
            else:
                contacts[name] = {"phone num" : mob}
                print("Contact Added!")
        add_contact()
    
    elif choice in "delete contact":
        def delete_contact():
            name = input("Enter the Name:").lower()
            if name in contacts:
                del contacts[name]
                print("Contact Deleted!")
            else:
                print("Contact does not exist!")
        delete_contact()

    elif choice in "search contact":
        def search_contact():
            name = input("Enter the Name:").lower()
            if name in contacts:
                name_prop = name.capitalize()
                print("The Contact you searched for:")
                print(f"\t Name is {name_prop}")
                print(f"\t Mobile number is {contacts[name]['phone num']}")
            else:
                print("Contact not found.")
        search_contact()

    elif choice in "display contact":
        def display_contact():
            print("The Contacts in the Contact Manager are:")
            for name, mob in contacts.items():
                name_prop = name.capitalize()
                print(f"\t Name : {name_prop}")
                print(f"\t Mobile number : {contacts[name]['phone num']}")
        display_contact()

    elif choice in "quit":
        print("Thank You! Visit again")
        break
        
    else:
        print("Invalid input!")
        break