from Controller.MedicalRecordController import MedicalRecordController
from Controller.RoomBedController import RoomBedController
from Model.Doctor import Doctor


class DoctorController:
    def __init__(self, database):
        self.db = database
        self.doc = None

    def login(self):
        print("\nDoctor Login...")
        docID = int(input("Enter DoctorID: "))
        pwd = input("Enter Password: ")

        doc = None

        for d in self.db.doctors:
            if d.doctor_id == docID:
                doc = d
                break
        if doc is None:
            print("Invalid DoctorID")
        elif doc.password != pwd:
            print("Invalid Credentials")
        else:
            print("Login Successfull")
            self.doctor_dashboard(doc)

    def doctor_dashboard(self, doc):
        self.med_rec = MedicalRecordController(self.db)
        self.room_bed = RoomBedController(self.db)
        while True:
            print(f"\n---{doc.doctor_name}'s Dashboard---")
            print("1.View My Appointments")
            print("2.Add Medical Records for a Patient")
            print("3.Write a Prescription")
            print("4.View Medical History of a Patient")
            print("5.Admit a Patient")
            print("6.Discharge a Patient")
            print("7.Log Out")

            try:
                ch = int(input("Enter your choice: "))
                if ch == 1:
                    self.view_appointments(doc)
                elif ch == 2:
                    self.med_rec.add_medical_record(doc)
                elif ch == 3:
                    self.med_rec.write_prescription(doc)
                elif ch == 4:
                    self.med_rec.view_medical_history()
                elif ch == 5:
                    pat_id = int(input("Enter Patient ID to be admitted:"))
                    self.room_bed.admit_patient(pat_id)
                elif ch == 6:
                    pat_id = int(input("Enter Patient ID to be Discharged:"))
                    self.room_bed.discharge_patient(pat_id)
                elif ch == 7:
                    print("Logging Out...")
                    break
                else:
                    print("Enter a Valid number")
            except ValueError:
                print("Enter a Valid number")

    def view_appointments(self, doc):
        found = False
        for apt in self.db.appointments:
            if apt.doctor_id == doc.doctor_id:
                print(f"{apt.appointment_id} | {apt.patient_id} | {apt.doctor_id} | {apt.appointment_date} | {apt.appointment_time} | {apt.status}")
                found = True
        if not found:
            print("No Appointments available")

    def admin_manage_doctors(self):
        while True:
            print("\n1.Add Doctor")
            print("2.Edit Doctor Details")
            print("3.Remove Doctor")
            print("4.View Doctor")
            print("5.Return Main Menu")

            try:
                ch = int(input("Enter your choice: "))
                if ch == 1:
                    self.admin_add_doctor()
                elif ch == 2:
                    self.admin_edit_doctor()
                elif ch == 3:
                    self.admin_remove_doctor()
                elif ch == 4:
                    self.admin_view_doctors()
                elif ch == 5:
                    print("Returning to Main Menu...")
                    break
                else:
                    print("Enter a Valid number")

            except ValueError:
                print("Enter a Valid number")

    def admin_add_doctor(self):
        name = input("Enter name: ")
        dept_id = int(input("Enter department_id: "))
        specialization = input("Enter Specialization: ").lower()
        available = True
        password = input("Enter Password: ")
        self.db.nxt_doctor_id += 1
        self.doc = Doctor(self.db.nxt_doctor_id, name, dept_id, specialization, available, password)
        self.db.doctors.append(self.doc)
        print("Added Doctor Successfully...")

    def admin_edit_doctor(self):
        id = int(input("Enter DoctorID to edit: "))
        doc = None

        for d in self.db.doctors:
            if d.doctor_id == id:
                doc = d
                break

        if doc is None:
            print("DoctorID not found")
            return

        print(f"{doc.doctor_id} | {doc.doctor_name} | {doc.department_id} | {doc.specialization} | {doc.availability}")
        while True:
            print("1.Update Availability")
            print("2.Update DepartmentID")
            print("3.Update password")
            print("4.Go Back")

            try:
                ch = int(input("Which data would you like to change"))
                if ch == 1:
                    doc.availability = not doc.availability
                elif ch == 2:
                    d_id = int(input("Enter new dept_id: "))
                    doc.department_id = d_id
                elif ch == 3:
                    new_pwd = input("Enter new password: ")
                    doc.password = new_pwd
                elif ch == 4:
                    print("Going Back...")
                    break
                else:
                    print("Enter a Valid number")
            except ValueError:
                print("Enter a Valid Number")

    def admin_remove_doctor(self):
        id = int(input("Enter DoctorID to be removed: "))
        for d in self.db.doctors:
            if d.doctor_id == id:
                print(f"Found Doctor {d.doctor_id} - {d.doctor_name} | Are you sure you wanna remove Y/N?: ", end = "")
                ch = input()
                if ch.upper() == "Y":
                    self.db.doctors.remove(d)
                    print("Successfully Removed")
                    print("Returning to Main Menu")
                elif ch.upper() == "N":
                    print("Returning to Main Menu")
                else:
                    print("Enter only the valid input")
                break


    def admin_view_doctors(self):
        for d in self.db.doctors:
            print(f"{d.doctor_id} | {d.doctor_name} | {d.department_id} | {d.specialization} | {d.availability}")
