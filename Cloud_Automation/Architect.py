strikes = 0
while True:
    name = input("Enter Identity Credentials or press ENTER to insert clearance code: ")

    if name == 'Admin Shutdown':
        print("System powering down... Goodbye, Architect.")
        break
    if name == '':
        print("Zero input detected. Please identify yourself.")
        continue
    elif name == 'Suarez':
        print("Welcome Admin, the Architect!")
        strikes = 0
        continue
    elif name == 'Guest' or name == 'User':
        print("lol, you are a clown not even up to par to be called an intruder")
    else:
        print("Identity Unknown. Initiating Challenge...")
        strikes += 1
        if strikes == 3:
            print("Lockdown")
            break

        # STEP 1: Get the input as a RAW STRING (don't use int() yet!)
        raw_input = input("What's your level of clearance: ")
        # STEP 2: Use the sensor to check the string
        if raw_input.isdigit():
        # STEP 3: Now it's safe to convert
            clearance_code = int(raw_input)
            if clearance_code == 0:
                print("Trigger Alarm")
                break
            elif clearance_code >= 100:
              print("High Priority")
            else:
                print("Low Priority")
        else:
            # STEP 4: Handle the "Basic" user who typed letters
            print("Invalid Identity Signature. Numbers only, please.")