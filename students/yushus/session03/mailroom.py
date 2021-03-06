import sys  # imports go at the top of the file
import random

donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ("Elon Musk", [250000, 15000])
            ]

prompt = "\n".join(("Welcome to mailroom bot!",
          "Please choose from below options:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - quit",
          ">>> "))

# sort by the total amount of donated
def sort_key(donor):
    return sum(donor[1])

def print_donor():
    donors = [x[0] for x in donor_db]
    donors_list = "\n".join(donors)
    print(donors_list)

def print_email(name, amount):
    letter = '''
        Dear {name},
        Thank you for your generous donation of ${amount}. Your kindness is really making the world different!

        Sincerely,
        Mailroom Bot
        '''
    print(letter.format(name=name, amount=amount))

def send_a_thank_you():
    
    # maintain a donor list which contains donor names only
    donors = [x[0] for x in donor_db]
    name = ""

    while True:
        name = input("Who do you want to send this to, use a full name: ")
        if name == 'list':
            print_donor()
        elif name not in donors:
            donor_db.append((name, []))
            break
        else:
            break

    amount = float(input("How much do you want to donate? "))

    for donar_name, amounts in donor_db:
        if donar_name == name:
            amounts.append(amount)

    print_email(name, amount)

    return



def exit_program():
    print("Bye!")
    sys.exit()  # exit the interactive script

def main():
    while True:
        response = input(prompt)  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        if response == "1":
            send_a_thank_you()
        elif response == "2":
            create_a_report()
        elif response == "3":
            exit_program()
        else:
            print("Not a valid option!")


if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()