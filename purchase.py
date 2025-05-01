# this code uses functions , loops and conditionals 
# *143# for purchasing data and more

import random

def show_main():
    print("PLEASE SELECT")
    print("1.Buy Airtime")
    print("2.Buy Data")
    print("3.Buy Private Wi-Fi")
    print("4.Buy TikTok Data")
    print("5.Buy Facebook Data")
    print("6.Exit")

def buy_Airtime():
    amount = input("Enter amount:")
    print(f"Airtime of {amount} purchased successfully!\n")

def buy_data():
    general_data = {"1GB": "5","2GB": "8", "5GB": "9", "10GB": "13"}
    print("available general data:")
    for data, price in general_data.items():
         print(f"{data}-{price}")

    choice =input("please choose a general data (e.g, 1GB, 2GB, 5GB, 10GB):")
    if choice in general_data:
        print(f"general data {choice} of {general_data[choice]} purchased successfully!\n")
    else:
        print("lnvalid choice, please try again.\n")

def buy_private_wifi():
    print("private wi-fi purchased successfully!\n")

def buy_TikTok_data():
    TikTok_data = {"1GB":"4", "3GB":"9", "5GB":"14"}
    print("available TikTok data:")
    for data, price in TikTok_data.items():
        print(f"{data}-{price}")
    
    choice = input("please choose a tiktok data(e.g, 1GB, 3GB, 5GB):")
    if choice in TikTok_data:
        print(f"TikTok data {choice} of {TikTok_data[choice]}purchased successfully!")
    else:
        print("lnvalid choice,please try again.")

def buy_facebook_data():
    facebook_data = {"1GB":"3", "3GB":"7", "5GB":"12"}
    print("available facebook data:")
    for data, price in facebook_data.items():
        print(f"{data}-{price}")

    choice = input("please choose a facebook data(e.g,1GB, 3GB, 5GB):")
    if choice in facebook_data:
        print(f"facebook data{choice}of {facebook_data[choice]} purchased successfully!\n")
    else:
        print("lnvalid choice,please try again.\n")

def main():
    while True:
        show_main()
        try:
            selection = int(input("please select an option:"))
            if selection == 1:
                buy_Airtime()
            elif selection == 2:
                buy_data()
            elif selection == 3:
                buy_private_wifi()
            elif selection == 4:
                buy_TikTok_data()
            elif selection == 5:
                buy_facebook_data()
            elif selection == 6:
                print("thank you for using our service.")
                break
            else:
                print("lnvalid option, please choose again.\n")
        except ValueError:
                print("please enter a valid number.\n")

if __name__ == "__main__":
    main()            
