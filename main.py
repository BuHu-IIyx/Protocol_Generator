from Model.Company import Company
from Model.DB import ConnectionDB
from Model.testInit import lab_ini
from View.MainWindow import MainWindow
import tkinter as tk
import psycopg2
#
# lab = lab_ini()
# customer = customer_ini()
# company = Company()
# company.add_laboratories(lab)
# company.add_customers(customer)
# generate_protocol(lab, customer, "20 февраля 2022 г.", "14.02.2022 г.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    app.pack()
    root.mainloop()

# conn = psycopg2.connect("dbname=testDB user=postgres host=localhost password=452204 port=5432")
# cursor = conn.cursor()
# cursor.execute()
# conn.commit()
# conn.close()
