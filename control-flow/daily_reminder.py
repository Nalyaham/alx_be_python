task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time = input("Is it time-bound? (yes/no)")

match priority:
    case "high":
        if time == "yes":
            print("Reminder: '", task, "' is a high prioirity task that requires immediate attention today!")
        if time == "no":
            print("Reminder '", task, "'  a high priority task. Consider completing it when you have free time.")
    case "low":
        if time == "yes":
            print("Note: '", task, "' is a low prioirity task that requires immediate attention today!")
            print("'", task, "'", "is a low prioirity task. Consider completing it when you have time.")
