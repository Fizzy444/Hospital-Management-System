class Room_Bed:
    def __init__(self, admission_id, patient_id, room_id, bed_id, admission_date, discharge_date):
        self.bed_id = bed_id
        self.status = "Available"
        self.patient_id = None
        self.admission_date = None
        self.discharge_date = None
