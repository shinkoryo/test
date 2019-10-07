import pytest

@pytest.fixture()
def some_data():
	print("22222")
	yield
	print("hhhhh")

def test_some_data(some_data):
	print("test")