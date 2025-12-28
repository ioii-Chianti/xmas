import random
import time
import sys
import datetime

RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def get_lucky_date():
    """Generates a random date (MM/DD) within a year."""
    start_date = datetime.date(2024, 1, 1)
    end_date = datetime.date(2024, 12, 31)
    
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    
    random_number_of_days = random.randrange(days_between_dates + 1)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    
    return random_date.strftime("%m/%d")

def santa_lottery():
    print("\n⭐ Christmas Gift Exchange Lottery ⭐")

    # 1. Setup Input
    while True:
        try:
            people_str = input("Enter number of PARTICIPANTS: ")
            num_people = int(people_str)
            
            gift_str = input("Enter number of GIFTS: ")
            num_gifts = int(gift_str)

            if num_people > 0 and num_gifts > 0:
                if num_gifts < num_people:
                    print(f"Warning: {YELLOW}{num_people}{RESET} people but only {YELLOW}{num_gifts}{RESET} gifts!")
                    print("Some will get nothing. Type 'y' to continue.")
                    if input("Confirm? ").lower() != 'y': continue
                break
            print("Numbers must be > 0!")
        except ValueError:
            print("Invalid input!")

    # 2. Initialize Lottery Box
    lottery_box = list(range(1, num_gifts + 1))
    print(f"\nBox ready! {YELLOW}{len(lottery_box)}{RESET} tickets.")
    print("-" * 50)

    # 3. Main Round (Regular Exchange)
    print("\n⭐ ROUND 1: Regular Exchange ⭐")
    for i in range(1, num_people + 1):
        if len(lottery_box) == 0:
            print(f"No gifts left for Person #{YELLOW}{i}{RESET}!")
            break

        while True: # Drawing Loop (Redraw returns here)
            remaining = len(lottery_box)
            print(f"\nPerson No. {YELLOW}{i}{RESET} (Box: {YELLOW}{remaining}{RESET} left)")
            cmd = input("Press [Enter] to draw... (or 'q' to quit): ")
            if cmd.lower() == 'q': sys.exit()

            print("Shuffling...", end="", flush=True)
            time.sleep(0.5)
            
            candidate = random.choice(lottery_box)
            print(f"\rDrawn: [ No. {RED}{candidate}{RESET} ]       ")

            action = None
            while True:
                user_input = input("Confirm? (ok/r): ").strip().lower()
                
                if user_input == 'ok':
                    action = 'confirm'
                    break
                elif user_input == 'r':
                    action = 'redraw'
                    break
                else:
                    print(f"{RED}Invalid input! Please type 'ok' or 'r'.{RESET}")

            if action == 'redraw':
                print(f"Redrawing...")
                continue
            else:
                lottery_box.remove(candidate)
                print(f"Taken gift No. {RED}{candidate}{RESET}")
                break

    # 4. Bonus Round (If gifts are left)
    if len(lottery_box) > 0:
        print("\n" + "=" * 50)
        print(f"⭐ BONUS ROUND STARTED! ({YELLOW}{len(lottery_box)}{RESET} gifts left) ⭐")
        print("=" * 50)
        
        bonus_round_count = 1
        
        while len(lottery_box) > 0:
            print(f"\nBonus Gift #{YELLOW}{bonus_round_count}{RESET} (Total left: {YELLOW}{len(lottery_box)}{RESET})")
            
            # A. Generate Random Date
            print("Generating Lucky Birthday Date...", end="", flush=True)
            time.sleep(1)
            lucky_date = get_lucky_date()
            print(f"\rTarget Birthday: [ {RED}{lucky_date}{RESET} ]")
            
            print("(Please find the person with the closest birthday!)")
            input("Once identified, press [Enter] to draw...")

            # B. Draw the Gift
            print("Shuffling...", end="", flush=True)
            time.sleep(0.5)
            candidate = random.choice(lottery_box)
            print(f"\rBonus Winner gets: [ No. {RED}{candidate}{RESET} ]")
            
            # C. Verification
            action = None
            while True:
                user_input = input("Confirm? (ok/r): ").strip().lower()
                if user_input == 'ok':
                    action = 'confirm'
                    break
                elif user_input == 'r':
                    action = 'redraw'
                    break
                else:
                    print(f"{RED}Invalid input! Please type 'ok' or 'r'.{RESET}")

            if action == 'redraw':
                print("Resetting this bonus round...")
                continue
            
            lottery_box.remove(candidate)
            print(f"Bonus gift No. {RED}{candidate}{RESET} distributed!")
            bonus_round_count += 1

    print("\n" + "-" * 50)
    print("Merry Christmas! Event Finished.")

if __name__ == "__main__":
    santa_lottery()