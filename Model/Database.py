class Database:
    def __init__(self):
        self.appointments = []
        self.bills = []
        self.departments = []
        self.doctors = []
        self.medical_records = []
        self.patients = []
        self.prescriptions = []
        self.prescription_items = []
        self.room_beds = []

        self.nxt_patient_id = 0
        self.nxt_doctor_id = 0
        self.nxt_appointment_id = 0
        self.nxt_prescription_id = 0
        self.nxt_medical_record_id = 0
        self.nxt_item_id = 0
        self.nxt_bill_id = 0
        self.nxt_room_id = 0
