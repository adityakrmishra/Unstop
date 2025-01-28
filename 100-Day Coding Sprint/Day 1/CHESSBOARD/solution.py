def chessboard(x):
  if (x[0] in 'aceg' and x[1] in '1357') or (x[0] in 'bdfh' and x[1] in '2468'):
    return 'Black'
  else:
    return 'White'
x=input()
print(chessboard(x))
