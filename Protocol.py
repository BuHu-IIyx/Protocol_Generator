from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.enum.section import WD_ORIENTATION, WD_SECTION_START

from Laboratory import *
from Customer import *


def generate_protocol(lab, customer, date_off, date_izm):
    doc = Document()
    current_section = doc.sections[-1]
    new_width, new_height = current_section.page_height, current_section.page_width
    current_section.orientation = WD_ORIENTATION.LANDSCAPE
    current_section.page_width = new_width
    current_section.page_height = new_height
    table1 = doc.add_table(rows=1, cols=2)
    table1_cells = table1.rows[0].cells
    table1_cells[0].paragraphs[0].add_run().add_picture('logo.jpg')
    table1_cells[1].paragraphs[0].add_run(lab.get_head())
    table2 = doc.add_table(rows=1, cols=2)
    table2_cells = table2.rows[0].cells
    table2_cells[1].paragraphs[0].add_run(lab.get_signature(date_off))
    doc.add_heading(customer.get_number_protocol())
    doc.add_paragraph(customer.get_text(date_izm))
    doc.add_paragraph("11. Сведения о средствах измерения:")
    table3 = doc.add_table(rows=2, cols=6)
    table3.cell(0, 0).merge(table3.cell(1, 0)).text = "Наименование средства измерения"
    table3.cell(0, 1).merge(table3.cell(1, 1)).text = "Заводской номер"
    table3.cell(0, 2).merge(table3.cell(0, 4)).text = "Свидетельство о государственной поверке"
    table3.cell(1, 2).text = "Номер"
    table3.cell(1, 3).text = "Выдано"
    table3.cell(1, 4).text = "Действительно до"
    table3.cell(0, 5).merge(table3.cell(1, 5)).text = "Погрешность измерения"
    for i in range(0, 3):
        cells = table3.add_row().cells
        for j, item in enumerate(lab.get_measure(i)):
            cells[j].text = str(item)
    doc.add_paragraph("12. Идентификация используемого метода/методик (нормативно-техническая документация), "
                      "а также дополнительная информация, востребованная заказчиком (НД, необходимые для оценки):  ")

    doc.save('test.docx')
