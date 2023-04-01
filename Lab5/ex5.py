import re

date = "2021-11-02"
date_pattern = re.compile(r"(\d{4})-(\d{2})-(\d{2})")
match = date_pattern.match(date)

if match:
    year = match.group(1)
    month = match.group(2)
    day = match.group(3)

    new_date = f"{day}-{month}-{year}"
    print("Original date:", date)
    print("New date:", new_date)
else:
    print("Invalid date format.")
