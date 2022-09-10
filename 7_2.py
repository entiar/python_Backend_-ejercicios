from datetime import timedelta, datetime

now = datetime.now()
t1 = timedelta(hours = now.hour, minutes = now.minute, seconds = now.second)
t2 = timedelta(hours = 7, minutes = 0, seconds = 00)
t3 = t2 - t1

if t3>t2:
    print("Es hora deir a casa")
else:
    print("Falta ", t3, " para volver a casa")



