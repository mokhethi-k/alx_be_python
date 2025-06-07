from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_date

date = display_current_datetime()
print(f"Current date and time: {date}")
def calculate_future_date(number_of_days):
    time_delta = timedelta(days = number_of_days)
    future_date = (datetime.now() + (time_delta)).strftime("%Y-%m-%d")
    print(f"Future date: {future_date}")

num_days = int(input("Enter the number of days to add to the current date: "))

calculate_future_date(num_days)