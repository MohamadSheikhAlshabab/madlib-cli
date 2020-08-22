import re
def welcome_msg():
    try:
        """
    Mad Libs is a phrasal template word game where one player prompts others for 
    a list of words to substitute for blanks in a story before reading aloud. 
    The game is frequently played as a party game or as a pastime.
        """
        print("""
    ****************************************
    |         Welcome to madlib            |
    | This is a phrasal template word game |
    | where one player prompts others for  |
    | a list of words to substitute for    |
    | blanks in a story before reading     |
    |  aloud.                              |
    ****************************************
    """)
    except Exception as e :
        print(f"THERE IS AN ERROR in welcome_msg, IS {e}")
    return print


def read_template():
    """
    This function to try to read the file if success will open it,
    if else there is the expection to return the message with the reason
    of this error.

    """
    try:
        with open('./files/template.txt','r') as file :
            contents=file.read()
        print("Is the file Closed? " , file.closed)
        return contents

    except Exception as e:
        print(f"THERE IS AN ERROR in read_template, IS {e}")
    # return("\n\n\nread_file :\n\n\n",contents)


def copy_file():
    """
    This function to copy the contents of file and make an 
    another version from it.
    """
    try:
        with open('./files/template-copy.txt','w') as file2 :
            file2.write(read_template())
        print("Is the file Closed? " , file2.closed)
        return print("\n\n\ncopy_file:\n\n\n",file2.write(read_template()))
    except Exception as e:
        print(f"THERE IS AN ERROR in copy_file, IS {e}")


inserts=[]
def parse(string):
    """
    This function to find matched words,
    then to insert instead of these words.
    """
    try:
        inputs=[]
        match =(r"(?<={)[\w'<>' -]+(?=})")
        inputs += re.findall(match, string)
        for i in inputs:
            insert=input(f"Insert {i} : ")
            if  insert.isdigit()==False:
                print(insert.isdigit()," Keep going inserting string")
                inserts.append(insert)
            elif insert.isdigit() == True:
                print(insert.isdigit(),"ALERT!!! you inserted a number")
                print ("YOU SHOULD INSTER A STRING, NOT ALLOWED TO INSERT NUMBERS.")
        return inputs
    except Exception as error:
        print(f"THERE IS AN ERROR IN parse, IS {error}" )
    return inserts

def merge(read,insert): 
    """
   This function is to merge a template with inserted inputs 
    """
    try:
        contents = read
        for words in range(21):
            start = contents.find("{")
            end = contents.find("}") + 1
            contents = contents[:start] + insert[words] + contents[end:]
        print(contents)
    except Exception as error:
        print(f"THERE IS AN ERROR in merge, IS {error}")

if __name__=="__main__":
    msg = welcome_msg()
    read = read_template()
    copy = copy_file()
    insert = parse(read)
    template = merge(read,inserts,parse)