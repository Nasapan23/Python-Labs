import datetime

date_str = "24 March 2023"
date = datetime.datetime.strptime(date_str, "%d %B %Y")
week_num = date.strftime("%U")
print(f"The week number of {date_str} is {week_num}")
