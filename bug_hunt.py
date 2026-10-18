count = 1
total = 0

# BUG: Added the missing colon to the while statement.
# BUG: Changed < 5 to <= 5 so the loop includes 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Used an f-string to print the integer correctly.
print(f"Sum of 1 to 5 is: {total}")
