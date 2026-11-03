def main_menu():
print("HOSPITAL MANAGEMENT SYSTEM")

while True:  
    print("1. Patient Management")  
    print("2. Doctor Management")  
    print("3. Appointment Management")  
    print("4. Billing Management")  
    print("5. Medicine Inventory")  
    print("6. Hospital Reports")  
    print("7. Exit")  

    choice=int(input("Enter your choice:"))  

    if choice==1:  
        print("Patient Management selected")  

    elif choice==2:  
        print("Doctor Management selected")  

    elif choice==3:  
        print("Appointment Management selected")  

    elif choice==4:  
        print(" Billing Management selected")  

    elif choice==5:  
        print("Medicine Inventory selected")  

    elif choice==6:  
        print("Hospital Reports selected")  

    elif choice==7:  
        print("Thank You for visiting")  
        break  

    else:  
        print("Invalid Choice')

main_menu()
