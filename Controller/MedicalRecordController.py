from Model.Medical_Record import Medical_Record
from Model.Prescription import Prescription
from Model.Prescription_Item import Prescription_Item


class MedicalRecordController:
    def __init__(self, database, doc):
        self.db = database
        self.doc = doc

    def add_medical_record(self, doc):
        pat_id = int(input("Enter PatientID: "))
        consult = input("Enter Consultation Details: ")
        diagnosis = input("Enter Diagnosis Details: ")

        import datetime

        day = datetime.datetime.now(tz=datetime.UTC).date()
        today = day.strftime("%d-%m-%Y")

        self.db.nxt_medical_record_id += 1
        med_rec = Medical_Record(self.db.nxt_medical_record_id, pat_id, doc.doctor_id, consult, diagnosis, today)
        self.db.medical_records.append(med_rec)
        print("Successfully Added Medical Record")

    def write_prescription(self, doc):
        pat_id = int(input("Enter PatientID: "))
        med_rec = None
        for mr in self.db.medical_records[::-1]:
            if mr.patient_id == pat_id:
                med_rec = mr
                break

        if med_rec is None:
            print("No Records Available for this Patient, to add Prescription create a medical record")
            return

        import datetime

        day = datetime.datetime.now(tz=datetime.UTC).date()
        today = day.strftime("%d-%m-%Y")

        self.db.nxt_prescription_id += 1
        pres = Prescription(self.db.nxt_prescription_id, med_rec.record_id, pat_id, doc.doctor_id, today)
        self.db.prescriptions.append(pres)
        print("Successfully Created Prescription")

        while True:
            med_name = input("Enter Medicine name: ")
            dosage = input("Enter Dosage: ")
            duration = input("Enter Duration: ")
            instruct = input("Enter Instructions: ")

            self.db.nxt_item_id += 1
            pres_item = Prescription_Item(self.db.nxt_item_id, self.db.nxt_prescription_id, med_name, dosage, duration, instruct)
            self.db.prescription_items.append(pres_item)
            print("Successfully Added Prescription Item")
            ch = input("Add Another? (Y/N): ").upper()
            if ch == "N":
                break
        print("Prescription Saved Successfully")

    def view_medical_history(self):
        pat_id = int(input("Enter Patient ID to view Medical History: "))
        found = False

        for med_rec in self.db.medical_records:
            if med_rec.patient_id == pat_id:
                print(f"{med_rec.record_id}, {med_rec.patient_id}, {med_rec.doctor_id}, {med_rec.consultation_details}, {med_rec.diagnosis}, {med_rec.record_date}")
                found = True

        if not found:
            print("Medical Record not found for the specified Patient")
