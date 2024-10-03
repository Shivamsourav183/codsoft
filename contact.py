contacts = {}

def menu():
    print("\n--------------MENU--------------")
    print("press 4 if you want to terminate program.")
    print("press 0 to view contact.")
    print("press 1 to add a person to the contacts book.")
    print("press 2 to update an existing contacts.")
    print("press 3 to delete an existing contacts.")
    print("press 5 to print all contacts.")
    print("press any number from 6-9 to display menu")
    print("---------------------------------------")
    print("      CONTACT BOOK      ")

def display():
    if contacts:
        print("\n---Contact List---")
        for name,details in contacts.items():
            print(f"{name}: Phone: {details['phone']}, Email:{details['email']},Address: {details['address']}")
    else:
        print("No contacts found.")
        
menu()
           
while True:
    choice=int(input("Enter command:"))
            
    if choice==0:
        look=input("Name of the person:").upper()
        if look in contacts:
            details=contacts[look]
            print(f"\nContact Details for {look}:")
            print(f"phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
        else:
          print("contact not found.")
          
    elif choice==1:
        Name=input("Enter Name:").upper()
        phone=input("Enter Phone number: ")
        email=input("Enter email address: ")
        address=input("Enter home address: ")
        contacts[Name]= {"phone":phone,"email": email,"address":address}
        print(f"Contact {Name} added successfully.")
        display()
        
                
    elif choice==2:
           Name=input("Enter the name of the contact to update: ").upper()
           if Name in contacts:
               phone=input("Enter new phone number: ")
               email=input("Enter new email address: ")
               address=input("Enter new home address: ")
               contacts[Name]= {"phone":phone,"email": email,"address":address}
               print(f"Contact {Name} added successfully.")
               display()
        
           else:
                print("Number is invalid.Please try again.")
                
    elif choice==3:
        Number=input("Enter the name of the contact to delete:").upper()
          
        if Name in contacts:  
            del contacts[Name]
            print(f"Contact {Name} deleted successfully.")   
            display()
        else:
                    print("Contact not found.")                 
    elif choice==4:
             print("Thank you for using the Contact book! Goodbye!")
             break
            
    elif choice==5:
           
            display()
        
    else:
            menu()