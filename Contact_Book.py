# Contact Book

contacts = {}

def add_contact():
    print("Contact Add Window!")
    
    name = input("Enter the name of the contact: ")
    
    if name in contacts:
        print("Contact with same Name Exist, Update it Instead.")
        return
    
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    address = input("Enter the address: ")

    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    
    print("Well Done! The contact of " + name + " has been added in your list.")

def view_contacts():
    if contacts:
        print("Here's Your All Contacts:")
        for name, details in contacts.items():
            print("Name: " + name + ", Phone Number: " + details['phone'])
    else:
        print("Your contact list is Empty, Add some First!")

def search_contact():
    print("Contact Search Window!")
    
    search_term = input("Enter the Name or Phone Number you want to search for: ")
    
    found = False
    
    for name, details in contacts.items():
        if search_term == name or search_term == details['phone']:
            print("Contact Found..!")
            print("Name: " + name)
            print("Phone Number: " + details['phone'])
            print("Email Address: " + details['email'])
            print("Address: " + details['address'])
            found = True
            break

    if not found:
        print("Contact not Found!")

def update_contact():
    print("Contact Update Window!")
    
    name = input("Enter the Name of the Contact you want to update: ")
    
    if name in contacts:
        print("You are about to Update contact for " + name + ". If you don't want to change, simply press Enter without typing anything.")
        
        new_phone = input("Enter the new Phone number: ")
        new_email = input("Enter the new Email address: ")
        new_address = input("Enter the new Address: ")

        if new_phone:
            contacts[name]['phone'] = new_phone
        if new_email:
            contacts[name]['email'] = new_email
        if new_address:
            contacts[name]['address'] = new_address
            
        print("The details for " + name + " have been successfully updated.")
    else:
        print("No contact with the name " + name + " present. Please verify the name and try again.")

def delete_contact():
    print("Contact Deleting Window!")
    
    name = input("Enter the name of the Contact you want to delete: ")
    
    if name in contacts:
        del contacts[name]
        print("The contact for " + name + " has successfully deleted.")
    else:
        print("Contact not found in List. Please verify the Name and try again.")

def main_menu():
    while True:
        print("Welcome to your Contact Book! What would you like to do today?")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Search for a Contact")
        print("4. Update an Existing Contact")
        print("5. Delete Contact")
        print("6. Exit the Contact Book")

        choice = input("Enter the number to your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Thank you for using the Contact Book. Have a Nice day Ahead..!")
            break
        else:
            print("That's invalid Option, Try to put between 1-6 options only.")

if __name__ == "__main__":
    main_menu()
