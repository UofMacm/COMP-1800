hour = 7
minute = 24
second = 8

second = second + 37 + 3*13 + 28
minute = minute + 12 + 3*8 + 20

minute = minute + second//60
second = second % 60
hour = hour + minute//60
minute = minute % 60

print(str(hour) + ":" + str(minute) + ":" + str(second))

