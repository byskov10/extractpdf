from pdfminer.high_level import extract_pages

def pages(pdf):
    page_count = sum(1 for _ in extract_pages(pdf))
    return page_count

import re
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBox, LTTextLine
import pandas as pd
def beskrivelse(pdf, page):    
    specific_x = 199.680
    text_input = []

    for page_layout in extract_pages(pdf, page_numbers=[page]):
        for element in page_layout:
            if isinstance(element, (LTTextBox, LTTextLine)):
                if specific_x == element.x0:
                    text_input.extend(element.get_text().split("\n"))

    df = pd.DataFrame({"Beskrivelse": text_input})
    return df