# https://www.codewars.com/kata/convert-string-to-camel-case/train/python/5dbcaa22ae55380025720e12

def to_camel_case(text):

    if len(text)==0:
        return text
    #your code here
    first_let = text[0]
        
    spaced = text.replace("-", " ")
    spaced = spaced.replace("_", " ")
    titled = spaced.title()
    joined = titled.replace(" ", "")
    result = first_let+joined[1:]
    
    return result
    