#replace woard from folowing string
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
name  = input("enter your name")
date = input("enter date")
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>",date)
print(letter)