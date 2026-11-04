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
        patient_menu()  

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
        print("Invalid Choice")

main_menu()

patients=[]
def add_patient():
    d={}
    d["Id"]= int(input("Enter patient Id:"))
    for p in patients:
        if p["Id"]==d["Id"]:
            print("Patient ID already exists!")
            return
    d["Name"]=input("Enter patient name:")
    d["Age"]=int(input("Enter patient age:"))
    d["Gender"]=input("Enter patient Gender:")
    d["Contact"]=int(input("Enter patient phone number:"))
    d["Disease"]=input("Entee patient disease:")
    patients.append(d)
    
def patient_menu():
    while True:
        print("PATIENT MANAGEMENT\n")
        print("1. Add Patient\n")
        print("2. View all Patients\n")
        print("3. Search Patient\n")
        print("4. Update Patient\n")
        print("5. Delete Patient\n")
        print("6. Back to Main Menu\n")
        ch=int(input(" Enter your choice:"))
        if ch==1:
            add_patient()
        elif ch==2:
            print("View all Patients")
        elif ch==3:
            print("Search Patient ")
        elif ch==4:
            print("Update Patient")
        elif ch==5:
            print("Delete Patient")
        elif ch==6:
            print(" Back to Menu")
            break
        else:
            print("Invalid Choice")
            
