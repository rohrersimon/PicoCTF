encoded_flag = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彤㔲挶戹㍽'

# How the flag got encrypted
flag = 'TEST'
enc = ''.join(
    [
        chr(
            (
                ord(flag[i]) << 8
                ) + ord(
                    flag[i + 1]
                    )
            ) for i in range(0, len(flag), 2)
        ]
    )

# Reverse the process
unicode_list = [ord(char) for char in encoded_flag]

flag_list = []
for element in unicode_list:
    second = element%256
    first = (element - second) >> 8
    flag_list.append(chr(first))
    flag_list.append(chr(second))

print(''.join(flag_list))