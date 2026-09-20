from Controller.MainController import MainController
from Model.Database import Database


def main():
    print("Starting Hospital Management System")
    hospital_db = Database()
    app = MainController(hospital_db)
    app.start()

if __name__ == "__main__":
    main()
