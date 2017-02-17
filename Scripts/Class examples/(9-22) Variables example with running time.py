hour = int(input("Enter the hour: "))
minute = int(input("Enter the minute: "))
second = int(input("Enter the second: "))

# add the minutes and seconds from the run
second = second + 37 + 3*13 + 28
minute = minute + 12 + 3*8 + 20

# convert the extra seconds into minutes
minute = minute + second//60
second = second % 60

# convert the extra minutes into hours
hour = hour + minute//60
minute = minute % 60

print(hour,":",minute,":",second)  # Python automatically adds spaces between all items separated by commas
print(str(hour) + ":" + str(minute) + ":" + str(second))   # since Python can't add strings and non-strings, we use str() to convert our variables into strings
