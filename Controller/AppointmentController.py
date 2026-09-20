from typing_extensions import ParamSpecKwargs

from Model.Appointment import Appointment


class AppointmentController:
    def __init__(self, databse, curr_patient):
        self.db = databse
        self.patient = curr_patient
        self.nxt_appointment_id = 0

    def book_an_appointment(self):
        spec = input("Enter Doctor Specialization you need (eg.Cardio): ").lower()
        found = False
        for d in self.db.doctors:
            if d.specialization == spec:
                print(f"{d.doctor_id} | {d.doctor_name}")
                found = True

        if not found:
            print("Sorry no available doctors in that specialization")
            return

        doc_id = int(input("Enter DoctorID you want to book: "))
        date = input("Enter date you wanna book (DD-MM-YYYY): ")
        time = input("Enter time you wanna book (MM:HH): ")

        self.nxt_appointment_id += 1
        new_apt = Appointment(self.nxt_appointment_id, self.patient.patient_id, doc_id, date, time, "Booked")
        self.db.appointments.append(new_apt)
        print(f"Successfully Booked Appointment ID:{new_apt.appointment_id} for {date} at {time}")

    def view_my_appointment(self):
        pass
