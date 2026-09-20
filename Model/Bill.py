class Bill:
    def __init__(self, bill_id, patient_id, total_amount, amount_paid, payment_status, bill_date):
        self.bill_id = bill_id
        self.patient_id = patient_id
        self.total_amount = total_amount
        self.amount_paid = amount_paid
        self.payment_status = payment_status
        self.bill_date = bill_date
