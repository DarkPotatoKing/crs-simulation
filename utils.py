from __future__ import division

def center(s, length = 20):
    s = str(s)
    spaces = (length-len(s))
    r_spaces = spaces // 2
    l_spaces = spaces - r_spaces
    return ' ' * l_spaces +  s + ' ' * r_spaces