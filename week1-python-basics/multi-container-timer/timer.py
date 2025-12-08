import sys
import time

if len(sys.argv) > 1:
    seconds = int(sys.argv[1])
else:    
    name=input("Anong pangalan mo pare?")
    if not name:
        name = "Anonymous Boi"

    number=input(f"Hi {name} Putangina mo, ilang seconds gusto mo?")
    while not number.isdigit():
        number=input(f"Pare number lang tangina mo naman e")
    seconds= int(number)

print(f"Starting {seconds} second timer now")
print()

while seconds > 0:
    minutes = seconds // 60
    segundo = seconds % 60

    print(f"\r{minutes:02d}:{segundo:02d}", end="", flush=True)

    time.sleep(1)
    seconds = seconds - 1

print("\rTimes UP")
