# we have a phone shop and some phones with some problems to repair
import re
import json
import os
import sys

# ma tooye in tamrin ye seri code ro mudulise mikonim: sakhtane function va bordane oon kodha dakhele function
phones_list = []
# lab 10: making some changes with os files
# avalin bar ke run mikonim mige ke file phones.json vojood nadare. che mikonim?
# az try and except mishe estefade kard

# raveshe dge az os estefade

# inja function load phones ro misazim
def load_phones(phones_file):
    '''loads the phone from the given file'''
    # ye global list dorost mikonim va ye function dge misazim
    global phones_list

    if os.path.isfile("phones.file"):
        phone_file = open("phones.file")
        phone_json_data = phone_file.read()

        phones_list.extend(json.loads(phone_json_data))
        phone_file.close()
        return True
    return False

def save_phones(phones_file):
    '''saves the phones to the given file'''
    global phones_list
    phone_file = open("phones.file", "w")
    phone_json = json.dumps(phones_list, indent=4)
    phone_file.write(phone_json)
    phone_file.close

# alan vaghti run bokonim codo azmoon mikhad kamel hame chiz ro
# type bokonim. Hala mikhaym yekam hooshmandesh bokonim pas miyaym bad az input ha validatesh ro
# mizarim bejaye inke poshte sare ham input haro bezarim. pas input migirim va validatesh mikonim


def get_add_phone_inputs():
    """gets inputs for a new phone to be repairs and validates them """
    repair_id = input("Enter repair ID: ")
    if re.search("^\d+$", repair_id) is None:
        raise ValueError("repair ID must be a number")


    make = input("Enter make: ")
    if re.search("^[a-zA-Z]+$", make) is None:
        # make
        # exact match and letters only
        raise ValueError("Make must be all letters")

    model = input("Enter model: ")
    if re.search("^[a-zA-Z0-9]+$", model) is None:
        raise ValueError("Model must be all letters or numbers")

    problem = input("Enter problem: ")
    if re.search("^[a-zA-Z]+$", problem) is None:
        raise ValueError("Price must be a valid currency")

    price = input("Repair price: ")
    if re.search("^[0-9]+.[0-9]{2}$", price) is None:


        raise ValueError("Price must be a valid currency")

    return repair_id ,make, model, problem, price




def main():
    # agar nakham hamishe dataye my phone ro store bokonam tooye phones.json az sys estefade
    # va az def loadphones ro misazim
    if len(sys.argv) != 2:
        print("Must specify the name of the phones json file")
    phones_file = sys.argv[1]

    quit = False

    is_phones_loaded = load_phones(phones_file)
    if not is_phones_loaded:
        print("No existing phones found")

    # try:
    #     phone_file = open("phones.json")
    #     phone_json_data = phone_file.read()
    #
    #     phones_list.extend(json.loads(phone_json_data))
    #     phone_file.close()
    # except:
    #     print("phones.json doesn't exist")

    # if os.path.isfile("phones.json"):
    #     phone_file = open("phones.json")
    #     phone_json_data = phone_file.read()
    #
    #     phones_list.extend(json.loads(phone_json_data))
    #     phone_file.close()
    # else:
    #     print("phones.json doesn't exist")

    while not quit:
        user_selection = input("Add a phone(a), list phones(l), finish repair(f), quit(q): ")

        try:
            if user_selection == "a":

                # now we want to handle the exceptions so
                # try:



                # make = input("Enter make: ")
                # model = input("Enter model: ")
                # problem = input("Enter problem: ")
                # price = input("Repair price: ")
                #
                # # make
                # # exact match and letters only
                # is_valid_make = False
                # if re.search("^[a-zA-Z]+$", make):
                #     is_valid_make = True
                #
                # is_valid_model = False
                # if re.search("^[a-zA-Z0-9]+$", model):
                #     is_valid_model = True
                #
                # is_valid_problem = False
                # if re.search("^[a-zA-Z]+$", problem):
                #     is_valid_problem = True
                #
                #     # we want to make sure that it is a valid price
                # is_valid_price = False
                # if re.search("^[0-9]+.[0-9]{2}$", price):
                #
                #     is_valid_price = True

                repair_id, make, model, problem, price = get_add_phone_inputs()
            # vaghti k code bala ke commentesh kardi ro bordi too ye function jadid>>>
            # we miss a validation now. let us change that function to raise exceptions
            # pas is valid ha ro pak mikonim az zire code va try va except minevisim vasashoon

            # if is_valid_make and is_valid_model and is_valid_problem and is_valid_price:
                phone = {"repair_id": repair_id, "make": make, "model": model, "problem": problem, "price": price}
                phones_list.append(phone)
                phone_file = open("phones.json", "w")
                phone_json = json.dumps(phones_list, indent=4)
                phone_file.write(phone_json)
                phone_file.close()
        # else:
        #     print("Invalid data Entered. Phone not added.")



                save_phones(phones_file)
        # except ValueError as e:
        #     print("Could not add the phone...")
        #     print(str(e))


            elif user_selection == "l":
                print("There are %d phones in for repair" % len(phones_list))
                for phone in phones_list:
                    print("%d: %s %s with this problem: %s (Price: $%.2f" %
                          (int(phone["repair_id"]), phone["make"], phone["model"], phone["problem"], phone["price"]))

                    # I want to add my option to finish that repair
            elif user_selection == "f":
                repair_id = input("Enter Repair ID to complete: ")
                if re.search("^\s+$", repair_id) is None:
                    raise ValueError("Repair ID must be numeric")
                is_found = False
                for phone in phones_list:
                    if phone["repair_id"] == repair_id:
                        phones_list.remove(phone)
                        is_found = True
                        break
                if not is_found:
                    print("Couldn't find the repair to complete")
                else:
                    print("Repair %s successfully completed" % repair_id)
            elif user_selection == "q":
                # phone_file = open("phones.json", "w")
                # phone_json = json.dumps(phones_list, indent=4)
                # phone_file.write(phone_json)
                # phone_file.close

                print("Quitting the Phone Repair Program")

                quit = True
            else:
                # I should write the phones list to the file
                save_phones(phones_file)
                print("Invalid Selection. Try Again.")
        except ValueError as e:
            print("An error occurred: %s" % str(e))



if __name__ == "__main__":
    main()



