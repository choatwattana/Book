first_question = input("Did you get vaccinate?(yes or no )  " )
second_question = input("Have you infected before? (yes or no ) ")
if first_question == "no" and second_question == "no":
    print("You will get 2 pfizer ")
elif first_question == "no" and second_question == "yes":
    print("you wil get only 1 dose of pfizer ")
else :
    print("Please,answer this question")
    first_dose = input("what is your first dose?(sv az or si) ")
    second_dose = input("what is your second dose?(sv , az , si or non) ")
    third_dose = input("what is your third dose?( sv , az , si or non ")
    if first_dose == "sv" and second_dose == "sv" and third_dose == "non":
        print("you will get 1 pfizer for next dose ")
    elif  first_dose == "si" and second_dose == "si" and third_dose == "non":
        print("you will get 1 pfizer for next dose")
    elif first_dose == "sv" and second_dose == "non" and third_dose == "non":
        print("you will get 1 pfizer for next dose ")
    elif first_dose == "az" and second_dose == "non" and third_dose == "non":
        print("you will get 1 pfizer for next dose ")
    elif first_dose == "si" and second_dose == "non" and third_dose == "non":
        print("you will get 1 pfizer for next dose ")
    elif first_dose == "sv" or  "az" and second_dose == "sv"or "az" and third_dose == "az"or"non" :
        print("you won't get any of pfizer")
