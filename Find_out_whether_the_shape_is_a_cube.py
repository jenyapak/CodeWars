def cube_checker(volume, side):
    if volume <= 0 or side <= 0:
        return False
    elif side**3 == volume:
        return True
    else:
        return False
