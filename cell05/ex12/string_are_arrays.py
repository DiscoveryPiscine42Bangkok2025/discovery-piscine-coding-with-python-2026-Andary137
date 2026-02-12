import sys

def main():
    if len(sys.argv) != 2:
        print("none")
        return
    text = sys.argv[1]
    result = ""
    for char in text:
        if char == 'z':
            result += 'z'
    if result == "":
        print("none")
    else:
        print(result)

if __name__ == "__main__":
    main()

# python string_are_arrays.py "Zaz visits the zoo with Zazie"