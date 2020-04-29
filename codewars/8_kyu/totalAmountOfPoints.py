# https://www.codewars.com/kata/5bb904724c47249b10000131?utm_source=newsletter&utm_medium=email&utm_campaign=weekly_coding_challenges&utm_term=2020-04-28

def points(games):
    points = 0
    for match in games:
        x = int(match[0])
        y = int(match[2])
        points += points_match(x, y)
    return points
    
def points_match(x, y):
    points = 1
    if x>y:
        points=3
    if x<y:
        points=0
    return points