
from checkmate import checkmate

def main():
    boards = [
#1
"""\
R...
.K..
..P.
....\
""", 
#2
"""\
..
.K\
""",
#3
"""\
B...
.K..
....
....\
""",  
#4
"""\
Q...
.K..
....
....\
""",
#5
"""\
....
.P..
.K..
....\
""",
#6
"""\
....
.P..
K...
....\
""",
#7
"""\
.k..
.P..
....
....\
""",
#8
"""\
........
.Q...P..
.....K..
........
........
........
.....R..
........\
"""
    ]
    for idx, b in enumerate(boards, start=1):
        print(f"\nTest case {idx}:")
        print(b)
        if checkmate(b) == "Error":
            print("Error")
            
if __name__ == "__main__":
    main()