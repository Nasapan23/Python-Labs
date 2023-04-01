import re

link = "https://www.newyorker.com/magazine/2021/11/01/the-book-of-form-and-emptiness-the-war-for-gloria-read-until-you-understand-and-the-end-of-bias"

date_pattern = re.compile(r"/(\d{4})/(\d{2})/(\d{2})/")
match = date_pattern.search(link)

if match:
    year = match.group(1)
    month = match.group(2)
    day = match.group(3)

    print("Year:", year)
    print("Month:", month)
    print("Day:", day)
else:
    print("No date found in link.")
