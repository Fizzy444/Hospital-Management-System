from calendar import c

from Model.Doctor import Doctor


class DoctorController:
    def __init__(self, database):
        self.db = database

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
        pass

    def admin_manage_doctors(self):
        while True:
            print("1.Add Doctor")
            print("2.Edit Doctor Details")
            print("3.Remove Doctor")
            print("4.Return Main Menu")

            try:
                ch = int(input("Enter your choice: "))
                if ch == 1:
                    self.admin_add_doctor()
                elif ch == 2:
                    self.admin_edit_doctor()
                elif ch == 3:
                    self.admin_remove_doctor()
                elif ch == 4:
                    print("Returning to Main Menu...")
                else:
                    print("Enter a Valid number")

            except ValueError:
                print("Enter a Valid number")

    def admin_add_doctor(self):
        pass

    def admin_edit_doctor(self):
        pass

    def admin_remove_doctor(self):
        pass
