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
        doctor_menu()

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
    d["Disease"]=input("Enter patient disease:")
    patients.append(d)

def view_patient():
    if not patients:
        print("No patient found")
        return
    for t in patients:
        print(t)

def search_patient():
    id=int(input("Enter id:"))
    for t in patients:
        if t["Id"]==id:
            print("Patient found")
            print(t)
            return
    print("Patient not found")

def update_patient():
    id=int(input("Enter patient Id:"))

    for t in patients:
        if t["Id"]==id:

            print("\nWhat do you want to update?")
            print("1. Name")
            print("2. Age")
            print("3. Gender")
            print("4. Contact")
            print("5. Disease")

            chc=int(input("Enter choice:"))

            if chc==1:
                t["Name"]=input("Enter name:")
            elif chc==2:
                t["Age"]=int(input("Enter age:"))
            elif chc==3:
                t["Gender"]=input("Enter gender:")
            elif chc==4:
                t["Contact"]=input("Enter phone number:")
            elif chc==5:
                t["Disease"]=input("Enter disease:")
            else:
                print("Invalid entry")
                return

            print("Patient updated successfully")
            return

    print("Patient not found")

def delete_patient():
    id=int(input("Enter patient Id:"))

    for t in patients:
        if t["Id"]==id:
            patients.remove(t)
            print("Patient deleted successfully")
            return

    print("Patient not found")
    
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
            view_patient()
        elif ch==3:
            search_patient()
        elif ch==4:
            update_patient()
        elif ch==5:
            delete_patient()
        elif ch==6:
            print("Back to Menu")
            break
        else:
            print("Invalid Choice")


doctors=[]
def add_doctor():
    d1={}
    d1["Id"]=int(input("Enter doctor Id:"))
    
    for d in doctors:
        if d["Id"]==d1["Id"]:
            print("Doctor ID already exists")
            return
            
    d1["Name"]=input("Enter doctor name:")
    d1["Age"]=int(input("Enter doctor age:"))
    d1["Gender"]=input("Enter doctor Gender:")
    d1["Contact"]=input("Enter doctor phone number:")
    d1["Department"]=input("Enter doctor department:")

    doctors.append(d1)

def view_doctor():
    if not doctors:
        print("No doctor found")
        return
    for t in doctors:
        print(t)

def search_doctor():
    id=int(input("Enter id:"))
    for t in doctors:
        if t["Id"]==id:
            print("Doctor found")
            print(t)
            return
    print("Doctor not found")

def update_doctor():
    id=int(input("Enter doctor Id:"))

    for t in doctors:
        if t["Id"]==id:

            print("\nWhat do you want to update?")
            print("1. Name")
            print("2. Age")
            print("3. Gender")
            print("4. Contact")
            print("5. Department")

            chc=int(input("Enter choice:"))

            if chc==1:
                t["Name"]=input("Enter name:")
            elif chc==2:
                t["Age"]=int(input("Enter age:"))
            elif chc==3:
                t["Gender"]=input("Enter gender:")
            elif chc==4:
                t["Contact"]=input("Enter phone number:")
            elif chc==5:
                t["Department"]=input("Enter department:")
            else:
                print("Invalid entry")
                return

            print("Doctor updated successfully")
            return

    print("Doctor not found.")

def delete_doctor():
    id=int(input("Enter doctor Id:"))

    for t in doctors:
        if t["Id"]==id:
            doctors.remove(t)
            print("Doctor deleted successfully!")
            return

    print("Doctor not found")

def doctor_menu():
    while True:
        if choice==1:
            add_doctor()
        elif choice==2:
            view_doctor()
        elif choice==3:
            search_doctor()
        elif choice==4:
            update_doctor()
        elif choice==5:
            delete_doctor()
        elif choice==6:
            break
        else:
            print("Invalid choice")
            
