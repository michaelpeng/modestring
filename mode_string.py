"""
s = "ababab"
"aaaaa"

"aa"

s
s[0..1]

d = {}
d['key'] = 'value'
d.keys


most common L-character substring
care about ties

-----
"""

def mode_string(s, L):
    n = s.length
    i = 0 # counter
    d = {} # dict of keys
    
    while i < n-(L-1):
        if d[s[i..i+L]]:
             d[s[i..i+L]] += 1
        else:
            d[s[i..i+L]] = 1
        i+=1
    
    max = []
    maxvalue = 0
    keylist = d.keys
    
    for key in d.keys:
        if d[key] > maxvalue:
            max = [key]
            maxvalue = d[key]
        elif d[key] == maxvalue:
            max.append(key)
    
    return max