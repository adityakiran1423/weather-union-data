from utils import temperature
from utils import humidity
from utils import wind
from utils import rain_accumulation


def day_or_month_handler():
    print("Enter 1. for day data and 2. for month data")

    while True:
        day_or_month_choice = int(input(""))
        print()
        if day_or_month_choice==1:
            print("You have chosen : Day data \n")
            break
        elif day_or_month_choice==2:
            print("You have chosen : Month data \n")
            break
        else:
            print("Please enter only 1 or 2")

    arg = choice_handler(day_or_month_choice)

def choice_handler(day_or_month_choice):
    choice= 0
    valid_choice_list=[1,2,3,4,5,6,7]

    if day_or_month_choice==1:
        # day
        print("1. Max temperature for the day")
        print("2. Minimum temperature for the day")
        print("3. Maximum humidity for the day")
        print("4. Minimum humidity for the day")
        print("5. Maximum wind speed for the day")
        print("6. Minimum wind speed for the day")
        print("7. Rain accumulation for the day")
        print()
        print("Enter your choice")
        while True:
            choice=int(input())
            print()
            if choice in valid_choice_list:
                if choice==1:
                    temperature.temperature(day_or_month_choice)
                    break
                elif choice ==2:
                    temperature.temperature(day_or_month_choice)
                    break
                elif choice ==3:
                    humidity.humidity(day_or_month_choice)
                    break
                elif choice ==4:
                    humidity.humidity(day_or_month_choice)
                    break
                elif choice ==5:
                    wind.wind(day_or_month_choice)
                    break
                elif choice ==6:
                    wind.wind(day_or_month_choice)
                    break
                elif choice ==7:
                    rain_accumulation.rain_accumulation(day_or_month_choice)
                    break
            else:
                print("Please enter a valid option (enter options from only 1 to 7)")
    else:
        # month
        print("1. Max temperature for the month")
        print("2. Minimum temperature for the month")
        print("3. Maximum humidity for the month")
        print("4. Minimum humidity for the month")
        print("5. Maximum wind speed for the month")
        print("6. Minimum wind speed for the month")
        print("7. Rain accumulation for the month")
        print()
        print("Enter your choice")
        while True:
            choice=int(input())
            print()
            if choice in valid_choice_list:
                if choice==1:
                    temperature.temperature(day_or_month_choice)
                    break
                elif choice ==2:
                    temperature.temperature(day_or_month_choice)
                    break
                elif choice ==3:
                    humidity.humidity(day_or_month_choice)
                    break
                elif choice ==4:
                    humidity.humidity(day_or_month_choice)
                    break
                elif choice ==5:
                    wind.wind(day_or_month_choice)
                    break
                elif choice ==6:
                    wind.wind(day_or_month_choice)
                    break
                elif choice ==7:
                    rain_accumulation.rain_accumulation(day_or_month_choice)
                    break
            else:
                print("Please enter a valid option (enter options from only 1 to 7)")

    return choice

def main():
    day_or_month_handler()

if __name__=="__main__":
    main()
