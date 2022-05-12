from datetime import datetime

date_string = "Feb 8 2022  8:43PM"
datetime_object = datetime.strptime(date_string, '%b %d %Y %I:%M%p')
print(datetime_object)
