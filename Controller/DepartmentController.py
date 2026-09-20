from Model.Department import Department


class DepartmentController:
    def __init__(self, database):
        self.db = database
        self.nxt_deptID = 0
        self.dept = None

    def admin_manage_dept(self):
        while True:
            print("1.Add Department")
            print("2.Remove Department")
            print("3.View Department")
            print("4.Return Menu")

            try:
                ch = int(input("Enter your choice: "))
                if ch == 1:
                    self.admin_add_dept()
                elif ch == 2:
                    self.admin_remove_dept()
                elif ch == 3:
                    self.admin_view_dept()
                elif ch == 4:
                    print("Returning to Main Menu...")
                    break
                else:
                    print("Enter a Valid number")
            except ValueError:
                print("Enter a Valid number")

    def admin_add_dept(self):
        name = input("Enter Department Name: ")
        self.nxt_deptID += 1
        self.dept = Department(self.nxt_deptID, name)
        self.db.departments.append(self.dept)
        print("Added Department Successfully")

    def admin_remove_dept(self):
        id = int(input("Enter DepartmentID: "))
        for d in self.db.departments:
            if d.department_id == id:
                print(f"Found department {d.department_id} - {d.department_name} | Are you sure you wanna remove Y/N: ", end = '')
                choice = input()
                if choice.upper() == "N":
                    print("Exiting...")
                else:
                    self.db.departments.remove(d)
                    print("Removed Department Successfully")
                break
    def admin_view_dept(self):
        for d in self.db.departments:
            print(f"{d.department_id} - {d.department_name}")
