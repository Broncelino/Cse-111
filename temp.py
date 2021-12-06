while True:
        try:
            n = int(input("enter"))
            break
        except ValueError as val_err:
            print("please enter a valid file: ")