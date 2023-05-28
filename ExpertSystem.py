def evaluate_performance():
    print("Welcome to the Employee Performance Evaluation System.")
    name = input("Enter the employee's name: ")
    age = int(input("Enter the employee's age: "))
    years_of_experience = int(input("Enter the employee's years of experience: "))
    performance_score = int(input("Enter the employee's performance score (out of 100): "))

    if age < 25:
        print("Employee is too young for evaluation.")
    elif years_of_experience < 5:
        print("Employee does not meet the minimum experience requirement.")
    elif performance_score >= 80:
        print(f"Congratulations, {name}! You have achieved a high performance rating.")
    elif performance_score >= 60:
        print(f"{name}, your performance is satisfactory.")
    else:
        print(f"Sorry, {name}, your performance needs improvement.")


# Start the employee performance evaluation system
evaluate_performance()
