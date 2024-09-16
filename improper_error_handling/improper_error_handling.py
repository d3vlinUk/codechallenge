def error_handling_pass():
    number = input("Enter number:\n")
    try:
        int(number)
    except Exception:
        pass

def error_handling_continue():
    number = input("Enter number:\n")
    for i in range(10):
        try:
            int(number)
        except Exception:
            continue