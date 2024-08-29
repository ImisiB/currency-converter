while True:
    print()
    print("TO CONVERT DOLLARS TO NAIRA TYPE; 1")
    print("TO CONVERT DOLLARS TO POUNDS; 2")
    print("TO STOP THE PROGRAM TYPE; 3")
    option = input("          OPTION = ")
    print()
    
    def main():
        if option == "1":
            print("This a program that converts dollars to naira")
            print()
            dollars = eval(input("Enter the amount of dollars: "))
            naira = convert_to_naira(dollars)
            print("That is",naira , "in naira")
        elif option == "2":
            print("This is a program that converts dollars to pounds")
            dollar = eval(input("Enter the amount of dollars: "))
            pounds = dollar_to_pounds(dollar)
            print("That is ",pounds , "in naira")
        elif option == "3":
            print("Program ended")
            quit()
            
        else:
            print("Invalid number, please type 1 or 2")
    convert_to_naira = lambda dollars: dollars * 1590.11
    dollar_to_pounds = lambda dollar: dollar * 0.82
    main()
