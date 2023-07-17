import os.path
import requests
from .conftest import tmp_path



def test_download_png():
    url = 'https://selenium.dev/images/selenium_logo_square_green.png'

    response = requests.get(url)
    with open(os.path.join(tmp_path, 'selenium_logo.png'), 'wb') as file:
        file.write(response.content)

    size = os.path.getsize(os.path.join(tmp_path, 'selenium_logo.png'))
    print(size)

    assert os.path.exists(os.path.join(tmp_path, 'selenium_logo.png'))
    assert size == 30803

    os.remove(os.path.join(tmp_path, 'selenium_logo.png'))