class Prescription_Item:
    def __init__(self, item_id, prescription_id, medicine_name, dosage, duration, instructions):
        self.item_id = item_id
        self.prescription_id = prescription_id
        self.medicine_name = medicine_name
        self.dosage = dosage
        self.duration = duration
        self.instructions = instructions
