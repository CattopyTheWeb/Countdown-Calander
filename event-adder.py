import time
add = True
while add:
    event = input("Enter your event name: ")
    day = input("Enter the day of the event: ")
    month = input("Enter the month of the event: ")
    full_year = input("Enter the year of the event: ")

    year = str(full_year)[-2:]

    f = open("events.txt", "a")
    f.write(f"{event},{day}/{month}/{year}")
    f.close()
    print("The event has successfully been added to the events.txt file.")
    more = input("Would you like to add another event to your events.txt file? (y/n)\n")
    
    if more == "n" or more == "N":
        print("Quitting...")
        time.sleep(3)
        add = False
        exit()

print("Error invalid input")
time.sleep(3)
exit()
