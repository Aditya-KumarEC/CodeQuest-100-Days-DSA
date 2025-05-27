input=input("enter the string")
output=""
for i in range (len(input)):
    if input[i]!='_':
        output+=input[i]
    else:
        pre_char=output[-1]
        nxt_char=chr(ord(pre_char)+1)
        output+=nxt_char
print("Restored output:",output)