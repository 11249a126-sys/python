t1 = float(input("Enter Test 1 mark: "))
t2 = float(input("Enter Test 2 mark: "))
t3 = float(input("Enter Test 3 mark: "))

# Calculate all possible two-test averages
avg1 = (t1 + t2) / 2
avg2 = (t1 + t3) / 2
avg3 = (t2 + t3) / 2

# Find the best (highest) average
best_avg = max(avg1, avg2, avg3)

# Display the result
print("The best average of two tests is:", best_avg)
