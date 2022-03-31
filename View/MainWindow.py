import tkinter as tk
from tkinter import CENTER, W, E
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

from Controller.MainController import get_labs_list, get_customer_list, get_factors_list, generate_protocol, \
    get_measure_list, get_methodologies_list, get_experts_list, get_customer, add_laboratory_click, add_customer_click


class MainWindow(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        root.title("Производственный контроль")
        root.geometry("650x445+300+200")
        root.resizable(False, False)
        self.init_main_window()

    def lab_checked(self, event):
        self.combo_cust.configure(values=get_customer_list(), state='normal')

    def customer_checked(self, event):
        self.combo_factor.configure(values=get_factors_list(self.combo_cust.get()), state='normal')
        self.show_button.configure(state='normal')

    def factor_checked(self, event):
        self.create_button.configure(state='normal')

    def show_button_click(self):
        self.generate_tree(self.combo_cust.get())

    def create_button_click(self):
        lab = self.combo_labs.get()
        cust = self.combo_cust.get()
        fact = self.combo_factor.get()
        GenerateProtocolWindow(lab, cust, fact)

    @staticmethod
    def add_lab_button_click():
        AddLabWindow()

    @staticmethod
    def add_cust_button_click():
        AddCustomerWindow()

    def generate_tree(self, customer_name):
        self.tree = ttk.Treeview(self, height=15)
        self.tree['columns'] = ('customer',)
        self.tree.column('#0', width=5)
        self.tree.column('customer', anchor=W, width=640)

        self.tree.heading('customer', text=customer_name, anchor=CENTER)
        dep_iid = ''
        wa_iid = ''
        customer = get_customer(customer_name)
        for dep in customer.departments:
            dep_iid = str(dep.department_id)
            self.tree.insert(parent='', index='end', iid=dep_iid, values=(dep.name,))
            for wa in dep.working_areas:
                wa_iid = str(wa.number) + '. '
                self.tree.insert(parent=dep_iid, index='end', iid=wa_iid, values=(wa_iid + wa.name,))
        self.tree.grid(column=0, row=0, columnspan=6)

    def init_main_window(self):
        self.toolbar = tk.Frame(bd=2)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        lab_list = get_labs_list()

        tk.Label(self.toolbar, text="Лаборатория:").grid(column=0, row=0)
        self.combo_labs = ttk.Combobox(self.toolbar)
        self.combo_labs.configure(values=lab_list)
        self.combo_labs.grid(column=1, row=0)
        self.combo_labs.bind("<<ComboboxSelected>>", self.lab_checked)

        self.add_lab_button = ttk.Button(self.toolbar, text='+', state='normal', width=2,
                                         command=self.add_lab_button_click)
        self.add_lab_button.grid(column=2, row=0)

        tk.Label(self.toolbar, text="Организация:").grid(column=0, row=1)
        self.combo_cust = ttk.Combobox(self.toolbar, state='disabled')
        self.combo_cust.grid(column=1, row=1)
        self.combo_cust.bind("<<ComboboxSelected>>", self.customer_checked)

        self.add_cust_button = ttk.Button(self.toolbar, text='+', state='normal', width=2,
                                          command=self.add_cust_button_click)
        self.add_cust_button.grid(column=2, row=1)

        tk.Label(self.toolbar, text="Производственный фактор:").grid(column=0, row=2)
        self.combo_factor = ttk.Combobox(self.toolbar, state='disabled')
        self.combo_factor.grid(column=1, row=2)
        self.combo_factor.bind("<<ComboboxSelected>>", self.factor_checked)

        self.show_button = ttk.Button(self.toolbar, text='Показать данные', state='disable', width=20,
                                      command=self.show_button_click)
        self.show_button.grid(column=3, row=1)

        self.create_button = ttk.Button(self.toolbar, text='Создать протокол', state='disable', width=20,
                                        command=self.create_button_click)
        self.create_button.grid(column=3, row=2)

        tk.Label(self.toolbar, text="").grid(column=0, row=3)

        # self.tree = ttk.Treeview(self.toolbar, height=30, show='headings')


class GenerateProtocolWindow(tk.Toplevel):
    def __init__(self, lab, cust, fact):
        super().__init__()
        self.lab = lab
        self.cust = cust
        self.fact = fact
        self.init_window()

    def create_button_click(self):
        zamer = self.combo_zam.get()
        oformitel = self.combo_oformit.get()
        measure = self.combo_measuring.get()
        methodologies = self.combo_methodologies.get()
        date = self.date.get_date()
        date_izm = self.date_zamer.get_date()
        generate_protocol(self.lab, self.cust, self.fact, zamer.split(': ')[0], oformitel.split(':')[0],
                          measure.split(':')[0], methodologies.split(':')[0], date, date_izm)
        self.destroy()

    def init_window(self):
        self.title('Создание протокола')
        self.geometry('300x200+400+300')
        self.resizable(False, False)

        self.grab_set()
        self.focus_set()

        tk.Label(self, text="Выберите замерщика:", bd=5).grid(column=0, row=1)
        self.combo_zam = ttk.Combobox(self, values=get_experts_list())
        self.combo_zam.grid(column=1, row=1)

        tk.Label(self, text="Выберите оформителя:", bd=5).grid(column=0, row=2)
        self.combo_oformit = ttk.Combobox(self, values=get_experts_list())
        self.combo_oformit.grid(column=1, row=2)

        tk.Label(self, text="Выберите приборы:", bd=5).grid(column=0, row=3)
        self.combo_measuring = ttk.Combobox(self, values=get_measure_list(self.fact))
        self.combo_measuring.grid(column=1, row=3)

        tk.Label(self, text="Выберите методики:", bd=5).grid(column=0, row=4)
        self.combo_methodologies = ttk.Combobox(self, values=get_methodologies_list(self.fact))
        self.combo_methodologies.grid(column=1, row=4)

        tk.Label(self, text="Дата протокола:", bd=5).grid(column=0, row=5)
        self.date = DateEntry(self, width=20, foreground="white", bd=2)
        self.date.grid(column=1, row=5)

        tk.Label(self, text="Дата замера:", bd=5).grid(column=0, row=6)
        self.date_zamer = DateEntry(self, width=20, foreground="white", bd=2)
        self.date_zamer.grid(column=1, row=6)

        self.exit_button = ttk.Button(self, text='Отмена', width=20, command=self.destroy)
        self.exit_button.grid(column=0, row=7)

        self.create_button = ttk.Button(self, text='Добавить', width=20, command=self.create_button_click)
        self.create_button.grid(column=1, row=7)


class AddLabWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_window()

    def add_button_click(self):
        add_laboratory_click(self.entry_short_name.get(), self.entry_name, self.entry_name_lab, self.entry_logo,
                             self.entry_director, self.entry_address, self.entry_certificate_number, self.entry_phone,
                             self.entry_e_mail)
        self.destroy()

    def init_window(self):
        self.title('Добавить лабораторию')
        self.geometry('500x280+400+300')
        self.resizable(False, False)

        self.grab_set()
        self.focus_set()

        tk.Label(self, text="Название сокращенное:", bd=5).grid(column=0, row=1)
        self.entry_short_name = ttk.Entry(self, width=55)
        self.entry_short_name.grid(column=1, row=1, columnspan=2)

        tk.Label(self, text="Название полное:", bd=5).grid(column=0, row=2)
        self.entry_name = ttk.Entry(self, width=55)
        self.entry_name.grid(column=1, row=2, columnspan=2)

        tk.Label(self, text="Название лаборатории:", bd=5).grid(column=0, row=3)
        self.entry_name_lab = ttk.Entry(self, width=55)
        self.entry_name_lab.grid(column=1, row=3, columnspan=2)

        tk.Label(self, text="Логотип:", bd=5).grid(column=0, row=4)
        self.entry_logo = ttk.Entry(self, width=55)
        self.entry_logo.grid(column=1, row=4, columnspan=2)

        tk.Label(self, text="Руководитель:", bd=5).grid(column=0, row=5)
        self.entry_director = ttk.Entry(self, width=55)
        self.entry_director.grid(column=1, row=5, columnspan=2)

        tk.Label(self, text="Адрес:", bd=5).grid(column=0, row=6)
        self.entry_address = ttk.Entry(self, width=55)
        self.entry_address.grid(column=1, row=6, columnspan=2)

        tk.Label(self, text="Номер сертификата:", bd=5).grid(column=0, row=7)
        self.entry_certificate_number = ttk.Entry(self, width=55)
        self.entry_certificate_number.grid(column=1, row=7, columnspan=2)

        tk.Label(self, text="Телефон:", bd=5).grid(column=0, row=8)
        self.entry_phone = ttk.Entry(self, width=55)
        self.entry_phone.grid(column=1, row=8, columnspan=2)

        tk.Label(self, text="E-mail:", bd=5).grid(column=0, row=9)
        self.entry_e_mail = ttk.Entry(self, width=55)
        self.entry_e_mail.grid(column=1, row=9, columnspan=2)

        self.exit_button = ttk.Button(self, text='Отмена', width=20, command=self.destroy)
        self.exit_button.grid(column=1, row=10)

        self.create_button = ttk.Button(self, text='Создать', width=20, command=self.add_button_click)
        self.create_button.grid(column=2, row=10)


class AddCustomerWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_window()

    def add_button_click(self):
        add_customer_click(self.entry_short_name.get(), self.entry_name, self.entry_legal_address,
                           self.entry_actual_address, self.entry_contract_number, self.entry_contract_date)
        self.destroy()

    def init_window(self):
        self.title('Добавить заказчика.')
        self.geometry('500x220+400+300')
        self.resizable(False, False)

        self.grab_set()
        self.focus_set()

        tk.Label(self, text="Название сокращенное:", bd=5).grid(column=0, row=1)
        self.entry_short_name = ttk.Entry(self, width=55)
        self.entry_short_name.grid(column=1, row=1, columnspan=2)

        tk.Label(self, text="Название полное:", bd=5).grid(column=0, row=2)
        self.entry_name = ttk.Entry(self, width=55)
        self.entry_name.grid(column=1, row=2, columnspan=2)

        tk.Label(self, text="Юридический адрес:", bd=5).grid(column=0, row=3)
        self.entry_legal_address = ttk.Entry(self, width=55)
        self.entry_legal_address.grid(column=1, row=3, columnspan=2)

        tk.Label(self, text="Фактический адрес:", bd=5).grid(column=0, row=4)
        self.entry_actual_address = ttk.Entry(self, width=55)
        self.entry_actual_address.grid(column=1, row=4, columnspan=2)

        tk.Label(self, text="Номер договора:", bd=5).grid(column=0, row=5)
        self.entry_contract_number = ttk.Entry(self, width=55)
        self.entry_contract_number.grid(column=1, row=5, columnspan=2)

        tk.Label(self, text="Дата договора:", bd=5).grid(column=0, row=6)
        self.entry_contract_date = DateEntry(self, width=50, foreground="white", bd=2)
        self.entry_contract_date.grid(column=1, row=6, columnspan=2)

        self.exit_button = ttk.Button(self, text='Отмена', width=20, command=self.destroy)
        self.exit_button.grid(column=1, row=7)

        self.create_button = ttk.Button(self, text='Создать', width=20, command=self.add_button_click)
        self.create_button.grid(column=2, row=7)
