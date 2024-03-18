print(ord('a')) # 97
print(ord('a') << 8) # 24832
print(ord('b')) # 98
print(ord('b') << 8) # 25088
print(ord('c')) # 99
print(ord('c') << 8) # 25344

print(2**8)
# difference is 256 between << 8 characters

# reversing the effect
a = ord('a') # 97
not_a = ord('a') << 8 # 24832
print(not_a >> 8) # 97

# unserstanding the chr function
a = ord('a')
print(chr(a)) # a
not_a = ord('a') << 8
print(chr(not_a)) # 愀
print(chr(not_a >> 8)) # a

# understanding Unicode numbers
print(chr(24832))
print(chr(24833))

# Flag format is: picoCTF{...}
flag = r'picoCTF{}'
for c in flag:
    print(ord(c))
"""
112 > p
105 > i
99 > c
111 > o
67 > C
84 > T
70 > F
123 > {
125 > }
"""

def get_unicode(word: str) -> list:
    return [ord(c) for c in word]

def get_word(unicode_list: list) -> str:
    return ''.join([chr(i) for i in unicode_list])

unicode = get_unicode(r'picoCTF{}')
print(unicode)
print(get_word(unicode))