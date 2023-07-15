# Read the number of test cases
T = int(input("enter the values of X and Y"))

# Iterate through each test case
for _ in range(T):
    # Read the numbers on the dice
    X, Y = map(int, input().split())
    
    # Calculate the sum of the numbers
    dice_sum = X + Y
    
    # Check if the sum satisfies the constraint
    if dice_sum <= 6:
        print("NO")
    else:
        print("YES")
