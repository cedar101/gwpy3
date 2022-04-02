while True:
    formula = input("Please enter a chemical formula: ")
    if formula == "quit":
        print("프로그램을 종료합니다.")
        break
    if formula == "H2O":
        print("Water")
    elif formula == "NH3":
        print("Ammonia")
    elif formula == "CH4":
        print("Methane")
    else:
        print("Unknown compound")
