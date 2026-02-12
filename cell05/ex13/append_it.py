import sys

def main():
    params = sys.argv[1:]
    
    if len(params) == 0:
        print("none")
    else:
        for p in params:
            if not p.endswith("ism"):
                print(f"{p}ism")

if __name__ == "__main__":
    main()

# python append_it.py "parallel" "egoism" "human"