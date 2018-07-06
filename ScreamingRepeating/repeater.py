times = input("How many times do I have to tell you? ")

if times:
    times = int(times)
    for time in range(times):
        print("CLEAN UP YOUR ROOM!")
else:
    print("Tell me how many times!")
