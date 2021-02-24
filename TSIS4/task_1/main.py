import re

file = open('text.data', encoding="utf8")
text = file.read()

CompanyName = r"\nФилиал.*(?P<CompanyName>\b[A-Z]+)"
BINPattern = r"\nБИН.*(?P<BIN>\b[0-9]+)"

BIN = re.search(BINPattern, text).group("BIN")
Company = re.search(CompanyName, text).group("CompanyName")

print("Company Name:", Company)
print("BIN:", BIN)

itemPatternText = r"(?P<name>.*)\n{1}(?P<count>.*)x(?P<unit_price>.*)\n{1}(?P<g>.*)\n{1}Стоимость\n{1}(?P<overall>.*)"
itemPattern = re.compile(itemPatternText)


for m in re.finditer(itemPattern, text):
    print(m.group("name") + "\n" + m.group("count") + "\n" + m.group("unit_price") + "\n"+ m.group("overall"))

TimePattern = r"\nВремя: (?P<Time>\b[0-9].*\n{1}(?P<Address>.*))"
TimeText = re.search(TimePattern, text).group("Time")
AddressText = re.search(TimePattern, text).group("Address")
print(TimeText)

file.close()