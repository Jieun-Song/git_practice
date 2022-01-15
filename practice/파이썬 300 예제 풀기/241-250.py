# 241

# import datetime

# now = datetime.datetime.now()
# print(now)

# 242

# import datetime
# now = datetime.datetime.now()
# print(type(now))

# 243

# import datetime

# today = datetime.date.today()
# five_days = datetime.timedelta(days=5)
# four_days = datetime.timedelta(days=4)
# three_days = datetime.timedelta(days=3)
# two_days = datetime.timedelta(days=2)
# one_days = datetime.timedelta(days=1)

# print(today - five_days)
# print(today - four_days)
# print(today - three_days)
# print(today - two_days)
# print(today - one_days)

# 244

# import datetime

# now = datetime.datetime.now()
# print(now.strftime("%H:%M:%S"))

# 245

# import datetime

# now = datetime.datetime.strptime("2020-05-04", "%Y-%m-%d")
# print(type(now))

# 246

# import time
# import datetime

# while 1:
#     if time.time() % 1 <= 0.0001:
#         print(datetime.datetime.now())
