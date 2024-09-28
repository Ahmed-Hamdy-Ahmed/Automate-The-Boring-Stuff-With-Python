# Chess Dictionary Validator

def isValidChessBoard(chessBoard):
  checkChessBoard = {}
  validCessBoard = {
    '1a': 'bRook', '1b': 'bKnight', '1c': 'bBishop', '1d': 'bQueen',
    '1e': 'bKing', '1f': 'bBishop', '1g': 'bKnight', '1h': 'bRook',
    
    '2a': 'bPawn', '2b': 'bPawn', '2c': 'bPawn', '2d': 'bPawn',
    '2e': 'bPawn', '2f': 'bPawn', '2g': 'bPawn', '2h': 'bPawn',
    
    '3a': '', '3b': '', '3c': '', '3d': '', '3e': '', '3f': '', '3g': '', '3h': '',
    '4a': '', '4b': '', '4c': '', '4d': '', '4e': '', '4f': '', '4g': '', '4h': '',
    
    '5a': '', '5b': '', '5c': '', '5d': '', '5e': '', '5f': '', '5g': '', '5h': '',
    '6a': '', '6b': '', '6c': '', '6d': '', '6e': '', '6f': '', '6g': '', '6h': '',
    
    '7a': 'wPawn', '7b': 'wPawn', '7c': 'wPawn', '7d': 'wPawn',
    '7e': 'wPawn', '7f': 'wPawn', '7g': 'wPawn', '7h': 'wPawn',
    
    '8a': 'wRook', '8b': 'wKnight', '8c': 'wBishop', '8d': 'wQueen',
    '8e': 'wKing', '8f': 'wBishop', '8g': 'wKnight', '8h': 'wRook',
  }
  validCessBoardNum = {
    'bRook': 2, 'bBishop': 2, 'bKnight': 2, 'bQueen': 1, 'bKing': 1, 'bPawn': 8,
    'wRook': 2, 'wBishop': 2, 'wKnight': 2, 'wQueen': 1, 'wKing': 1, 'wPawn': 8
  }
  for k, v in chessBoard.items():
    if v != '':
      checkChessBoard.setdefault(v , 0)
      checkChessBoard[v] += 1

  for k, v in checkChessBoard.items():
    if checkChessBoard[k] != validCessBoardNum[k]:
      return False
  chessBoardkeys = True
  chessBoardValues = True
  pieces = 0
  for k,v in chessBoard.items():
    if v:
      if k not in validCessBoard.keys():
        chessBoardkeys = False
      if v not in validCessBoard.values():
        chessBoardValues = False
      pieces += 1
  if chessBoardValues and chessBoardkeys and pieces == 32:
    return True
  else:
    return False

valid_chess_board_1 ={
    '1a': 'bRook', '1b': 'bKnight', '1c': 'bBishop', '1d': 'bQueen',
    '1e': 'bKing', '1f': 'bBishop', '1g': 'bKnight', '1h': 'bRook',
    
    '2a': 'bPawn', '2b': 'bPawn', '2c': 'bPawn', '2d': 'bPawn',
    '2e': 'bPawn', '2f': 'bPawn', '2g': 'bPawn', '2h': 'bPawn',
    
    '3a': '', '3b': '', '3c': '', '3d': '', '3e': '', '3f': '', '3g': '', '3h': '',
    '4a': '', '4b': '', '4c': '', '4d': '', '4e': '', '4f': '', '4g': '', '4h': '',
    
    '5a': '', '5b': '', '5c': '', '5d': '', '5e': '', '5f': '', '5g': '', '5h': '',
    '6a': '', '6b': '', '6c': '', '6d': '', '6e': '', '6f': '', '6g': '', '6h': '',
    
    '7a': 'wPawn', '7b': 'wPawn', '7c': 'wPawn', '7d': 'wPawn',
    '7e': 'wPawn', '7f': 'wPawn', '7g': 'wPawn', '7h': 'wPawn',
    
    '8a': 'wRook', '8b': 'wKnight', '8c': 'wBishop', '8d': 'wQueen',
    '8e': 'wKing', '8f': 'wBishop', '8g': 'wKnight', '8h': 'wRook',
  }


print(isValidChessBoard(valid_chess_board_1))