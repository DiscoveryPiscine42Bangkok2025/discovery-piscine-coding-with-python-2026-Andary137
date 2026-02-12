def checkmate(board): #แปลง board จากstringเป็น list #เพื่อให้เข้าถึงตำแหน่งแต่ละช่องด้วย index   
    board = board.splitlines()
    size = len(board)

    for row in board:
        if len(row) != size:
            return "Error"
       # เราตรวจว่าทุกแถวต้องยาวเท่ากันถ้าไม่เท่ากันแสดงว่าไม่ใช่ square board จึง return "Error"

# หาตำแหน่งของ king
    king_pos = None
    for  i in range(size):
        for j in range(size):
            if board[i][j] == 'K':
                king_pos = (i, j)
                break

    if not king_pos:
            print("Fail")
            return "Error"

    x , y = king_pos
# ฟังก์ชันช่วยเช็คทิศทาง
    def check_direction(dx, dy, pieces):
        i, j = x + dx, y + dy
        while 0 <= i < size and 0 <= j < size:
            if board[i][j] != ".":
                return board[i][j] in pieces
            i += dx
            j += dy
        return False
 # เช็ค Rook / Queen → แนวตั้ง+แนวนอน
    if (check_direction(1, 0, "RQ") or
        check_direction(-1, 0, "RQ") or
        check_direction(0, 1, "RQ") or
        check_direction(0, -1, "RQ")):
        print("Success")
        return
  # เช็ค Bishop / Queen → แนวทแยง
    if (check_direction(1, 1, "BQ") or
        check_direction(1, -1, "BQ") or
        check_direction(-1, 1, "BQ") or
        check_direction(-1, -1, "BQ")):
        print("Success")
        return

    # เช็ค Pawn
    for dx, dy in [(-1, -1), (-1, 1)]:
        i, j = x + dx, y + dy
        if 0 <= i < size and 0 <= j < size and board[i][j] == "P":
            print("Success")
            return

    print("Fail")