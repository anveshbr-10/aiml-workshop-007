sections = {'A': [["🪑"]*5 for _ in range(10)],   'B': [["🪑"]*10 for _ in range(10)],  'C': [["🪑"]*5 for _ in range(10)],   }
print("   ------------------🎫 WELCOME TO Bharat AUDITORIUM 🎫----------------\n")
print("     Section A" + " " * 15 + "   Section B" + " " * 15 + " Section C")
for row_index in range(10):
    row_a = " ".join(sections['A'][row_index])
    row_b = " ".join(sections['B'][row_index])
    row_c = " ".join(sections['C'][row_index])
    print(f"{row_index} {row_a}   {row_index} {row_b}   {row_index} {row_c}")
section = input("\nEnter section (A, B, C): ").upper()
if section not in sections:
    print("\nSection not available.")
    exit()
row = int(input("Enter row number (0-9): "))
if not (0 <= row < 10):
    print("\nRow not available")
    exit()
col = int(input(f"Enter column number (0-{len(sections[section][0]) - 1}): "))
if not (0 <= col < len(sections[section][0])):
    print("\nColumn not available.")
    exit()
if sections[section][row][col] == "🪑":
    sections[section][row][col] = "☑️ "
    print(f"\nSeat booked: Section {section} Row {row} Seat {col}")
else:
    print("\nSeat already booked!")
print("\nUpdated seating layout:\n")
for i in range(10):
    row_a = " ".join(sections['A'][i])
    row_b = " ".join(sections['B'][i])
    row_c = " ".join(sections['C'][i])
    print(f"{i} {row_a}   {i} {row_b}   {i} {row_c}")
