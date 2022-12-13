ascii = """114
114
114
111
99
107
110
114
110
48
49
49
51
114
"""

for c in ascii.split():
    print(chr(int(c)), end='')
