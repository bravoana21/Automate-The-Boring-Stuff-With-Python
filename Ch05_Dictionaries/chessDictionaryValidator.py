def isValidChessBoard(chessBoard):
    piece_count = {
        'bking': 0, 'wking': 0,
        'bpawn': 0, 'wpawn': 0,
        'b': 0, 'w': 0
    }
    valid_pieces = ['king', 'pawn', 'knight', 'bishop', 'rook', 'queen']
    valid_x_spaces = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    valid_y_spaces = ['1', '2', '3', '4', '5', '6', '7', '8']

    for position, piece in chessBoard.items():
        if not (position[0] in valid_y_spaces and position[1:] in valid_x_spaces):
            return False    # Spaces range from '1' to '8' and 'a' to 'h'
        
        if piece[0] not in 'bw' or piece[1:] not in valid_pieces:
            return False     # Piece name is valid
        
        piece_count[piece] = piece_count.get(piece, 0) + 1
        piece_count[piece[0]] += 1

        if piece in ['bking', 'wking'] and piece_count[piece] > 1:
            return False  # There's onnly one king for each player
        if piece in ['bpawn', 'wpawn'] and piece_count[piece] > 8:
            return False    # At most 8 pawns for each player
        if piece_count[piece[0]] > 16:
            return False    # At most 16 pieces for each player

    return piece_count['bking'] == 1 and piece_count['wking'] == 1


# Test Cases
chessBoard_1 = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(str(isValidChessBoard(chessBoard_1)) + ' 1')
chessBoard_2 = {'1h': 'bking', '2h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(str(isValidChessBoard(chessBoard_2)) + ' 2')  # Two bkings
chessBoard_3 = {'1z': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(str(isValidChessBoard(chessBoard_3)) + ' 3')  # 'z' out of range
chessBoard_4 = {'1h': 'bking', '6c': 'wqueen', '9g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(str(isValidChessBoard(chessBoard_4)) + ' 4')   # '9' out of range
chessBoard_5 = {'1h': 'bking', '61c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(str(isValidChessBoard(chessBoard_5)) + ' 5')   # '61' out of range
chessBoard_6 = {'1h': 'bking', '6c': 'wqueen', '2g': 'wknight', '5h': 'brook', '3e': 'wking'}
print(str(isValidChessBoard(chessBoard_6)) + ' 6')   # brook and wknight are considered
chessBoard_7 = {'6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(str(isValidChessBoard(chessBoard_7)) + ' 7')   # No bking
chessBoard_8 = {'1h': 'bking', '8g': 'bpawn', '7g': 'bpawn', '8f': 'bpawn', '6g': 'bpawn', '5g': 'bpawn', '4g': 'bpawn', '3g': 'bpawn', '2g': 'bpawn', '1g': 'bpawn', '3e': 'wking'}
print(str(isValidChessBoard(chessBoard_8)) + ' 8') # More pawns than allowed
chessBoard_9 = {'1h': 'bking', '7g': 'bpawn', '8f': 'bpawn', '6g': 'bpawn', '5g': 'bpawn', '4g': 'bpawn', '3g': 'bpawn', '2g': 'bpawn', '1g': 'bpawn', '3e': 'wking'}
print(str(isValidChessBoard(chessBoard_9)) + ' 9')  # 8 pawns
chessBoard_10 = {'1h': 'zking', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(str(isValidChessBoard(chessBoard_10)) + ' 10') # 'zking' doesn't belong to neither player
chessBoard_11 = {'1h': 'bking', '6c': 'wquen', '2g': 'wknight', '5h': 'brook', '3e': 'wking'}
print(str(isValidChessBoard(chessBoard_11)) + ' 11')   # 'wquen' is not a valid name of piece
chessBoard_12 = {'1h': 'bking', '7g': 'wpawn', '8g': 'wpawn', '6g': 'wpawn', '5g': 'wpawn', '4g': 'wpawn', '3g': 'wpawn', '2g': 'wpawn', '1g': 'wpawn',  '2a': 'wknight',  '2b': 'wbishop',  '2c': 'wrook',  '2d': 'wqueen',  '2e': 'wknight',  '2f': 'wbishop',  '2h': 'wrook',   '7h': 'wrook', '3e': 'wking'}
print(str(isValidChessBoard(chessBoard_12)) + ' 12')  # More pieces than allowed
chessBoard_13 = {'1h': 'bking', '7g': 'wpawn', '8g': 'wpawn', '6g': 'wpawn', '5g': 'wpawn', '4g': 'wpawn', '3g': 'wpawn', '2g': 'wpawn', '1g': 'wpawn',  '2a': 'wknight',  '2b': 'wbishop',  '2c': 'wrook',  '2d': 'wqueen',  '2e': 'wknight',  '2f': 'wbishop',  '2h': 'wrook', '3e': 'wking'}
print(str(isValidChessBoard(chessBoard_13)) + ' 13')  # 16 pieces