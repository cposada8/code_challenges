# https://www.codewars.com/kata/human-readable-duration-format/train/python/5dc4377506d013000fa85307

def calculate_units(seconds, unit):
    constants = {
        "year": 31536000,
        "day": 86400,
        "hour": 3600,
        "minute": 60,
        "second": 1
    }
    constant = constants[unit]
    units = int(seconds/constant)
    seconds_left = seconds-units*constant
    
    return units, seconds_left
    
def text_unit(units, name_unit):
    if units == 0:
        return ""

    add_s = "s" if units > 1 else ""
    
    answer = str(units) + " " + name_unit + add_s
    return answer

def format_duration(seconds):
    #your code here
    if seconds == 0:
        return "now"
      
    
    unit_names = ["year", "day", "hour", "minute", "second"]
    units = [] # each position means one unit.
    
    
    for unit_name in unit_names:
        unit_actual, seconds = calculate_units(seconds, unit_name)
        units.append(unit_actual)
    
    
    # select the last unit different from 0
    last_index = 0
    num_different_units = 0
    for i in range(5):
        if units[i] != 0:
            last_index = i
            num_different_units += 1
    
    
    # generate the answer
    answer = ""
    add_and = " and " if num_different_units != 1 else ""
    
    for i in range(last_index):
        units_actual = units[i]
  
        if units_actual != 0:
            unit_name = unit_names[i]
            add_comma = ", " if len(answer) != 0 else ""
            answer += add_comma + text_unit(units_actual, unit_name)
    
    answer += add_and + text_unit(units[last_index], unit_names[last_index]) 
    return answer
    
    
    
    