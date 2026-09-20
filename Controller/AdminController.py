from Controller.BillController import BillController
from Controller.DepartmentController import DepartmentController
from Controller.DoctorController import DoctorController


class AdminController:
    def __init__(self, database):
        self.db = database
        self.__adminID = "admin"
        self.__adminPassword = "admin"

    def login(self):
        print("\nAdmin Login...")
        name = input("Enter adminID: ")
        pwd = input("Enter Password: ")

        if name == self.__adminID and pwd == self.__adminPassword:
            print("Login Successfull")
            self.admin_console()
        else:
            print("Invalid Credentials")

    def admin_console(self):
        self.doctor_controller = DoctorController(self.db)
        self.dept_controller = DepartmentController(self.db)
        self.bill_controller = BillController(self.db)

        while True:
            print("\n---Admin Console---")
            print("1.Manage Doctors")
            print("2.Manage Departments")
            print("3.Generate Bill")
            print("4.Logout")

            try:
                ch = int(input("Enter your choice: "))
                if ch == 1:
                    self.doctor_controller.admin_manage_doctors()
                elif ch == 2:
                    self.dept_controller.admin_manage_dept()
                elif ch == 3:
                    self.bill_controller.admin_generate_bill()
                elif ch == 4:
                    print("Logging Out...")
                    break
                else:
                    print("Enter a Valid number")
            except ValueError:
                print("Enter a Valid number")
