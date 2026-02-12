import sys

def main():
    if len(sys.argv) < 3:
        print("none")
    else:
        params = sys.argv[1:]
        
        for p in reversed(params):
            print(p)

if __name__ == "__main__":
    main()

# python aff_rev_params.py "Andy" "My name is" "Hello"