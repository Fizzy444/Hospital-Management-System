class Room_Bed:
    def __init__(self, bed_id):
        self.bed_id = bed_id
        self.status = "Available"
        self.patient_id = None
        self.admission_date = None
        self.discharge_date = None
