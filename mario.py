
# main()
def main():
    h = get_h()
    for i in range(h):
        print("#")

def get_h():
    while True:
        try:
            n = int(input("Height: "))
            if n > 0:
                return n  # Return only if n is greater than 0
            else:
                print("Height must be a positive integer.")
        except ValueError:
            print("Not an integer.")

main()
