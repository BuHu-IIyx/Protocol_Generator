import tkinter as tk
from tkinter import CENTER, W, E, S
from tkinter import ttk
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkcalendar import Calendar, DateEntry

from Controller.MainController import get_labs_list, get_customer_list, get_factors_list, generate_protocol, \
    get_measure_list, get_methodologies_list, get_experts_list, get_customer, add_laboratory_click, add_customer_click, \
    add_department_click, add_workplace_click, edit_department_click, edit_workplace_click, export_workplaces_click, \
    import_workplaces_click, import_wp_click


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
        self.import_wp_button.configure(state='normal')

    def factor_checked(self, event):
        self.create_button.configure(state='normal')
        self.export_button.configure(state='normal')
        self.import_button.configure(state='normal')

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

    def add_department_button_click(self):
        customer_name = self.tree.heading('customer').get('text')
        AddDepartmentWindow(customer_name)

    def add_workplace_button_click(self):
        customer_name = self.tree.heading('customer').get('text')
        if '.' in self.tree.focus():
            department_id = self.tree.parent(self.tree.focus())
        else:
            department_id = self.tree.focus()

        department_name = self.tree.item(department_id).get('values')[0]
        AddWorkplaceWindow(department_id, department_name, customer_name)

    def edit_button_click(self):
        customer_name = self.tree.heading('customer').get('text')
        if '.' in self.tree.focus():
            department_id = self.tree.parent(self.tree.focus())
            department_name = self.tree.item(department_id).get('values')[0]
            wp_name = self.tree.item(self.tree.focus()).get('values')[0]
            wp_id = self.tree.focus()
            wp_id = wp_id.partition('.')[0]
            AddWorkplaceWindow(department_id, department_name, customer_name, wp_name, int(wp_id))
        else:
            department_id = self.tree.focus()
            customer_name = self.tree.heading('customer').get('text')
            department_name = self.tree.item(department_id).get('values')[0]
            AddDepartmentWindow(customer_name, department_name, int(department_id))

    def export_button_click(self):
        file = asksaveasfilename(defaultextension=".csv", initialfile="report.csv")
        export_workplaces_click(file, self.combo_cust.get(), self.combo_factor.get())

    def import_button_click(self):
        file = askopenfilename()
        import_workplaces_click(file, self.combo_factor.get())
        print(file)

    def import_wp_button_click(self):
        file = askopenfilename()
        import_wp_click(file, self.combo_cust.get())

    def update_treeview(self, customer_name):
        self.tree.heading('customer', text=customer_name, anchor=CENTER)
        dep_iid = ''
        wa_iid = ''
        count = 1
        customer = get_customer(customer_name, self.combo_factor.get())
        for dep in customer.departments:
            dep_iid = str(dep.department_id)
            self.tree.insert(parent='', index='end', iid=dep_iid, values=(dep.name,))
            for wa in dep.working_areas:
                wa_iid = str(wa.number) + '. '
                self.tree.insert(parent=dep_iid, index='end', iid=wa_iid, values=(str(count) + '. ' + wa.name,))
                count += 1

    def generate_tree(self, customer_name):
        if hasattr(self, 'tree'):
            for i in self.tree.get_children():
                self.tree.delete(i)
            self.update_treeview(customer_name)

        else:
            self.grid_frame = tk.Frame(bd=2)
            self.grid_frame.pack(side=tk.TOP, fill=tk.X)

            self.add_department_button = ttk.Button(self.grid_frame, text='Добавить отдел', state='normal',
                                                    command=self.add_department_button_click)
            self.add_department_button.pack(side=tk.LEFT, fill=tk.X, expand=True)

            self.add_workplace_button = ttk.Button(self.grid_frame, text='Добавить РМ', state='normal',
                                                   command=self.add_workplace_button_click)
            self.add_workplace_button.pack(side=tk.LEFT, fill=tk.X, expand=True)

            self.edit_button = ttk.Button(self.grid_frame, text='Изменить', state='normal',
                                          command=self.edit_button_click)
            self.edit_button.pack(side=tk.LEFT, fill=tk.X, expand=True)

            self.tree_frame = tk.Frame(bd=2)
            self.tree_frame.pack(side=tk.TOP, fill=tk.BOTH)

            self.tree = ttk.Treeview(self.tree_frame, height=14, selectmode='browse')
            self.tree['columns'] = ('customer',)
            self.tree.column('#0', width=5)
            self.tree.column('customer', anchor=W, width=635)

            self.update_treeview(customer_name)

            self.tree.pack(side=tk.LEFT, fill=tk.BOTH)

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
        self.show_button.grid(column=4, row=1)

        self.create_button = ttk.Button(self.toolbar, text='Создать протокол', state='disable', width=20,
                                        command=self.create_button_click)
        self.create_button.grid(column=4, row=2)

        self.import_wp_button = ttk.Button(self.toolbar, text='Импорт РМ', state='disable', width=15,
                                           command=self.import_wp_button_click)
        self.import_wp_button.grid(column=3, row=0)

        self.export_button = ttk.Button(self.toolbar, text='Экспорт зон', state='disable', width=15,
                                        command=self.export_button_click)
        self.export_button.grid(column=3, row=1)

        self.import_button = ttk.Button(self.toolbar, text='Импорт зон', state='disable', width=15,
                                        command=self.import_button_click)
        self.import_button.grid(column=3, row=2)

        tk.Label(self.toolbar, text="").grid(column=0, row=3)


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
        self.title('Добавить заказчика')
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


class AddDepartmentWindow(tk.Toplevel):
    def __init__(self, customer_name, department_name='', department_id=0):
        super().__init__()
        self.customer_name = customer_name
        self.department_name = department_name
        self.department_id = department_id
        self.init_window()

    def add_button_click(self):
        if self.department_id == 0:
            add_department_click(self.entry_department_name.get(), self.customer_name)
        else:
            edit_department_click(self.department_id, self.entry_department_name.get())
        self.destroy()

    def init_window(self):
        self.title('Добавить отдел')
        self.geometry('500x130+400+300')
        self.resizable(False, False)

        self.grab_set()
        self.focus_set()

        tk.Label(self, text=self.customer_name, bd=5).grid(column=0, row=0)

        tk.Label(self, text="Название отдела:", bd=5).grid(column=0, row=1)
        self.entry_department_name = ttk.Entry(self, width=55)
        self.entry_department_name.insert(0, self.department_name)
        self.entry_department_name.grid(column=1, row=1, columnspan=2)

        self.exit_button = ttk.Button(self, text='Отмена', width=20, command=self.destroy)
        self.exit_button.grid(column=1, row=2)

        self.create_button = ttk.Button(self, text='Создать', width=20, command=self.add_button_click)
        self.create_button.grid(column=2, row=2)


class AddWorkplaceWindow(tk.Toplevel):
    def __init__(self, department_id, department_name, customer_name, wp_name='', wp_id=0):
        super().__init__()
        self.department_id = department_id
        self.customer_name = customer_name
        self.department_name = department_name
        self.wp_name = wp_name
        self.wp_id = wp_id
        self.init_window()

    def add_button_click(self):
        if self.wp_id != 0:
            edit_workplace_click(self.wp_id, self.entry_wp_name.get(), self.check_noise.get(),
                                 self.check_loc_vib.get(), self.check_gen_vib.get())
        else:
            add_workplace_click(self.entry_wp_name.get(), self.department_id, self.check_noise.get(),
                                self.check_loc_vib.get(), self.check_gen_vib.get())
        self.destroy()

    def init_window(self):
        self.title('Добавить отдел')
        self.geometry('400x200+400+300')
        self.resizable(False, False)

        self.grab_set()
        self.focus_set()

        tk.Label(self, text=self.customer_name + ' - ' + self.department_name, bd=5). \
            grid(column=0, row=0, columnspan=3, sticky=W)

        tk.Label(self, text="Название точки:", bd=5).grid(column=0, row=2, sticky=W)
        self.entry_wp_name = ttk.Entry(self, width=40)
        self.entry_wp_name.insert(0, self.wp_name)
        self.entry_wp_name.grid(column=1, row=2, columnspan=2)

        tk.Label(self, text="Выберите факторы:", bd=5).grid(column=0, row=3, sticky=W)
        self.check_noise = tk.BooleanVar()
        self.check_noise.set(0)
        self.check_loc_vib = tk.BooleanVar()
        self.check_loc_vib.set(0)
        self.check_gen_vib = tk.BooleanVar()
        self.check_gen_vib.set(0)
        ttk.Checkbutton(self, text='Шум', variable=self.check_noise, onvalue=1, offvalue=0). \
            grid(column=1, row=3, columnspan=2, sticky=W)
        ttk.Checkbutton(self, text='Вибрация локальная', variable=self.check_loc_vib, onvalue=1, offvalue=0). \
            grid(column=1, row=4, columnspan=2, sticky=W)
        ttk.Checkbutton(self, text='Вибрация общая', variable=self.check_gen_vib, onvalue=1, offvalue=0). \
            grid(column=1, row=5, columnspan=2, sticky=W)

        tk.Label(self, text=" ", bd=5).grid(column=0, row=6, columnspan=3)

        self.exit_button = ttk.Button(self, text='Отмена', width=20, command=self.destroy)
        self.exit_button.grid(column=1, row=6)

        self.create_button = ttk.Button(self, text='Создать', width=20, command=self.add_button_click)
        self.create_button.grid(column=2, row=6)
