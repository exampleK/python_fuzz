#时分秒
import datetime
from datetime import datetime
import time
zhi = 245959
new_zhi = ""
dic = open("c://sfm_am_pm.txt","a")
a2 = "2020-5-10 09:00:00"
cday = datetime.strptime('2020-5-10 09:00:00', '%Y-%m-%d %H:%M:%S')
import datetime
now_day=cday+datetime.timedelta(seconds=1)
now_day_str=now_day.strftime('%H%M%S')
print(now_day_str)
dic.write((now_day_str)+"\n")
while(now_day_str!='000000'):
    now_day=now_day+datetime.timedelta(seconds=1)
    now_day_str=now_day.strftime('%H%M%S')
    print(now_day_str)
    dic.write((now_day_str)+"\n")
    if(now_day_str=='180000'):
        dic.close()
        break
dic.close()