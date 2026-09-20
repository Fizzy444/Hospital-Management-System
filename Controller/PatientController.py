from Model.Patient import Patient


class PatientController:
    def __init__(self, database):
        self.db = database
        self.nxt_patient_id = 0
        self.patient = None

    def register(self):
        try:
            self.nxt_patient_id += 1
            name = input("Enter name: ")
            age = int(input("Enter Age: "))
            if age < 1:
                print("Enter valid age...")

            contact_details = int(input("Enter Phone number: "))
            password = input("Enter password: ")

            self.patient = Patient(self.nxt_patient_id, name, age, contact_details, password)
            self.db.patients.append(self.patient)
            print("---Registered the patient successfully---")
            print(f"Your Patient_ID is {self.nxt_patient_id}")

        except ValueError:
            print("Enter a valid number")

    def login(self):
        print("\nPatient Login...")
        id = int(input("Enter Patient_ID: "))
        password = input("Enter Password: ")

        patient = None

        for p in self.db.patients:
            if p.patient_id == id:
                patient = p
                break

        if patient is None:
            print("Patient ID not found")
        elif patient.password != password:
            print("Incorrect Password")
        else:
            print("Login Successfull!!!")
            self.patient_dashboard(patient)

    def patient_dashboard(self, patient):
        while True:
            print(f"\n{patient.name}'s Dashboard")
            print("1.View My Profile")
            print("2.Logout")

            try:
                ch = int(input("Enter your choice: "))
                if ch == 1:
                    print(f"Patiend_ID: {patient.patient_id} | Name: {patient.name} | Age: {patient.age} | Contact_Details: {patient.contact_details}")
                elif ch == 2:
                    print("Logging Out...")
                    break
                else:
                    print("Enter a Valid number")
            except ValueError:
                print("Enter a Valid number")
