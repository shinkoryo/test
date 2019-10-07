# test_sysexit.py 的内容
import pytest
def f():
	raise SystemExit(1)

def test_mytest():
	with pytest.raises(SystemExit):
		f()