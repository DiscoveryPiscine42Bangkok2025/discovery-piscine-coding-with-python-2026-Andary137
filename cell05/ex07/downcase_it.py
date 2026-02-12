import sys

def main():
    if len(sys.argv) == 2:
        print(sys.argv[1].lower())
    else:
        print("none")

if __name__ == "__main__":
    main()

# python downcase_it.py "LUCIOLE"
# python downcase_it.py