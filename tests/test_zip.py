import zipfile
import os
from .conftest import tmp_path, resources_path


def test_create_zip_file():
    file_dir = os.listdir(resources_path)
    zip_file_path = os.path.join(tmp_path, 'resources.zip')

    with zipfile.ZipFile(zip_file_path, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        for file in file_dir:
            add_file = os.path.join(resources_path, file)
            zf.write(add_file)

    assert os.path.exists(zip_file_path)


def test_zip_file():
    zip_file_path = os.path.join(tmp_path, 'resources.zip')

    with zipfile.ZipFile(zip_file_path, mode='a') as zf:
        files = [os.path.basename(file.filename) for file in zf.infolist()]
        print(files)

        assert 'docs-pytest-org-en-latest.pdf' in files
        assert 'file_example_XLSX_50.xlsx' in files

