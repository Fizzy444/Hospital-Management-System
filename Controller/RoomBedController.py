from Model.Room_Bed import Room_Bed
import datetime


class RoomBedController:
    def __init__(self, database):
        self.db = database

    def admin_create_bed(self):
        num = int(input("Enter number of beds to be created: "))
        for i in range(1, num + 1):
            self.db.nxt_room_id += 1
            room_bed = Room_Bed(self.db.nxt_room_id)
            self.db.room_beds.append(room_bed)
        print(f"Successfully created {num} beds")

    def admit_patient(self, pat_id):
        found = False

        for rb in self.db.room_beds:
            if rb.status == "Available":
                found = True
                rb.patient_id = pat_id
                rb.status = "Occupied"
                today = datetime.datetime.now(tz=datetime.UTC).date()
                date = today.strftime("%d-%m-%Y")
                rb.admission_date = date
                print("Assigned Bed to the Patient")
                break

        if not found:
            print("All beds are occupied")

    def discharge_patient(self, pat_id):
        found = False
        for rb in self.db.room_beds:
            if rb.patient_id == pat_id:
                found = True
                rb.patient_id = None
                today = datetime.datetime.now(tz=datetime.UTC).date()
                date = today.strftime("%d-%m-%Y")
                rb.discharge_date = date
                rb.status = "Available"

                print(f"Patient Discharged at {date}")
        if not found:
            print("Patient ID not found")
