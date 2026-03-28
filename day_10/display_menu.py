def display_menu():
    return "Contact Book Menu:\n1. Add Contact\n2. View Contact\n3. Edit Contact\n4. Delete Contact\n5. List All Contacts\n6. Exit"

call1 = display_menu()
print(call1)

def add_contact(contact_book):
    name = input()
    phone = input()
    email = input()
    address = input()
    if name in contact_book:
        print("Contact already exists!")
    else:
        contact_book[name] = {
            "phone": phone,
	        "email": email,
	        "address": address
        }
        print("Contact added successfully!")

#contact_book = {}
#add_contact(contact_book)
#print(contact_book)
#contact_book = {"Alice": {"phone": "123-456-7890", "email": "alice@example.com", "address": "123 Main St"}}
contact_book = {
    "Alice": {"phone": "123-456-7890", "email": "alice@example.com", "address": "123 Main St"},
    "Bob": {"phone": "234-567-8901", "email": "bob@example.com", "address": "456 Oak Ave"}
}
def view_contact(contact_book):
    contact_name = input()
    if contact_name in contact_book:
        print(f"Name: {contact_name}")
        for key, value in contact_book[contact_name].items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("Contact not found!")
#view_contact(contact_book)  

def edit_contact(contact_book):
    name = input()
    
    if name in contact_book:
        current_contact = contact_book[name]
        updated_phone = input()
        if updated_phone != '':
            current_contact['phone'] = updated_phone
        
        updated_email = input()
        if updated_email != '':
            current_contact['email'] = updated_email
        
        updated_address = input()
        if updated_address != '':
            current_contact['address'] = updated_address
        
        print("Contact updated successfully!")

    else:
        print("Contact not found!")


#call3=edit_contact(contact_book)
#print(call3)
#print(contact_book)

def delete_contact(contact_book):
    name = input() 
    if name in contact_book:
        contact_book.pop(name)
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

#call4=delete_contact(contact_book)
#print(call4)
#print(contact_book)

def list_all_contacts(contact_book):
    if contact_book == {}:
        print("No contacts available.")
    else:
        for contact in contact_book:
            print(f"Name: {contact}")
            for key, value in contact_book[contact].items():
                print(f"{key.capitalize()}: {value}")
            print()
call5 = list_all_contacts(contact_book)
print(call5)


contact_book = {}
while True:
    display_menu()
    choice = int(input())
    if choice == 1:
        add_contact(contact_book)   
    elif choice == 2:
        view_contact(contact_book)
    elif choice == 3:
        edit_contact(contact_book)
    elif choice == 4:
        delete_contact(contact_book)
    elif choice == 5:
        list_all_contacts(contact_book)
    elif choice == 6:
        break
    else:
        print("Invalid choice. Please try again.")

