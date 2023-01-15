import random

def setUpGame():
    global activeBoundaries,whichBoundary,numBoundaries, mode, whichKey, asciList
    getUserName = True
    startPlay = False
    whichBoundary = -1                                                                                                                                                                                                                                                                                                                                                  #Turns off all other click areas until game is ready to start except for Start
    activeBoundaries = [ True for i in range( numBoundaries ) ]

def showGameState ( ):
    global whichBoundary, cornerPointX, menuBarHeight, playAreaWidth, playAreaHeight
    global board, numRows, numCols,  playerInfo
    global boardImage, diceImage, bannerImage, scalingFactor, diceValue

    fill ( 255 )
    rect( cornerPointX, menuBarHeight, playAreaWidth, playAreaHeight )
    image(boardImage, 0, 0, scalingFactor * numCols, scalingFactor * numRows)
    image(bannerImage, scalingFactor * numCols, 0, scalingFactor, scalingFactor * numRows)
    image(turtleImage, playerInfo[1][1] * scalingFactor, playerInfo[1][2] * scalingFactor, scalingFactor, scalingFactor)
    image(hareImage, playerInfo[0][1] * scalingFactor, playerInfo[0][2] * scalingFactor, scalingFactor, scalingFactor)
    image (menuBarImage, menuBarX, menuBarY, menuBarWidth, menuBarHeight)
    image(diceImage,600,400,600,100)
    return    
    
def setup():
    global board, playerTurn, numRows, numCols, gameOver, playerInfo,numBoundaries
    global boardImage, diceImage, bannerImage, scalingFactor, diceValue, turtleImage, hareImage
    global canvasWidth, canvasHeight, cornerPointX, cornerPointY, gScore, pScore
    global upperBoundary, bottomBoundary, leftBoundary, rightBoundary
    global menuBarImage, menuBarWidth, menuBarHeight, menuBarX, menuBarY, menuItemWidth, menuItemHeight
    global playAreaWidth, playAreaHeight, validLocation, startX, startY
    global allBoundaries, whichBoundary, removeBoundary, activeBoundaries, numBoundaries    
    global startChosen, helpChosen, scoreChosen, resetGame, numMenuItems,helpImage,diceBound, mode
    global getUserName, userName, charLimit, acceptedChars, whichKey, fontSize, fontColor, terminateInput, startPlay, chosePlay, choseResetGame,activeBoundaries
    global whichKey, asciList, controlKeys, nameIn, nameLimit, nameCount, mode, nameCharCount

    size(700, 600)    
    
    charLimit = 15
    terminateInput = "0"
    userName = ""
    whichKey = ''
    asciList = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0"
    fontSize = 24
    fontColor = 200
    nameIn = ""
    nameLimit = 15
    nameCount = 0
    nameCharCount = 0
    background( 200, 20, 20 )
    fill( 250, 250, 250 )
    textSize ( 20 )
    text( "Enter Player 1 name > ", 100, 300 )
    text( "Enter Player 2 name > ", 100, 400 )
    text("Welcome to Snakes and Ladders" , 200, 100)
    text("Press 0 once you're done entering name and then again to start!", 50, 200)
    mode = "Start"
    
    
    
    
    menuBarImage = loadImage("menu.png")
    canvasWidth = 700 
    canvasHeight = 600
    cornerPointX = 0 
    cornerPointY = 0
        
    menuBarWidth = canvasWidth
    menuBarHeight = 100
    menuBarX = 0 
    menuBarY = 500
    menuItemWidth = menuBarWidth // 4
    menuItemHeight = menuBarHeight
    numMenuItems = 4
    
    startLocX = menuBarX
    startLocY = menuBarY
    
    whichBoundary=-1
    allBoundaries = []                                        

    removeBoundary = False                 
    for i in range ( numMenuItems ):
        upperLeft = [ startLocX, startLocY ]                                        
        lowerRight = [ startLocX + menuItemWidth, startLocY + menuItemHeight ]
        clickBoundary = [ upperLeft, lowerRight ]
        allBoundaries.append( clickBoundary )
        startLocX += menuItemWidth   
    numBoundaries = len( allBoundaries )    
    startChosen = 0
    helpChosen = 1
    scoreChosen = 2
    resetGame = 3
    menuBar = 3
    
    playAreaWidth = canvasWidth
    playAreaHeight = canvasHeight - menuBarHeight 

    diceHeight = 100
    diceWidth = 100
    upperBoundary = menuBarHeight + diceWidth /2 - 1
    bottomBoundary = canvasHeight - diceHeight/2 - 1
    leftBoundary = cornerPointX + diceWidth/2 - 1
    rightBoundary = canvasWidth - diceWidth/2 - 1
                                                                            
    
    setUpGame()   
    
    diceValue = 0
    diceBound= [[600,400],[699,499]] 

    scalingFactor = 100

    numCols = 6
    numRows = 5
    
    playerTurn = False
    
    gameOver = numCols * numRows
    
    board = [i for i in range(numRows * numCols + 7)]
    board[3] = 22
    board[5] = 8
    board[11] = 26
    board[20] = 29
    board[17] = 4
    board[19] = 7
    board[21] = 9
    board[27] = 1
    board[31] = 30
    board[32] = 30
    board[33] = 30
    board[34] = 30
    board[35] = 30
    
    boardImage = loadImage("board.PNG")
    diceImage = loadImage("dice.png")
    bannerImage = loadImage("banner.png")
    turtleImage = loadImage("player1.png")
    hareImage = loadImage("player2.png")
    helpImage= loadImage("helpScreen.png")
    
    playerInfo = [[0, 0, 400, scalingFactor, 0, ""],[0, 0, 400, scalingFactor, 0, ""]]


def saveHighscore():
    Scores = open("Scores.txt", w)
    Scores.append(playerInfo[0][4])
    Scores.append(playerInfo[1][4])
      #readHighscore=open("Highscore.txt",r)
#     currentHighScores=open(Highscores,a)
#     readHighscore=open("Highscore.txt",r)
#     currentHighScores=open(Highscores,a)
#     if readHighscores.read(1):
#         currentHighScores.write("/n"+playerName+","+str(score)
#     else:
#         currentHighScores.write(playerName+","+(score)
#     readHighscore.close()
#     current_highscores.close()
# def getHighScores():
#     allHighscores=[]
#     for value in open ("Highscore.txt",r):
#         allHighscores.append(value.split(","))
#     for value in allHighscores:
#         value[1]=int(value[1])
# def bubbleSort(List)                           
# for i in range(len(the_list)-1):
#         if the_list[i][item_num] > the_list[i+1][item_num]:
#             the_list[i], the_list[i+1] = the_list[i+1], the_list[i]

#     if all(the_list[i][item_num] <= the_list[i+1][item_num] for i in range(len(the_list)-1)):
#         sorted_highscores = the_list
#         return List(0,9)

   
    
def scoreBoard():
            background( 200, 20, 20 )
            fill( 250, 250, 250 )
            textSize ( 30 )
            textAlign(CENTER)
            text("Scoreboard" , 320, 50)
            text(playerInfo[0][5] , 250, 300) 
            text(playerInfo[0][4] , 320, 300)
            text(playerInfo[1][4] , 320, 400)  
            text(playerInfo[1][5] , 250, 400)
def draw():
    global board, playerTurn, numRows, numCols, gameOver, playerInfo,helpImage, gScore, pScore
    global boardImage, diceImage, bannerImage, scalingFactor, diceValue,whichBoundary, mode, whichKey, asciList
    global whichKey, asciList, controlKeys, nameIn, nameLimit, nameCount, mode, nameCharCount
    
    Scores = open("Scores.txt", "w")
    Scores.write(playerInfo[0][5])
    Scores.write(playerInfo[1][5])
    
    if mode == "Start":
        if ( whichKey == "0" ) or ( nameCharCount >= nameLimit ):
            playerInfo[nameCount][5] = nameIn 
            nameIn = ""
            nameCount += 1
            nameCharCount = 0
        else:
            if whichKey != "":
                    nameIn += whichKey.upper()
                    nameCharCount += 1
                    if nameCount == 0:
                        text( nameIn, 330, 300 )
                    else:
                        text( nameIn, 330, 400 )

        if nameCount == 2:
            mode = "Play"
   # print(playerInfo)
    whichKey = ""

    
            
    if mode == "Play":    
        image(boardImage, 0, 0, scalingFactor * numCols, scalingFactor * numRows)
        image(bannerImage, scalingFactor * numCols, 0, scalingFactor, scalingFactor * numRows)
        image(turtleImage, playerInfo[1][1] * scalingFactor, playerInfo[1][2] * scalingFactor, scalingFactor, scalingFactor)
        image(hareImage, playerInfo[0][1] * scalingFactor, playerInfo[0][2] * scalingFactor, scalingFactor, scalingFactor)
        image (menuBarImage, menuBarX, menuBarY, menuBarWidth, menuBarHeight)
        fill(0)
        textSize(25)
        text("green: ",495,550)
        text("purple: ",495,580)
        text(playerInfo[0][4] , 600, 550)
        text(playerInfo[1][4] , 600, 580)
        #print(whichBoundary)
        if diceValue == 1:  
            copy(diceImage, 0, 0, 100, 100, 600, 400, 100, 100)
        if diceValue==2:  
            copy(diceImage, 100, 0, 100, 100, 600, 400, 100, 100)
        if diceValue==3:
            copy(diceImage, 200, 0, 100, 100, 600, 400, 100, 100)
        if diceValue==4:
            copy(diceImage, 300, 0, 100, 100, 600, 400, 100, 100)
        if diceValue==5:
            copy(diceImage, 400, 0, 100, 100, 600, 400, 100, 100)
        if diceValue==6:
            copy(diceImage, 500, 0, 100, 100, 600, 400, 100, 100)
        if whichBoundary == startChosen:
            activeBoundaries = [ False for i in range( numBoundaries ) ]
            activeBoundaries [ resetGame ] = True
        if whichBoundary==helpChosen:
            image (helpImage, 0, 0, playAreaWidth, playAreaHeight )
            activeBoundaries = [ False for i in range( numBoundaries ) ]
            activeBoundaries [ resetGame ] = True
        if whichBoundary==scoreChosen:
            scoreBoard()
            image (menuBarImage, menuBarX, menuBarY, menuBarWidth, menuBarHeight)                
            activeBoundaries = [ False for i in range( numBoundaries ) ]
            activeBoundaries [ resetGame ] = True
        if playerInfo[int(playerTurn)][0] >= gameOver: 
            scoreBoard()
            text("Number of Turns per player:", 300, 200)
            textSize(30)
            text("CONGRATS " + playerInfo[int(playerTurn)][5] + " HAS WON", 300, 500)
            #textSize(100)
            textAlign(CENTER)
            textSize(20)
            #textAlign(CENTER)
            text("Press = to Restart", 320, 100)
            text("Press . to Exit", 320, 150)
            if keyPressed == True and key.upper() == '=':
                setup()
            elif keyPressed == True and key.upper() == '.':
                exit()

                
def diceRoll(playerInfo, diceImage, scalingFactor, numRows, numCols):
    global diceValue, playerTurn, board
    if diceValue==0:
        playerInfo[int(playerTurn)][0] = board[playerInfo[int(playerTurn)][0]+1]
        playerTurn = not playerTurn
        playerInfo[int(playerTurn)][0] = board[playerInfo[int(playerTurn)][0]+1]
        diceValue = 1
    else:
        diceValue = random.randint( 1,6 )
        playerInfo[int(playerTurn)][0] = board[playerInfo[int(playerTurn)][0] + diceValue]
        playerTurn = not playerTurn

    return(playerInfo[int(playerTurn)][0])
    
def movePlayer(playerInfo, numCols, numRows, playerTurn):        
    if ((playerInfo[int(playerTurn)][0] - 1) // numCols) % 2 == 0:
        playerInfo[int(playerTurn)][1] = (playerInfo[ int( playerTurn ) ] [ 0 ] - 1) % numCols
        playerInfo[playerTurn][4] += 1
    else:
        playerInfo[int(playerTurn)][1] = numCols - (playerInfo[int(playerTurn)][0] % numCols)
        playerInfo[playerTurn][4] += 1
    if playerInfo[int(playerTurn)][0] == 12 or playerInfo[int(playerTurn)][0] == 24:
        playerInfo[playerTurn][4] += 1
        playerInfo[int(playerTurn)][1] = 0
    playerInfo[int(playerTurn)][2] = (numRows - 1) - ((playerInfo[ int(playerTurn)][0] - 1 ) // numCols)
    return(playerInfo)
def mouseReleased():
    global allBoundaries, whichBoundary, removeBoundary, activeBoundaries, numBoundaries, validLocation,diceBound
    # for i in range( numBoundaries ):
    #     if activeBoundaries[ i ]:
    #         print(activeBoundaries)
    #         validXRange = allBoundaries[i][0][0] <= mouseX <= allBoundaries[i][1][0] 
    #         validYRange = allBoundaries[i][0][1]  <= mouseY <= allBoundaries[i][1][1]
    #         validLocation = validXRange and validYRange
    #         if validLocation:
    #             whichBoundary = i
    #             break
    #         if validLocation and removeBoundary:
    #             activeBoundaries[ whichBoundary ] = False
    whichBoundary = -1
    for i in range( numBoundaries ):
        if activeBoundaries[ i ]:
            validXRange = allBoundaries[i][0][0] <= mouseX <= allBoundaries[i][1][0] 
            validYRange = allBoundaries[i][0][1]  <= mouseY <= allBoundaries[i][1][1]
            validLocation = validXRange and validYRange
            if validLocation:
                whichBoundary = i
                break
        if validLocation and removeBoundary:
            activeBoundaries[ whichBoundary ] = False
    if diceBound:
        validXRange = diceBound[0][0] <= mouseX <= diceBound[1][0] 
        validYRange = diceBound[0][1]  <= mouseY <= diceBound[1][1]
        validLocation = validXRange and validYRange
        if validLocation:
            if playerInfo[int(playerTurn)][0] < gameOver:
                diceRoll(playerInfo, diceImage, scalingFactor, numRows, numCols)
                movePlayer(playerInfo, numCols, numRows, playerTurn)
                    
def keyReleased():
    global whichKey, asciList, controlKeys
    if key == CODED:
       if keyCode in controlKeys:
        whichKey = keyCode
    elif key in asciList:
        whichKey = key
    else:
        whichKey = ''        
