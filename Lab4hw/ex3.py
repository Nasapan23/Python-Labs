import datetime

date1_str = "20 March 2023"
date2_str = "25 March 2023"
date1 = datetime.datetime.strptime(date1_str, "%d %B %Y")
date2 = datetime.datetime.strptime(date2_str, "%d %B %Y")
delta = date2 - date1
print(f"There are {delta.days} days between {date1_str} and {date2_str}")
