from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.datetime.now()
    print("The Current date and time: ", current_date.strftime("%Y-%m-%d %H: %M: %S"))
    return current_date

def calculate_future_date(current_date):
        number_of_days = int(input("Enter the number of days: "))
        future_date = current_date + datetime.timedelta(days = number_of_days)
        print("Future date is: ", future_date.strftime("%Y-%m-%d %H: %M: %S"))
    
    
def main():
    current_date = display_current_datetime()
    calculate_future_date(current_date)
    
if __name__ == "__main__":
    main()
