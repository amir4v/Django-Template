from djnago.test import override_settings

import pytest


@pytest.fixture(autouse=True)
def test_settings(settings):
	with override_settings(SECRET_KEY='django-insecure-=!%dlpgnc+4mk7+2h!l4&x^3)r+q4+=nz@y3k&e)8gg^gtgqkn',):
		yield
