import sys

def main():
    if len(sys.argv) != 2:
        print("none")
    else:
        expected_word = sys.argv[1]
        
        user_input = input("What was the parameter? ")
        
        if user_input == expected_word:
            print("Good job!")
        else:
            print("Nope, sorry...")

if __name__ == "__main__":
    main()

# python parameter_matching.py "Hello"