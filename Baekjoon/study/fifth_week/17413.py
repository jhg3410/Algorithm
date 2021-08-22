string = input()

word = ''
result = ''

tag = False
for chr in string:
    # print(word)
    if tag == False:
        if chr == '<':
            result += word[::-1]
            tag = True
            result += chr
        
        if chr.isdigit():
            word += chr

        if chr.isalpha():
            word += chr

        if chr == ' ':
            result += word[::-1]
            word = ''
            result += ' '

    elif tag == True:
        if chr == '>':
            tag = False
            word = ''
        result += chr

result += word[::-1]
print(result)
