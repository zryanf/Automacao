import re
with open("numero.txt", "r", encoding="utf-8") as file:
    file = file.read()
phoneRegex = re.compile(r'\(11\)\d\d\d\d\d-\d\d\d\d')
mo = phoneRegex.findall(file)
print(mo)
