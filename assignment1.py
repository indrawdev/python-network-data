import re

fname = input("Enter file name: ")
if len(fname) < 1:
  fname = "regex_sum_1190588.txt"

data = open(fname)

lst = list()
text = ""

for line in data:
	text = text + " " + line.rstrip()
	lst = re.findall("[0-9]+", text)

lst = map(int, lst)
result = sum(lst)

print(result)