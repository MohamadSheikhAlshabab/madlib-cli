from madlib_cli.madlib import welcome_msg , read_template, parse , merge 
import pytest


# @pytest.fixture
def test_read_template():
    """
    to test read file
    """
    try:
        expected =open('../files/text.txt','r')
        actual= template('../files/test.txt')
        assert actual == expected
    except Exception as e:
        print(f"Error in  test_parse : {e}")

# @pytest.fixture
def test_parse():
    """
    to test if template fill it with items of list
    """
    try:
        expected =["bla_bla_1","bla_bla_2","bla_Bla_3"]
        actual= parse("I'm {bla_bla_1} and you are {bla_bla_2} and we're {bla_bla_3} ")
        assert actual == expected
    except Exception as e:
        print(f"Error in  test_parse : {e}")

# @pytest.fixture
def test_merge():
    """
    to merge contents of list and fill it in template.
    """
    try:
        inserts=["Mohamad","Bechlor's degree"," 5 dogs"]
        template= "i am %s, I have %s, I have %s"
        parse=["Name","Your's Degree","1-100 animal"]
        expected = "i am Mohamad, I have Bechlor's degree, I have 5 dogs"
        actual= merge(template , inserts,parse)
        assert actual == expected
    except Exception as e:
        print(f"Error in  test_parse : {e}")