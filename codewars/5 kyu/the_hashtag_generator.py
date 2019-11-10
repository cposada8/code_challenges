# https://www.codewars.com/kata/the-hashtag-generator/train/python/5dc0975e0f3634002c462dba

def generate_hashtag(s):
    #your code here
    if s == "":
        return False
    capitalized = s.title().replace(" ", "")
    result = "#" + capitalized
    if len(result)>140:
        return False
    else:
        return result
    