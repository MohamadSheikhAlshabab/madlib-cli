from madlib_cli.madlib import welcome_msg , read_file , copy_file , insert_fun , template , __name__


def test_read_template():
    """
    to test read file
    """
    try:
        expected =open('../files/text.txt','r')
        actual= insert_fun('../files/test.txt')
        assert actual == expected
    except Exception as e:
        print(f"Error in  test_parse : {e}")

def test_parse():
    """
    to test if template fill it with items of list
    """
    try:
        expected ="""
        Make Me A Video Game!

I the {Adjective1} and {Adjective2} {A First Name3} have {Past Tense Verb4}{A First Name5}'s {Adjective6} sister and plan to steal her {Adjective7} {Plural Noun8}!

What are a {Large Animal9} and backpacking {Small Animal10} to do? Before you can help {A Girl's Name11}, you'll have to collect the {Adjective12} {Plural Noun13} and {Adjective14} {Plural Noun15} that open up the {Number 2-5016} worlds connected to A {First Name's17} Lair. There are {Number18} {Plural Noun19} and {Number20} {Plural Noun21} in the game, along with hundreds of other goodies for you to find.
"""
        actual= template(["Adjective1" ,"Adjective2" ,"A First Name3" ,"Past Tense Verb4","A First Name5","Adjective6","Adjective7","Plural Noun8","Large Animal9","Small Animal10","A Girl's Name11","Adjective12","Plural Noun13","Adjective14","Plural Noun15","Number 1-5016","First Name's17","Number18","Plural Noun19","Number20" ,"Plural Noun21"])
        assert actual == expected
    except Exception as e:
        print(f"Error in  test_parse : {e}")


def test_merge():
    """
    to merge contents of list and fill it in template.
    """
    try:
        expected = template(["1","2","3"])
        actual= insert_fun("i am {bla bla} with {bla's bla} have {bla 1-5 bla}")
        assert actual == expected
    except Exception as e:
        print(f"Error in  test_parse : {e}")