encoded_flag = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彤㔲挶戹㍽'

# How the flag got encrypted
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

# Attempt to reverse the process
flag = ''.join(
    [
        chr(
            (ord(enc[i]) >> 8) + ord(enc[i + 1])
            ) for i in range(0, len(enc), 2)
        ]
    )
print(flag)