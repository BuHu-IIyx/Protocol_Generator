from docx import Document
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
    hdr_cells = table1.rows[0].cells
    hdr_cells[0].add_paragraph().add_run().add_picture('logo.jpg')
    hdr_cells[1].add_paragraph(lab.get_head())
    table2 = doc.add_table(rows=1, cols=2)
    hdr_cells2 = table2.rows[0].cells
    hdr_cells2[1].add_paragraph(lab.get_signature(date_off))
    doc.add_heading(customer.get_number_protocol())
    doc.add_paragraph(customer.get_text(date_izm))
    doc.save('test.docx')
