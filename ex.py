import re

text = "2026-01-14"

match = re.match(r"(\d{4})-(\d{2})-(\d{2})", text)

print("Year:", match.group(1))
print("Month:", match.group(2))
print("Day:", match.group(3))
