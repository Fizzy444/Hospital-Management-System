class Appointment:
    def __init__(self, appointment_id, patient_id, doctor_id, appointment_date, appointment_time, status):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time
        self.status = status

    def get_appointment_details(self):
        return f"{self.appointment_id}, {self.patient_id}, {self.doctor_id}, {self.appointment_date}, {self.appointment_time}, {self.status}"
