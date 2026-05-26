patients = []
patient_id = 100

# Login Status
logged_in = False


# Add Patient Function
def add_patient():

    global patient_id

    patient_id += 1

    name = input("Enter Patient Name : ")

    try:
        age = int(input("Enter Patient Age : "))

    except:
        print("Invalid Age")
        return

    disease = input("Enter Disease : ")

    patient = {
        "ID": patient_id,
        "Name": name,
        "Age": age,
        "Disease": disease
    }

    patients.append(patient)

    # File Handling
    with open("patients.txt", "a") as file:

        file.write(f"""
ID : {patient["ID"]}
Name : {patient["Name"]}
Age : {patient["Age"]}
Disease : {patient["Disease"]}
-----------------------
""")

    print(f"Patient Added Successfully. Patient ID is {patient_id}")


# View Patient Function
def view_patient():

    if len(patients) == 0:

        print("No Patient Record Found")

    else:

        print("\n===== Patient Records =====")

        for patient in patients:

            print("\nID :", patient["ID"])
            print("Name :", patient["Name"])
            print("Age :", patient["Age"])
            print("Disease :", patient["Disease"])


# Search Patient Function
def search_patient():

    try:
        search_id = int(input("Enter Patient ID : "))

    except:
        print("Invalid ID")
        return

    found = False

    for patient in patients:

        if patient["ID"] == search_id:

            print("\n===== Patient Found =====")

            print("ID :", patient["ID"])
            print("Name :", patient["Name"])
            print("Age :", patient["Age"])
            print("Disease :", patient["Disease"])

            found = True
            break

    if found == False:

        print("Patient Not Found")


# Delete Patient Function
def delete_patient():

    try:
        delete_id = int(input("Enter Patient ID to Delete : "))

    except:
        print("Invalid ID")
        return

    found = False

    for patient in patients:

        if patient["ID"] == delete_id:

            patients.remove(patient)

            print("Patient Deleted Successfully")

            found = True
            break

    if found == False:

        print("Patient Not Found")


# Update Patient Function
def update_patient():

    try:
        update_id = int(input("Enter Patient ID to Update : "))

    except:
        print("Invalid ID")
        return

    found = False

    for patient in patients:

        if patient["ID"] == update_id:

            print("\n===== Current Details =====")

            print("Name :", patient["Name"])
            print("Age :", patient["Age"])
            print("Disease :", patient["Disease"])

            print("\n===== Enter New Details =====")

            patient["Name"] = input("Enter New Name : ")

            try:
                patient["Age"] = int(input("Enter New Age : "))

            except:
                print("Invalid Age")
                return

            patient["Disease"] = input("Enter New Disease : ")

            print("Patient Updated Successfully")

            found = True
            break

    if found == False:

        print("Patient Not Found")


# Read File Function
def read_file():

    try:

        with open("patients.txt", "r") as file:

            data = file.read()

            print(data)

    except:

        print("File Not Found")


# Login System
import time

attempts = 0

while attempts < 3:

    user_id = input("Enter User ID : ")

    try:
        password = int(input("Enter Password : "))

    except:
        print("Invalid Password")
        continue

    if user_id == "baiju" and password == 123:

        print("\nLogin Successful")

        logged_in = True

        break

    else:

        attempts += 1

        print(f"Wrong Credentials. Attempts Left: {3 - attempts}")


# Block System
if attempts == 3:

    print("Too Many Wrong Attempts")
    print("System Blocked For 5 Minutes")

    # For Testing Use 10 Seconds
    time.sleep(10)

    # Final Version
    # time.sleep(300)

    exit()


# Main Menu
if logged_in:

    while True:

        print("\n===== Hospital Management System =====")

        print("1. Add Patient")
        print("2. View Patient")
        print("3. Staff Details")
        print("4. Exit")
        print("5. Search Patient")
        print("6. Delete Patient")
        print("7. View Saved File Data")
        print("8. Update Patient")

        try:
            choice = int(input("Enter Your Choice : "))

        except:
            print("Invalid Choice")
            continue

        # Add Patient
        if choice == 1:

            add_patient()

        # View Patient
        elif choice == 2:

            view_patient()

        # Staff Details
        elif choice == 3:

            print("\n===== Staff Details =====")

            print("Doctor : Dr. Baij Nath Srivastava")
            print("Nurse : Vaishnavi")
            print("Ward Boy : Dipanshu")

        # Exit
        elif choice == 4:

            print("System Closed")

            break

        # Search Patient
        elif choice == 5:

            search_patient()

        # Delete Patient
        elif choice == 6:

            delete_patient()

        # View Saved File Data
        elif choice == 7:

            read_file()

        # Update Patient
        elif choice == 8:

            update_patient()

        else:

            print("Invalid Choice")