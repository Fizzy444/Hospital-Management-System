from Controller.AppointmentController import AppointmentController
from Model.Patient import Patient


class PatientController:
    def __init__(self, database):
        self.db = database

    def register(self):
        try:
            self.db.nxt_patient_id += 1
            name = input("Enter name: ")
            age = int(input("Enter Age: "))
            if age < 1:
                print("Enter valid age...")

            contact_details = int(input("Enter Phone number: "))
            password = input("Enter password: ")

            self.patient = Patient(self.db.nxt_patient_id, name, age, contact_details, password)
            self.db.patients.append(self.patient)
            print("---Registered the patient successfully---")
            print(f"Your Patient_ID is {self.db.nxt_patient_id}")

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
        apt_controller = AppointmentController(self.db, patient)
        while True:
            print(f"\n{patient.name}'s Dashboard")
            print("1.View My Profile")
            print("2.Book an Appointment")
            print("3.View my Appointments")
            print("4.Cancel Appointments")
            print("5.View my Prescriptions")
            print("6.Logout")

            try:
                ch = int(input("Enter your choice: "))
                if ch == 1:
                    print(f"Patiend_ID: {patient.patient_id} | Name: {patient.name} | Age: {patient.age} | Contact_Details: {patient.contact_details}")
                elif ch == 2:
                    apt_controller.book_an_appointment()
                elif ch == 3:
                    apt_controller.view_my_appointment()
                elif ch == 4:
                    apt_controller.cancel_appointment()
                elif ch == 5:
                    self.view_prescription(patient)
                elif ch == 6:
                    print("Logging Out...")
                    break
                else:
                    print("Enter a Valid number")
            except ValueError:
                print("Enter a Valid number")

    def view_prescription(self, patient):
        found = False

        for pres in self.db.prescriptions:
            if pres.patiend_id == patient.patient_id:
                found = True
                print(f"\nDate: {pres.prescription_date} | Prescribed by {pres.doctor_id}")
                print("Medicines:")

                for item in self.db.prescription_items:
                    if item.prescription_id == pres.prescription_id:
                        print(f"Medicine Name: {item.medicine_name} | Dosage: {item.dosage} | Duration: {item.duration}")
                        print(f"Instructions: {item.instructions}")

        if not found:
            print("You have no Prescriptions")
