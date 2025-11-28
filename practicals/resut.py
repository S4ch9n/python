# ----------------------------------------------------------
# Student Management System
# Calculates Result, Attendance Status, Rewards & Eligibility
# ----------------------------------------------------------

# Input details from the user
name = input("Enter student name: ")

marks = float(input("Enter total marks obtained (out of 100): "))
attendance = float(input("Enter attendance percentage: "))
activities = input("Did student participate in extra activities? (yes/no): ").lower()

# Calculate Result (Pass/Fail)
if marks >= 40:
    result = "PASS"
else:
    result = "FAIL"

# Attendance Status
if attendance >= 75:
    attendance_status = "Good Attendance"
else:
    attendance_status = "Poor Attendance"

# Rewards based on performance
if marks >= 85 and attendance >= 90:
    reward = "Gold Star Award"
elif marks >= 70 and attendance >= 80:
    reward = "Silver Star Award"
elif marks >= 50 and attendance >= 75:
    reward = "Bronze Star Award"
else:
    reward = "No Reward"

# Equal Benefit Eligibility:
# Condition – student must PASS + attendance >= 75
if result == "PASS" and attendance >= 75:
    equal_benefit = "Eligible for Equal Benefit"
else:
    equal_benefit = "Not Eligible for Equal Benefit"

# Activity Bonus
if activities == "yes":
    activity_bonus = "Activity Bonus Granted"
else:
    activity_bonus = "No Activity Bonus"

# Final Output
print("\n----- STUDENT REPORT -----")
print("Name:", name)
print("Marks:", marks)
print("Attendance:", attendance, "%")
print("Result:", result)
print("Attendance Status:", attendance_status)
print("Reward:", reward)
print("Extra Activity:", activity_bonus)
print("Equal Benefit:", equal_benefit)
print("----------------------------")
