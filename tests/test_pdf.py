import os
from pypdf import PdfReader
from .conftest import resources_path

def test_read_pdf():
    file_path = os.path.join(resources_path, 'docs-pytest-org-en-latest.pdf')
    reader = PdfReader(file_path)

    number_of_pages = len(reader.pages)

    assert number_of_pages == 412, f'Expected 412 pages, but got {number_of_pages} pages'

    first_page = reader.pages[0]
    text = first_page.extract_text()

    assert 'holger krekel, trainer and consultant, https://merlinux.eu/' in text






