import re

pattern = "Was"
text = "Hello Was World"

match = re.search(pattern, text)
match = re.finditer(pattern, text)
print(match)