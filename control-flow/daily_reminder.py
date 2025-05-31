task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"'{task}' is a high priority task that requires immediate attention today!")
    case "low":
        if time_bound == "no":
            print(f"'{task}' is low priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print(f"'{task}' is a medium priority task. You can do it after completing high priority task.")