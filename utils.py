from __future__ import division

def center(s, length = 20):
    s = str(s)
    spaces = (length-len(s))
    left_spaces = spaces // 2
    right_spaces = spaces - left_spaces
    return ' ' * left_spaces +  s + ' ' * right_spaces