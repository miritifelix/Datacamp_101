# Initialize offset
offset = -8

# Code the while loop
while offset != 0:
    print('correcting...')
    if offset > 1:
        offset = offset - 1
    else:
        offset = offset + 1
    print(offset)
