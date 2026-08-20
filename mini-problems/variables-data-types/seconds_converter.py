seconds = int(input("Enter seconds: "))

hours = seconds//3600
minutes = (seconds%3600)//60
seconds = seconds%60

if hours != 1:
    print(f"{hours} hours")
else:
    print(f"{hours} hour")

if minutes != 1:
    print(f"{minutes} minutes")
else:
    print(f"{minutes} minute")

if seconds != 1:
    print(f"{seconds} seconds")
else:
    print(f"{seconds} second")