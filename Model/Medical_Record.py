class Medical_Record:
    def __init__(self, record_id, patient_id, doctor_id, consultation_details, diagnosis, record_date):
        self.record_id = record_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.consultation_details = consultation_details
        self.diagnosis = diagnosis
        self.record_date = record_date

    def get_medical_records(self):
        return f"{self.record_id}, {self.patient_id}, {self.doctor_id}, {self.consultation_details}, {self.diagnosis}, {self.record_date}"
