from Controller.AdminController import AdminController
from Controller.DoctorController import DoctorController
from Controller.PatientController import PatientController


class MainController:
    def __init__(self, database):
        self.db = database
        self.patient_controller = PatientController(self.db)
        self.doctor_controller = DoctorController(self.db)
        self.admin_controller = AdminController(self.db)

    def start(self):
        while True:
            print("\n----Main Menu----")
            print("1.Register as a new patient")
            print("2.Login as a patient")
            print("3.Login as a Doctor")
            print("4.Login as an Admin")
            print("5.Exit")

            try:
                ch = int(input("Enter your choice:"))
                if ch == 1:
                    self.patient_controller.register()
                elif ch == 2:
                    self.patient_controller.login()
                elif ch == 3:
                    self.doctor_controller.login()
                elif ch == 4:
                    self.admin_controller.login()
                elif ch == 5:
                    print("Exiting....")
                    break
                else:
                    print("Enter the correct option")
            except ValueError:
                print("Enter a Valid number...")
