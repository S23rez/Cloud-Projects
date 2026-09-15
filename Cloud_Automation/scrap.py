import sys, random

# --- CHAPTER 3: FUNCTION DEFINITIONS ---
def clearance_sensor(strikes):
    """
    This is a function. It uses a PARAMETER (strikes).
    It returns a string to the main loop (The 'Return' value).
    """
    print(f"--- ATTEMPT {strikes} ---")
    raw_input = input("Enter Clearance Code (Numbers Only): ")

    # Truthy/Falsey check: empty string is falsey
    if not raw_input:
        print("Error: Empty input is falsey.")
        return "RETRY"

    if raw_input.isdigit():
        code = int(raw_input)  # Convert string to integer
        if code == 0:
            return "ALARM"
        elif code >= 100:
            print("Access Level: High Priority")
            return "SUCCESS"

    print("Invalid Code.")
    return "FAIL"


# --- THE MAIN PROGRAM ---
strikes = 0  # Global variable

while True:  # 1. VALID WHILE STATEMENT
    name = input("\nEnter Identity (or 'quit'): ")

    # 2. BREAK AND EXIT LOGIC
    if name.lower() == 'quit':
        print("Exiting via sys.exit()...")
        sys.exit()  # 3. ENDING PROGRAM EARLY

    # 4. CONTINUE LOGIC
    if name == '':
        print("Name cannot be empty. Restarting loop...")
        continue  # Skips the rest of the code, jumps to top

    if name == 'Suarez':
        print("Welcome, Architect.")

        # 5. FOR LOOP AND RANGE LOGIC (Quiz questions 40-43)
        print("Loading System Modules...")
        for i in range(0, 101, 25):  # Start at 0, stop at 100, step by 25
            print(f"Progress: {i}%")

        # 6. TREE PRINTER PROJECT (From your PDF)
        size = 5
        print("\nSecurity Status Tree:")
        for row in range(1, size + 1):
            # Using String Multiplication (' ' * count)
            spaces = ' ' * (size - row)
            branches = '^' * (row * 2 - 1)
            print(spaces + branches)
        print((' ' * (size - 1)) + "#")  # The Trunk
        continue

    # 7. THE CHALLENGE LOGIC
    strikes += 1
    if strikes >= 3:
        print("STRIKE 3. LOCKDOWN.")
        break  # Breaks the while loop entirely

    # Calling the function from Chapter 3
    result = clearance_sensor(strikes)

    if result == "ALARM":
        print("ALARM TRIGGERED!")
        break
    elif result == "SUCCESS":
        print("Identity Verified.")
        strikes = 0  # Reset strikes