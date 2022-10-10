import re

def read_template(path):
    """
    the function take a file path then read the content
    and return the content
    if theres no file it will raise FileNotFoundError  
    """

    try:
        with open(path) as f :
            content = f.read()
            return content
    except:
        raise FileNotFoundError("missing file")

def parse_template(content):
    """
    the parse_template function take the content then stripped it to parts 
    and return the stripped content and those parts
    """
    stripped = re.sub(r"[^{]+(?=})", "", content)
    parts=tuple(re.findall(r"[^{]+(?=})", content))
    return stripped,parts

def user_input(parts):
    """
    the user_input function take the user answer and put it in input_value as a list and return it as a tuple

    """
    input_value=[]
    for part in list(parts):
        input_value.append(input(f'Please enter a {part} : '))
    return tuple(input_value)
    

def merge(stripped,input_value):
    """
    the merge function merge parts to the stripped content then return it

    """
    return stripped.format(*input_value)


def madlib_cli(path):
    print('''
    Madlib-cli Game
it is a game that the player input a list of words to substitute for blanks in a story
lets starrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrt !!
''')

    read=read_template(path)
    stripped,parts =parse_template(read)
    inputs=user_input(parts)
    result = merge(stripped,inputs)
    print(result)
    with open ("assets/story.txt" ,"w") as story:
        story.write(result)
         
if __name__=="__main__":
    madlib_cli("assets/make_me_a_video_game_template.txt")