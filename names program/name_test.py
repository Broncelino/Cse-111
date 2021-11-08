from names import make_full_name, \
    extract_given_name, extract_family_name
import pytest

def test_make_full_name():
    name = make_full_name('jo','jame')
    assert name == "jame;jo","didn't work"
    print("all good")

def test_extract_family_name():
    name = extract_family_name('jo; jame')
    assert name == "jo","no good"
    print("all good")

def test_extract_given_name():
    name = extract_given_name("jo; jame")
    assert name == "jame","all bad"
    print("goodie goodie")

'''test_make_full_name()
test_extract_family_name()
test_extract_given_name()'''

pytest.main(["-v", "--tb=line", "-rN", __file__])