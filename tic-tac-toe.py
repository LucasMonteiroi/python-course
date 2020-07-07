import random, copy

def drawBoard(board) :
    # This function will print the board it was passes

    # The board is a list with 10 string representing the board (ignore index 0)
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def inputPlayerLetter() :
    letter = ''
    while not (letter == 'X' or letter == 'O') :
        print('Do you want to be X or O ?')
        letter = input().upper()
    
    if letter == 'X' :
        return ['X', 'O']
    else :
        return ['O', 'X']

def whoGoesFirst() :
    if random.randint(0, 1) == 0 :
        return 'computer'
    else :
        return 'player'

def playAgain() :
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move) :
    board[move] = letter

def isWinner(bo, le) :
    return ((bo['top-L'] == le and bo['top-M'] == le and bo['top-R'] == le) or
    (bo['mid-L'] == le and bo['mid-M'] == le and bo['mid-R'] == le) or
    (bo['low-L'] == le and bo['low-M'] == le and bo['low-R'] == le) or
    (bo['top-L'] == le and bo['mid-L'] == le and bo['low-L'] == le) or 
    (bo['top-M'] == le and bo['mid-M'] == le and bo['low-M'] == le) or
    (bo['top-R'] == le and bo['mid-R'] == le and bo['low-R'] == le) or
    (bo['top-L'] == le and bo['mid-M'] == le and bo['low-R'] == le) or
    (bo['top-R'] == le and bo['mid-M'] == le and bo['low-L'] == le))

def isSpaceFree(board, move) :
    return board[move] == ' '

def getPlayerMove(board) :
    move = ' '
    while move not in 'top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R'.split() or not isSpaceFree(board, move) :
        print('What is your next move? (top-, mid-, low-, & L, M, R)')
        move = input()
    return move

def chooseRandomMoveFromList(board,  movesList) :
    possibleMoves = []
    for i in movesList :
        if isSpaceFree(board, i) :
            possibleMoves.append(i)
    
    if len(possibleMoves) != 0 :
        return random.choice(possibleMoves)
    else :
        return None

def getComputerMove(board, computerLetter) :
    if computerLetter == 'X' :
        playerLetter = 'O'
    else :
        playerLetter = 'X'

    for i in 'top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R'.split() :
        dupe = copy.copy(board)
        if isSpaceFree(dupe, i) :
            makeMove(dupe, computerLetter, i)
            if isWinner(dupe, computerLetter) :
                return i
    
    for i in 'top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R'.split() :
        dupe = copy.copy(board)
        if isSpaceFree(dupe, i) :
            makeMove(dupe, playerLetter, i)
            if isWinner(dupe, playerLetter) :
                return i
    
    move = chooseRandomMoveFromList(board, ['top-L', 'top-R', 'low-L', 'low-R'])
    if move != None :
        return move
    
    if isSpaceFree(board, 'mid-M') :
        return 'mid-M'
    
    return chooseRandomMoveFromList(board, ['top-M', 'low-M', 'mid-L', 'mid-R'])

def isBoardFull(board) :
    for i in 'top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R'.split() :
        if isSpaceFree(board, i) :
            return False
    return True

print('Welcome to Tic Tac Toe!')

while True :
    # Reset the board
    theBoard = {
        'top-L': ' ',
        'top-M': ' ',
        'top-R': ' ',
        'mid-L': ' ',
        'mid-M': ' ',
        'mid-R': ' ',
        'low-L': ' ',
        'low-M': ' ',
        'low-R': ' '
    }

    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying : 
        if turn == 'player' :
            print('Now it is your turn')
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
           
            if isWinner(theBoard, playerLetter) :
                drawBoard(theBoard)
                print('Hooray, You have won the game')
                gameIsPlaying = False
            else :
                if isBoardFull(theBoard) :
                    drawBoard(theBoard)
                    print('The game is tie')
                    break
                else :
                    turn = 'computer'
        else :
            print('It is computer turns')
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            
            if isWinner(theBoard, computerLetter) :
                drawBoard(theBoard)
                print('The computer beaten you! You loose the game')
                gameIsPlaying = False
            else :
                if isBoardFull(theBoard) :
                    drawBoard(theBoard)
                    print('The game is tie')
                    break
                else :
                    turn = 'player'
        
    if not playAgain() :
        break