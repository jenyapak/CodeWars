def uni_total(s):
    unitotal = 0
    for i in s:
        unitotal = unitotal + ord(i)
    return unitotal


####A#A OR

def uni_total(s):
    return sum([ord(letter) for letter in s])
