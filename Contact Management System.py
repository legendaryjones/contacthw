

print ( '''
       
       Welcome to the Contact Management System! 
Menu:
Add a new contact
Edit an existing contact
Delete a contact
Search for a contact
Display all contacts
Export contacts to a text file
Import contacts from a text file
Quit 

'''
)

# Display welcome message
contact = {

'Ginger Bread': {'Address': 'Drury Lane', 'Email': 'gingerb@mail.com', 'Phone': '123456'},
'Santa Clause': {'Address': 'North Pole', 'Email': 'santababy@mail.com', 'Phone': '123456'},
'CT padawan': {'Address': 'Coding Illinois', 'Email': 'codingt@mail.com', 'Phone': '123456'},
'mike jones': {'Address': 'Atlanta', 'Email': 'mikejones@mail.com', 'Phone': '2813308004'},
'jack jones':{'Address': 'Atlanta', 'Email': 'jackjones@mail.com', 'Phone': '2813308004'},
}

def __init__(self, contact,):
     self.contact
 
     
     
##### add contact
def add_contact(contact): 
     with open('contact.txt', 'w') as file: 
        for name,info in contact.items(): 
            file.write(f"{name}--{info['Address']}--{info['Email']}--{info['Phone']}\n")  

######read contact
def read_contact():
     contact = {}
with open('contact.txt', 'r') as file:
        for line in file:
            email = line.strip().split('--')
            #print (email)

def edit_contact():
    email = input("Enter the email address of the contact to edit: ")
    if email in contact:
        print("Editing contact with email:", email)
        name = input("Enter new name (leave blank to keep existing): ")
        if name:
            contact[email]['Name'] = name
        phone_number = input("Enter new phone number (leave blank to keep existing): ")
        if phone_number:
            contact[email]['Phone Number'] = phone_number
        additional_info = input("Enter new additional information (leave blank to keep existing): ")
        if additional_info:
            contact[email]['Additional Info'] = additional_info
        print("Contact edited successfully!")
    else:
        print("Contact not found!")

# def menu():
#     while True:
#         menu()
#         choice = input("Enter your choice: ")
#         if choice == 'add':
#             add_contact()
#         elif choice == 'edit':
#             edit_contact()
#         elif choice == 'delete':
#             delete_contact()
#         elif choice == 'search':
#             search_contact()
#         elif choice == 'display':
#             read_contact()
#         elif choice == 'export':
#             export_contacts()
#         elif choice == 'import':
#             import_contacts()
#         elif choice == 'quit':
#             print("Thank you for using the Contact Management System!")
#             break
#         else:
#             print("Invalid choice! Please try again.")
# # 
        
add_contact (contact)