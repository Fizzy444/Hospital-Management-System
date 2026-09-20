from Model.Bill import Bill


class BillController:
    def __init__(self, database):
        self.db = database

    def admin_generate_bill(self):
        pat_id = int(input("Enter PatientID to generate Bill: "))
        total_amount = int(input("Enter amount to be paid: "))
        amount_paid = int(input("Enter amount paid: "))
        payment_status = "PENDING"

        import datetime
        today = datetime.datetime.now(tz=datetime.UTC).date()
        day = today.strftime("%d-%m-%Y")

        bill = Bill(self.db.nxt_bill_id, pat_id, total_amount, amount_paid, payment_status, day)
        self.db.bills.append(bill)

        print("Successfully Created Bill")

    def view_bill(self, patient):
        found = False
        for b in self.db.bills:
            if b.patient_id == patient.patient_id:
                print(f"BillID: {b.bill_id} | Total Amount: {b.total_amount} | Amount Paid: {b.amount_paid} | Payment Status: {b.payment_status} | Bill Date: {b.bill_date}")
                found = True

        if not found:
            print("You do not have any bills")

    def pay_bill(self, patient):
        bill_id = int(input("Enter the bill ID for which you want to pay: "))
        found = False
        for b in self.db.bills:
            if b.patient_id == patient.patient_id and b.bill_id == bill_id:
                found = True
                print(f"Total amount: {b.total_amount}")
                print(f"Amount Paid: {b.amount_paid}")
                amt = int(input("Enter the amount you are paying: "))
                b.amount_paid += amt

                if b.amount_paid == b.total_amount:
                    b.payment_status = "PAID"
                elif b.amount_paid > 0:
                    b.payment_status = "PARTIALLY PAID"

        if not found:
            print("Bill ID not found")
