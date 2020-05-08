#Weather forecasting organization wants to show is it day or night.
#So, write a program for such organization to find whether is it dark outside or not.


from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H")
print("Day" if int(current_time) < 17 else "NIGHT" )
