# calculating time

time1 = int(input("Enter Hours: "))
time2 = int(input("Enter Minutes: "))

minute = time1*60
second = time2*60

print(time1, "h to Minute: ", minute, "min")
print(time2, "min to Seconds: ", second, "s")
total_minutes = minute + time2
total_seconds = time1*3600 + time2*60

print("Time-", time1,"h", time2,"min =",total_minutes, "min or", total_seconds, "s")
