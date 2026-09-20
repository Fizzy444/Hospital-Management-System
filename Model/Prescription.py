class Prescription:
    def __init__(self, prescription_id, record_id, patient_id, doctor_id, prescription_date):
        self.prescription_id = prescription_id
        self.record_id = record_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.prescription_date = prescription_date
