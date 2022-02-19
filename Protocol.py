from docx import Document
from docx.enum.section import WD_ORIENTATION, WD_SECTION_START

from Laboratory import *
from Customer import *


def generate_protocol():
    doc = Document()
    current_section = doc.sections[-1]
    new_width, new_height = current_section.page_height, current_section.page_width
    current_section.orientation = WD_ORIENTATION.LANDSCAPE
    current_section.page_width = new_width
    current_section.page_height = new_height
    doc.add_paragraph('Новый абзац с отступами и красной строкой.')
    doc.add_paragraph('Новый абзац.')
    doc.add_paragraph('Еще новый абзац.')
    doc.save('test.docx')
