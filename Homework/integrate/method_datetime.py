import datetime
# datetime.date	表示日期，常用的屬性有：year, month和day
# datetime.time	表示時間，常用屬性有：hour, minute, second, microsecond
# datetime.datetime	表示日期時間
# datetime.timedelta	表示兩個date、time、datetime例項之間的時間間隔，解析度（最小單位）可達到微秒
# datetime.tzinfo	時區相關資訊物件的抽象基類。它們由datetime和time類使用，以提供自定義時間的而調整。
# datetime.timezone	Python 3.2中新增的功能，實現tzinfo抽象基類的類，表示與UTC的固定偏移量
# datetime.weekday()：将星期几作为整数返回，其中星期一为0，星期日为6
# datetime.isoweek()：将星期几作为整数返回，星期一为1，星期日为7
# datetime.datetime(2018,7,24).strftime("%w") 星期幾，從0到6
