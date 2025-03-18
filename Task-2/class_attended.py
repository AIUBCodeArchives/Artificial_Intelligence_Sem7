total_number_working_days = int(input("Enter the total number of working days: "))
total_number_days_absent = int(input("Enter the total number of days for absent: "))

percentage = ((total_number_working_days-total_number_days_absent)/total_number_working_days)*100;

print(percentage)
if percentage < 75:
    print("you will not be siting in the exam")
else: 
    print("you will be siting in the exam")
