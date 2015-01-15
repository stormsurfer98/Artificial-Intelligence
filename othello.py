"""     +==========================+========-========*========-========+==========================+
        ||               APPLYING THE MINIMAX AI ALGORITHM TO THE GAME OF OTHELLO                ||
        ||                        by M. Stueben (Revised: January 5, 2015)                       ||
        +==========================+========-========*========-========+==========================+

              The zeroth rule for problem solving is to come to the problem with a history of
              successful problem-solving experiences behind you. Consequently, we can rarely
              afford to NOT complete a difficult assignment. We invent ourselves.

                                                  *  *  *

              The two most common statements made by coders are "How is this possible?" and "Oh
              no, a special case!". The first indicates that the coder does not understand either
              the probelm or his/her code. The second indicates a solution has begun.



              A SAMPLE 4-PLY DECISION TREE USING THE MINIMAX THEOREM (*) TO FIND BEST MOVE

   In the decision tree below, each node is a tuple (value, row, column). Only the value is shown in the tree.
The value is the best COMPUTER boardScore that can be expected, with the COMPUTER seeing ahead 4-ply and the
HUMAN seeing ahead 3-ply. Note that any boardScore is the number of HUMAN's pieces minus the number of
COMPUTER's pieces. Consequently, the larger score favors the HUMAN, while the smaller score favors the
COMPUTER.

                                      +----+
                    current board---> |o x |
                  (COMPUTER to move)  +----+
                                      / \  \___
                                     /   \     \___
                                    /     \__       \___
 The COMPUTER chooses the          /         \          \
 move with the MIN value -----> *M=3___      N=5        O=4  <-- These are the 4th-ply board scores that could
 on this level. However,         / \   \___   /\         /\      occur with optimal play on both sides. The
 each node on this level is     /   \      \__                   smaller the value, the better for the
 the MAX value of its          /     \        \__                COMPUTER.
 children.                    /       \          \__
                             /         \            \__
                            /           \              \__
                           /             \                \__
                          /               \                  \___
                         /                 \                     \
  max (across)        D=-1                *H=3                   L=2   <--HUMAN's possible replies
                       /\                   /\                    /\
                      /| \                 /| \                  /| \
                     / |  \               / |  \                / |  \
                    /  |   \             /  |   \              /  |   \
                   /   |    \           /   |    \            /   |    \
                  /    |     \         /    |     \          /    |     \
  min (across)  A=-1  B=2    C=4     E=9   C=4   *C=3      I=3   J=4    K=2   <-- COMPUTER's possible replies
                 /\    /\     /\      /\    /\     /\       /\    /\     /\
  max (across) -1 -2  1  2   1  4    9  7  1  4   2 *3     1  3  0  4   2 -1  <----- HUMAN's possible replies
--------------------------------------------------------------------------------------------------------------

NOTES: 1. The (parent) number for any node is either a max or min of the (child) nodes below it. But where do
          the numbers at the bottom come from? The numbers at the bottom are the board scores (HUMAN points
          minus COMPUTER points). The COMPUTER tries to go down a path to reach the minimum score for the
          4-ply level. The HUMAN tries to reach the maximum score for the same level. The COMPUTER chooses the
          node with the minimum score, but that score is the maximum value of the children's nodes. Again, the
          COMPUTER chooses the minimum of the HUMAN's maximums. And the COMPUTER assumes the HUMAN will choose
          the maximum of the COMPUTER's  minimums.

       2. Where does the tree come from? The tree is constructed by a depth-first recursive back-tracking
          search. Consequently, no more than one branch is ever held in memory at one time. But the re-
          cursion is unusual. We have a maxValue(depth) function and a minValue(depth) function. The maxValue
          function calls the minValue function, which in turn calls the maxValue function, etc. A base case
          (depth == 0) will return the best boardScore of all possible moves. WARNING: Your recursive code
          MUST account for the special case when white (COMPUTER) or black (HUMAN) has no legal move.

          +------------------------------------------------------------------------------------------+
          | TECHNICAL NOTE: I noticed that there is much common code shared by the maxValue(depth)   |
          | function and the minValue(depth) function. This violates the DRY (Don't Repeat Yourself) |
          | principle of coding. On the other hand, combining the two functions into one function    |
          | gives us a function that performs two different tasks, and which makes the function more |
          | difficult to code/understand/modify/debug. To combine the two functions into one function|
          | would take plenty of this:                                                               |
          |                                                                                          |
          |                      if player == COMPUTER: do this; else: do that.                      |
          |                                                                                          |
          | Extracting the common code into its own functions turned out to complicate the function, |
          | even though all coding principles would then seem to be satisfied. What to do?           |
          |                                                                                          |
          | When I came to examine this program, which I wrote last year, I couldn't understand my   |
          | own code at first. This disappointed me because I had made great efforts last year to    |
          | make my code clear. A couple hours (yes hours) later I not only understood it, but sig-  |
          | nificantly improved it. My previous implementation of the minimax algorithm had been     |
          | coded in a grossly inefficient manner. I changed the design, renamed variables, created  |
          | more descriptive comments, and reduced the minimax code by almost half. So why didn't I  |
          | code this efficiently the first time? I don't think I can implement a complicated-to-code|
          | algorithm AND code efficiently at the same time, even when I refactor at the end. By re- |
          | turning to the code long after I had forgotten how it worked, I was able to see how in-  |
          | efficiently it was coded (fresh eyes).                                                   |
          |                                                                                          |
          | I have three points here. First, the minimax algorithm, as simple as it is to understand,|
          | is NOT easy to code. Second, this program (outside of the minimax code) has other design |
          | flaws that would require too much time to fix now. Inefficient design is probably im-    |
          | possible to avoid, because it is difficult to discover a poor design before one has      |
          | committed to many blocks of code. And then the correction is not worth the reinvestment  |
          | of time, because the code--bad as it is--works. Finally, I was able to answer the        |
          | question posed above.                                                                    |
          |                                                                                          |
          | Placing the minimax code into twin recursive functions is the correct way for me to go,  |
          | because I cannot think of an easier way to both write and understand the minimax         |
          | algorithm. Keeping the code simple-to-understand is the first principle in programming,  |
          | from which all other coding principles follow.                                           |
          +------------------------------------------------------------------------------------------+

       3. Python's Tk graphics, REQUIRES that some variables MUST be global to compile. I used four: M for
          the matrix = Othello board, DEPTH for the maximum ply level of the tree,
          pointValueMatrixforWhite, and pointValueMatrixforBlack for the board evaluations matrices.

       4. Definition: In game theory, a ply is a half move. If each player in a two-player game makes a move,
          then the position is 2-ply deep.

       5. Definition: A zero-sum game is a game where one player's wins equal the opponent's loses. If we add
          one player's wins to his opponent's (negative) losses, the sum is always zero.

       6. Note well: In this program, the higher the boardScore the better for the HUMAN (black). Consequent-
          ly, the COMPUTER is always choosing the move with the minimum boardScore value.

       7. The minimax theorem says that the best move for either player in a two-player zero-sum game is the
          move that gives the opponent the least number of points (kinda obvious). But this theorem provides
          a simple strategy for both players: Player A's code is a greedy strategy. Player B's code is an
          altruistic strategy. The strategies are the same, except with some trivial changes of sign (max to
          min, and HUMAN to COMPUTER).

       8. As simple as the minimax theorem seems, it is tricky to put into place. I know this from experience.
          Consider the move/decision/search tree given previously.  What do we say about node M? Node M is the
          MAXIMUM of its children, and at the same time node M is the MINIMUM of the COMPUTER's choices on
          node M's level. Consequently, some nodes are both a MAXIMUM and a MINIMUM (in different ways) at the
          same time. It took me some time to realize that the question "is this node a minimum?" makes no
          sense without more qualification. Why do I think this program is going to be easier for you than me?
          Because the comments I left in the sample code are the result of many insights, and questions I had
          to answer for myself. Still, I removed about three lines of comments



       9. So, what does the minimax code for Othello look like? First, here is the call to the COMPUTER's
          move. We need to know the row, column, and (since we already calculated them) the tiles that should
          be turned over. The global constant DEPTH tells us how many ply (aka half moves, aka tree levels) we
          need to search to determine the best move. Note that the global DEPTH will be passed as parameter
          (now "depth", not "DEPTH") which will decrement by 1 with every recursive call.

                           bestRow, bestCol, finalPieces = computersMove(DEPTH)
          -----------------------------------------------------------------------------------------

      10. You MUST know how the boardScore is calculated. Here is what the function looks like:

                def boardScore(): # The higher the boardScore, the better for the HUMAN.
                   computerTotal = 0
                   humanTotal    = 0
                   for r in range(0, 8):
                        for c in range(0, 8):
                            if M[r][c] == COMPUTER:
                               computerTotal += pointValueMatrixforWhite[r][c]
                           if M[r][c] == HUMAN:
                                humanTotal += pointValueMatrixforBlack[r][c]
                   return humanTotal - computerTotal
          -----------------------------------------------------------------------------------------

      12. What does the computersMove look like? Here is most of it.

def computersMove(depth): # (even ply) IMPORTANT: This function is similar to the minValue function.
#---Initialize.
    depth = depth-1
    beta  = float( 'inf') # alpha and beta are dummy variables in this assignment. Keep them in, anyway.
    alpha = float('-inf')
    setOfMoveValuesAndMoves = []

#---Look at all possible moves for the COMPUTER, and there may be no moves (special case).
    for r in range(8):
        for c in range(8):
            if M[r][c] != 0:
               continue
            piecesTurnedOver = LocateTurnedPieces(r, c, COMPUTER)
            if not piecesTurnedOver:
               continue

#-----------Make a COMPUTER move, determine its depth-ply value, take it back (and then make another move).
            makeTheMoveAndTurnOverThePieces(r, c, piecesTurnedOver, COMPUTER) # COMPUTER makes a move.
            childValue = maxValue(depth-1, alpha, beta),r,c   # = boardScore and location for each move.
            setOfMoveValuesAndMoves.append(childValue)
            takeBackTheMoveAndTurnBackOverThePieces(r,c, piecesTurnedOver, COMPUTER)

#-----------Reduce beta if possible. [Keep this dummy comment in.]

#---Return the move with minimum boardScore of all possible COMPUTER moves in the current position.
#    ...
          -----------------------------------------------------------------------------------------

      13. Now comes the important question. What does the maxValue function look like? Here is my function
          with most of the code and a few comments removed. Most of the missing code is fairly simple to re-
          construct. Keep in mind that the utility functions are already written for you--e.g., the following
          functions already exist: LocateTurnedPieces(),  makeTheMoveAndTurnOverThePieces(), and
          takeBackTheMoveAndTurnBackOverThePieces(). Then what makes this function so difficult to write?
          There are a couple of small details (lines of code that accomplish something) that are hard to
          think of unless you get deep into the understanding of what is exactly being accomplished. The first
          small problem to solve is where to put the base case in this recursion.






def maxValue(depth, alpha, beta): # Recursive (odd ply) returns best move for HUMAN
#---Return the HUMAN move with MAXIMUM value that can be obtained after COMPUTER's previous move.
#   The returned tuple looks like this: (value, row, col).

#---Initialize.
    ...
    tuplesOfValuesWithTheirMoves = []
#---Look at all possible moves for HUMAN, and there may be no moves (an important special case).
    for r in range(8):
        for c in range(8):
            ...

#-----------Make a HUMAN move and store the move with its value in tuplesOfValuesWithTheirMoves.
#           The value of the HUMAN move is the minimum score the COMPUTER can obtain in response.
            ...
            childValue = minValue(depth-1, alpha, beta) # recursive case.
            ...

#-----------Attempt alpha-beta pruning.
            [Omit this code for now, but keep the place-marker (comment) in your code.]

#---Return
    ...
#----------------------------------------------------------------------------------------------------Othello--

      14. Here is some good news. The computersMove function [given previously] is a version of the minValue
          function which has the same code as the maxValue function (except max and min are switched and HUMAN
          and COMPUTER are switched). Thus, this code should be easier for you to write than it was for me.
          [Note: the pruning is different in the minValue and the maxValue function. But this assignment does
          not require pruning.]

      15. Confused? Too many details? Here is how to continue: Repeatedly re-read this handout. Work on this
          problem every day and perhaps several times a day. Repeatedly trace examples through the sample tree
          given previously. (I couldn't understand the implementation of the minimax theorem without seeing
          these examples.) Read other discussions of the minimax theorem on the Internet. When you discover
          that your code seems logical, yet fails, you need to ask what is missing. And then trace through the
          code (with lots of print statements) to watch what is happening on the matrix board (M). TRACING
          SAMPLE DATA IS HOW ALL ALGORITHMS ARE DEBUGGED. One of the reasons that the minimax algorithm is
          worth coding is because it gives you significant experience in tracing. Good luck.

      16. Curiously, when the computer plays at 6-ply it seems to apply strategy. But there is no strategy.
          The computer--or should I say the program--just applies the minimax algorithm with a self-modifying
          evaluation function. So where is the apparent strategy coming from? The appearance of strategy here
          is called an "emerging property". Would programs that interact with humans in an efficient way
          develop some kind of morality as an emerging property? If so, would different programs with
          different evaluation/fitness/cost functions produce different kinds of morality? Note that different
          religions promote different moralities. And the same religion in the same place, in same culture,
          and at the same time may have interpreters of morality that wildly contrast with each other. The
          subject of morality does not have universal agreement.
"""

##############################################<START OF PROGRAM>##############################################
def setUpCanvas(root): # These are the REQUIRED magic lines to enter graphics mode.
    root.title("A Tk/Python Graphics Program") # Your screen size may be different from 1270 x 780.
    canvas = Canvas(root, width = 1270, height = 780, bg = 'GREY30')
    canvas.pack(expand = YES, fill = BOTH)
    return canvas
#----------------------------------------------------------------------------------------------------Othello--

def createMatrix(): # = the initial position, with Black = 1, and white = -1. OK
    M = [ [0, 0, 0, 0, 0, 0, 0, 0,],
          [0, 0, 0, 0, 0, 0, 0, 0,],
          [0, 0, 0, 0, 0, 0, 0, 0,],
          [0, 0, 0,-1, 1, 0, 0, 0,], # The matrix M is GLOBAL.
          [0, 0, 0, 1,-1, 0, 0, 0,],
          [0, 0, 0, 0, 0, 0, 0, 0,],
          [0, 0, 0, 0, 0, 0, 0, 0,],
          [0, 0, 0, 0, 0, 0, 0, 0,],]
    return M
#----------------------------------------------------------------------------------------------------Othello--

def initializePointMatrices():
    global pointValueMatrixforWhite, pointValueMatrixforBlack
#---The COMPUTER's strategy will be based off of this GLOBAL matrix, which will be modified as
#   the board configuration changes. Remember: row (going down) is first:  P[row][col].
    pointValueMatrixforWhite = \
         [ [48,   6,  6,  6,  6,  6,   6, 48,], # P[0][0], P[0][1], ..., P[0][7]
           [ 6, -24, -4, -4, -4, -4, -24,  6,], # P[1][0], P[1][1], ..., P[1][7]
           [ 6,  -4,  1,  1,  1,  1,  -4,  6,], # P[2][0], P[2][1], ..., P[2][7]
           [ 6,  -4,  1,  1,  1,  1,  -4,  6,], # P[3][0], P[3][1], ..., P[3][7]
           [ 6,  -4,  1,  1,  1,  1,  -4,  6,], # P[4][0], P[4][1], ..., P[4][7]
           [ 6,  -4,  1,  1,  1,  1,  -4,  6,], # P[5][0], P[5][1], ..., P[5][7]
           [ 6, -24, -4, -4, -4, -4, -24,  6,], # P[6][0], P[6][1], ..., P[6][7]
           [48,   6,  6,  6,  6,  6,   6, 48,],]# P[7][0], P[7][1], ..., P[7][7]
    from copy import deepcopy
    pointValueMatrixforBlack = deepcopy(pointValueMatrixforWhite)
    return pointValueMatrixforWhite, pointValueMatrixforBlack
#----------------------------------------------------------------------------------------------------Othello--

def updateTheFourCorners():
    global pointValueMatrixforWhite, pointValueMatrixforBlack
#---1B. Modify upper-left corner cell's values if the HUMAN has taken that corner.
    if M[0][0] == 1:
        if M[0][2] in [0,-1]: pointValueMatrixforWhite[0][1] = -4 # bad  move for white (computer)
        if M[2][0] in [0,-1]: pointValueMatrixforWhite[1][0] = -4 # bad  move for white (computer)
        pointValueMatrixforWhite[1][1] = -4                       # bad  move for white (computer)
        pointValueMatrixforBlack[1][1] =  3                       # good move for black (human)

#---2B. Modify upper-right corner cell's values if the HUMAN has taken that corner.
    if M[0][7] == 1:
        if M[0][5] in [0,-1]: pointValueMatrixforWhite[0][6] = -4 # bad  move for white (computer)
        if M[2][7] in [0,-1]: pointValueMatrixforWhite[1][7] = -4 # bad  move for white (computer)
        pointValueMatrixforWhite[1][6] = -4                       # bad  move for white (computer)
        pointValueMatrixforBlack[1][6] =  3                       # good move for black (human)

#---3B. Modify lower-left corner cell's values if the HUMAN has taken that corner.
    if M[7][0] == 1:
        if M[5][0] in [0,-1]: pointValueMatrixforWhite[6][0] = -4 # bad  move for white (computer)
        if M[7][2] in [0,-1]: pointValueMatrixforWhite[7][1] = -4 # bad  move for white (computer)
        pointValueMatrixforWhite[6][1] = -4                       # bad  move for white (computer)
        pointValueMatrixforBlack[6][1] =  3                       # good move for black (human)

#---4B. Modify lower-right corner cell's values if the HUMAN has taken that corner.
    if M[7][7] == 1:
        if M[7][5] in [0,-1]: pointValueMatrixforWhite[7][6] = -4 # bad  move for white (computer)
        if M[5][7] in [0,-1]: pointValueMatrixforWhite[6][7] = -4 # bad  move for white (computer)
        pointValueMatrixforWhite[6][6] = -4                       # bad  move for white (computer)
        pointValueMatrixforBlack[6][6] =  3                       # good move for black (human)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#---1W. Modify upper-left corner cell's values if the COMPUTER has taken that corner.
    if M[0][0] == -1:
        if M[0][2] in [0,1]: pointValueMatrixforBlack[0][1] = -4 # bad  move for black (human)
        if M[2][0] in [0,1]: pointValueMatrixforBlack[1][0] = -4 # bad  move for black (human)
        pointValueMatrixforBlack[1][1] = -4                      # bad  move for black (human)
        pointValueMatrixforWhite[1][1] =  3                      # good move for white (computer)

#---2W. Modify upper-right corner cell's values if the COMPUTER has taken that corner.
    if M[0][7] == -1:
        if M[0][5] in [0,1]: pointValueMatrixforBlack[0][6] = -4 # bad  move for black (human)
        if M[2][7] in [0,1]: pointValueMatrixforBlack[1][7] = -4 # bad  move for black (human)
        pointValueMatrixforBlack[1][6] = -4                      # bad  move for black (human)
        pointValueMatrixforWhite[1][6] =  3                      # good move for white (computer)

#---3W. Modify lower-left corner cell's values if the COMPUTER has taken that corner.
    if M[7][0] == -1:
        if M[5][0] in [0,1]: pointValueMatrixforBlack[6][0] = -4 # bad  move for black (human)
        if M[7][2] in [0,1]: pointValueMatrixforBlack[7][1] = -4 # bad  move for black (human)
        pointValueMatrixforBlack[6][1] = -4                      # bad  move for black (human)
        pointValueMatrixforWhite[6][1] =  3                      # good move for white (computer)

#---4W. Modify lower-right corner cell's values if the COMPUTER has taken that corner.
    if M[7][7] == -1:
        if M[7][5] in [0,1]: pointValueMatrixforBlack[7][6] = -4 # bad  move for black (human)
        if M[5][7] in [0,1]: pointValueMatrixforBlack[6][7] = -4 # bad  move for black (human)
        pointValueMatrixforBlack[6][6] = -4                      # bad  move for black (human))
        pointValueMatrixforWhite[6][6] =  3                      # good move for white (computer)
#----------------------------------------------------------------------------------------------------Othello--

def updateTheMiddleRowsAndColumns():
    global pointValueMatrixforWhite, pointValueMatrixforBlack
    for n in range (2, 6):
        if M[0][n] == -1:
            pointValueMatrixforWhite[1][n] =  2 # TOP    row
            pointValueMatrixforBlack[1][n] = -1 # TOP    row
        if M[7][n] == -1:
            pointValueMatrixforWhite[6][n] =  2 # BOTTOM row
            pointValueMatrixforBlack[6][n] = -1 # BOTTOM row
        if M[n][0] == -1:
            pointValueMatrixforWhite[n][1] =  2 # LEFT   column
            pointValueMatrixforBlack[n][1] = -1 # LEFT   column
        if M[n][7] == -1:
            pointValueMatrixforWhite[n][6] =  2 # RIGHT  column
            pointValueMatrixforBlack[n][6] = -1 # RIGHT  column
        if M[0][n] == 1:
            pointValueMatrixforWhite[1][n] = -1 # TOP    row
            pointValueMatrixforBlack[1][n] =  2 # TOP    row
        if M[7][n] == 1:
            pointValueMatrixforWhite[6][n] = -1 # BOTTOM row
            pointValueMatrixforBlack[6][n] =  2 # BOTTOM row
        if M[n][0] == 1:
            pointValueMatrixforWhite[n][1] = -1 # LEFT   column
            pointValueMatrixforBlack[n][1] =  2 # LEFT   column
        if M[n][7] == 1:
            pointValueMatrixforWhite[n][6] = -1 # RIGHT  column
            pointValueMatrixforBlack[n][6] =  2 # RIGHT  column
#----------------------------------------------------------------------------------------------------Othello--

def updateThePointMatrices():
    initializePointMatrices()
    updateTheFourCorners()
    updateTheMiddleRowsAndColumns()
#----------------------------------------------------------------------------------------------------Othello--

def copyMatrixToScreen():
    canvas.create_text(30,30, text="x", fill = 'BLACK', font = ('Helvetica',1))
    for r in range (8):
       for c in range (8):
        if M[r][c] ==  1:
           sx = c*70 + 85
           sy = r*70 + 105
           canvas.create_oval(sx-25,sy-25, sx+25, sy+25, fill = 'BLACK')
        if M[r][c] == -1:
           sx = c*70 + 85
           sy = r*70 + 105
           canvas.create_oval(sx-25,sy-25, sx+25, sy+25, fill = 'WHITE')
    canvas.update()
#----------------------------------------------------------------------------------------------------Othello--

def showComputersMovesInRedOnScreen (r, c, pieces):
#---If white just moved, then make that stone red
    sy = r*70 + 105
    sx = c*70 + 85
    canvas.create_oval(sx-15,sy-15, sx+15, sy+15, fill = 'RED')

#------Turn any black stones partially white if they are about to be about to be turned over.
    for r,c in pieces:
           sy = r*70 + 105
           sx = c*70 + 85
           canvas.create_oval(sx-15,sy-15, sx+15, sy+15, fill = 'WHITE')
           canvas.update()
           sleep(PAUSE_TIME)
#----------------------------------------------------------------------------------------------------Othello--

def copyOldBoardToScreenInMiniaturizedForm(rr, cc):
 #--erase previous miniature board
    canvas.create_rectangle(650, 400, 821, 567, width = 5, fill    = 'GRAY30')
    ch = chr(9679)
    for r in range (8):
       for c in range (8):
        sx = c*20 + 665
        sy = r*20 + 412
        if M[r][c] ==  1:
           canvas.create_text(sx, sy, text = ch, fill = 'BLACK', font = ('Helvetica', 20, 'bold') )
        if M[r][c] == -1:
           canvas.create_text(sx, sy, text = ch, fill = 'WHITE', font = ('Helvetica', 20, 'bold') )

    canvas.create_text(cc*20 + 665, rr*20 + 413, text = 'B', fill = 'BLACK', \
                             font = ('Helvetica', 9, 'bold') )
    canvas.update()      # make all previous changes to the canvas
#----------------------------------------------------------------------------------------------------Othello--

def score(): # returns the number of black disks and white disks.
    whiteTotal = 0; blackTotal = 0
    for r in range(8):
      for c in range (8):
        if M[r][c] ==  1: blackTotal += 1
        if M[r][c] == -1: whiteTotal += 1
    return (blackTotal, whiteTotal)
#----------------------------------------------------------------------------------------------------Othello--
#   This function prints the matrices M , pointValueMatrixforWhite, and pointValueMatrixforBlack
#   to the console for debugging.
def printMatrices():
    print('\n Matrix M')
    print ('     0  1  2  3  4  5  6  7')
    print ('  +--------------------------+')
    for r in range(8):
      print (r, '|', end = '')
      for c in range (8):
         if M[r][c] == 1: ch = '#'
         if M[r][c] ==-1: ch = 'O'
         if M[r][c] == 0: ch = '-'
         if M[r][c] not in {-1,0,1}: ch = '?'
         print ("%3s"%ch, end = '')
      print ("  |")
    print ('  +--------------------------+')
    print ('  |human    = # = BLACK  =  1|')
    print ('  |computer = O = WHITE  = -1|')
    print ('  +--------------------------+')
    print ('M[3][0] =', M[3][0])
#   ------------------------------------------------
    print('\n Matrix pointValueMatrixforWhite')
    print ('      0    1    2    3    4    5    6    7')
    print ('  +------------------------------------------+')
    for r in range(8):
      print (r, '|', end = '')
      for c in range (8):
         print ("%5d"%pointValueMatrixforWhite[r][c], end = '')
      print ("  |")
    print ('  +------------------------------------------+')
#   ------------------------------------------------
    print('\n Matrix pointValueMatrixforBlack')
    print ('      0    1    2    3    4    5    6    7')
    print ('  +------------------------------------------+')
    for r in range(8):
      print (r, '|', end = '')
      for c in range (8):
         print ("%5d"%pointValueMatrixforBlack[r][c], end = '')
      print ("  |")
    print ('  +------------------------------------------+')
#----------------------------------------------------------------------------------------------------Othello--

def LocateTurnedPieces(r, c, player): # The pieces turned over are of -player's color. A zero in a
    if M[r][c] != 0: return []        # matrix M cell means an empty cell. This function does NOT
    totalFlipped =   []               # turn any pieces over.
 #--case 1 (move right)
    flipped = []
    if c < 6 and M[r][c+1] == -player:
        for n in range(1, 9):
            if c+n > 7 or M[r][c+n] == 0:
                flipped = []
                break
            if M[r][c+n] == player: break
            flipped += ((r,c+n,),)  # <-- We save the cell locations as tuples.
    totalFlipped += flipped

 #--case 2 (move down)
    flipped = []
    if r < 6 and M[r+1][c] == -player:
        for n in range(1, 9):
            if r+n > 7 or M[r+n][c] == 0:
                flipped = []
                break
            if M[r+n][c] == player: break
            flipped += ((r+n,c,),)
    totalFlipped += flipped

 #--case 3 (move up)
    flipped = []
    if r > 1 and M[r-1][c  ] == -player:
        for n in range(1, 9):
            if r-n < 0 or M[r-n][c] == 0:
                flipped = []
                break
            if M[r-n][c] == player: break
            flipped += ((r-n,c,),)
    totalFlipped += flipped

 #--case 4 (move left)
    flipped = []
    if c > 1 and M[r][c-1] == -player:
        for n in range(1, 9):
            if c-n < 0 or M[r][c-n] == 0:
                flipped = []
                break
            if M[r][c-n] == player: break
            flipped += ((r,c-n,),)
    totalFlipped += flipped

 #--case 5 (move down and right)
    flipped = []
    if r < 6 and c < 6 and M[r+1][c+1] == -player:
        for n in range(1, 9):
            if (r+n) > 7 or (c+n) > 7 or M[r+n][c+n] == 0:
                flipped = []
                break
            if M[r+n][c+n] == player: break
            flipped += ((r+n,c+n,),)
    totalFlipped += flipped

 #--case 6 (move up and left)
    flipped = []
    if r > 0 and c > 0 and M[r-1][c-1] == -player:
        for n in range(1, 9):
            if (r-n) < 0 or (c-n) < 0 or M[r-n][c-n] == 0:
                flipped = []
                break
            if M[r-n][c-n] == player: break
            flipped += ((r-n,c-n,),)
    totalFlipped += flipped

#--case 7 (move up and right)
    flipped = []
    if r > 1 and c < 6 and M[r-1][c+1] == -player:
        for n in range(1, 9):
            if (r-n) < 0 or (c+n) > 7 or M[r-n][c+n] == 0:
                flipped = []
                break
            if M[r-n][c+n] == player: break
            flipped += ((r-n,c+n,),)
    totalFlipped += flipped

 #--case 8 (move down and left)
    flipped = []
    if r < 6 and c > 1 and M[r+1][c-1] == -player:
        for n in range(1, 9):
            if (r+n) > 7 or (c-n) < 0 or M[r+n][c-n] == 0:
                flipped = []
                break
            if M[r+n][c-n] == player: break
            flipped += ((r+n,c-n,),)
    totalFlipped += flipped

    return totalFlipped
#----------------------------------------------------------------------------------------------------Othello--

def setUpInitialBoard(): #OK
    ch = chr(9679)
    Board  = createMatrix()
 #--print title
    canvas.create_text(330, 50, text = "OTHELLO with AI", \
                       fill = 'WHITE',  font = ('Helvetica', 20, 'bold'))
 #--print directions
    stng = "DIRECTIONS:\n1) Black (human) moves first. Click on any unoccupied cell.\n\
2) If a player cannot move, play passes to the opponent. \n3) Game ends when \
no legal move is possible.\n4) The player with the most colors on the board \
wins.\n5) A legal move MUST cause some pieces to turn color."
    canvas.create_text(810, 100, text = stng,  \
                       fill = 'WHITE',  font = ('Helvetica', 10, 'bold'))
 #--draw outer box, with red border
    canvas.create_rectangle(50, 70, 610, 630, width = 1, fill    = 'DARKGREEN')
    canvas.create_rectangle(47, 67, 612, 632, width = 5, outline = 'RED'  )

 #--Draw 7 horizontal and 7 vertical lines to make the cells
    for n in range (1, 8): # draw horizontal lines
       canvas.create_line(50, 70+70*n, 610, 70+70*n, width = 2, fill = 'BLACK')
    for n in range (1, 8):# draw vertical lines
       canvas.create_line(50+70*n,  70, 50+70*n, 630, width = 2, fill = 'BLACK')

 #--Place gold lines to indicate dangerous area to play (optional).
    canvas.create_rectangle(47+73, 67+73, 612-73, 632-73, width = 1, outline = 'GOLD'  )
    canvas.create_rectangle(47+2*71, 67+2*71, 612-2*71, 632-2*71, width = 1, outline = 'GOLD'  )

 #--Place letters at bottom
    tab = " " * 7
    stng = 'a' + tab + 'b' + tab + 'c' + tab + 'd' + tab + 'e' + \
                 tab + 'f' + tab + 'g' + tab + 'h'
    canvas.create_text(325, 647, text = stng, fill = 'DARKBLUE',  font = ('Helvetica', 20, 'bold'))

 #--Place digits on left side
    for n in range (1,9):
        canvas.create_text(30, 35 + n * 70, text = str(n),
                       fill = 'DARKBLUE',  font = ('Helvetica', 20, 'bold'))
 #--copy matrix to screen.
    copyMatrixToScreen()

 #--Place score on screen
    (BLACK, WHITE) = score()
    stng = 'BLACK = ' + str(BLACK) + '\nWHITE  = ' + str(WHITE)
    canvas.create_text(800, 200, text = stng, fill = 'WHITE',  font = ('Helvetica', 20, 'bold'))
    return Board
#----------------------------------------------------------------------------------------------------Othello--

def illegalClick(x, y): # Click is not on board or click is on an already-filled cell.
    player = 1 # player = Black
    if x < 52 or x > 609:
        print("Error 1. Mouse is to left or right of board.")
        return True # = mouse position is off the board

    if y < 62 or y > 632:
        print("Error 2.Mouse is above or below the board.")
        return True # = mouse position is off the board

 #--Calculate matrix position
    c = (x-50)//70
    r = (y-70)//70

    if M[r][c] != 0:
        print("ERROR 3: Cell is occupied at r =", r, " c =", c)
        return True      # = cell is occupied

 #--Not next to cell of opposite color
    flag = 0
    if c < 7 and           M[r  ][c+1] == -player: return False
    if r < 7 and           M[r+1][c  ] == -player: return False
    if r > 0 and           M[r-1][c  ] == -player: return False
    if c > 0 and           M[r  ][c-1] == -player: return False
    if r < 7 and c < 7 and M[r+1][c+1] == -player: return False
    if r > 0 and c > 0 and M[r-1][c-1] == -player: return False
    if r > 0 and c < 7 and M[r-1][c+1] == -player: return False
    if r < 7 and c > 0 and M[r+1][c-1] == -player: return False
    print("ERROR 4: no opposite colored neighbors at r =", r, " c =", c)
    return True # = illegal move
#----------------------------------------------------------------------------------------------------Othello--

def legalMove(player): # Check to see if any pieces will be turned over.
    pieces = []
    for r in range(8):
        for c in range(8):
           pieces += LocateTurnedPieces(r, c, player)
        if pieces != []: break
    if pieces ==[]:
       person = 'WHITE'
       if player == 1: person = 'BLACK'
       stng = 'There is no legal move for ' + person
       canvas.create_rectangle(655,260,957,307, width = 0, fill = 'GRAY30')
       canvas.create_text     (800,280,text = stng, fill = 'RED',  font = ('Helvetica', 10, 'bold'))
       return False
    return True
#----------------------------------------------------------------------------------------------------Othello--

def makeMove(r, c, pieces, player):
    global M
    if player not in [1, -1]: exit('ERROR: BAD PLAYER'+ str(player))
    if pieces == []: return
 #--make the player's legal move in matrix
    M[r][c] = player

    if player == COMPUTER:
        showComputersMovesInRedOnScreen(r, c, pieces)

 #--flip pieces to same color as the player
    for elt in pieces:
        M[elt[0]][elt[1]] = player

#--update the screen
    copyMatrixToScreen()

 #--erase old score and previous move
    canvas.create_rectangle(650, 160, 960, 310, width = 5, fill    = 'GRAY30')

 #--print new score
    (BLACK, WHITE) = score()
    stng = 'BLACK = ' + str(BLACK) + '\nWHITE  = ' + str(WHITE)
    canvas.create_text(800, 200, text = stng, \
                       fill = 'WHITE',  font = ('Helvetica', 20, 'bold'))

 #--print previous move on miniature board
    position = "previous move: "+ str(chr(c + 97))+str(r+1)
    canvas.create_text(800, 250, text = position, \
                       fill = 'WHITE',  font = ('Helvetica', 20, 'bold'))

    if player == COMPUTER:
       canvas.create_text(c*20 + 665, r*20 + 413, text = 'W', fill = 'WHITE', \
                             font = ('Helvetica', 9, 'bold') )
#----------------------------------------------------------------------------------------------------Othello--

def quit():
    blackScore, whiteScore = score()
    if   blackScore < whiteScore: msg = 'WHITE WON'
    elif whiteScore < blackScore: msg = 'BLACK WON'
    else:                         msg = '  DRAW!  '
    canvas.create_text(320, 350, text = msg, fill = 'RED',  font = ('Helvetica', 40, 'bold'))
    stng = 'THERE ARE NO LEGAL MOVES FOR EITHER PLAYER.'
    canvas.create_rectangle(655, 260, 955, 300, width = 0, fill = 'GRAY30')
    canvas.create_text(805, 280, text = stng, fill = 'GOLD',  font = ('Helvetica', 9, 'bold'))
#----------------------------------------------------------------------------------------------------Othello--

def totalPointsGainedFromFlippingPieces(player, r, c, pieces):
    if player == COMPUTER:
       total = pointValueMatrixforWhite[r][c]          # total = the points associated with the piece played.
       for (rr,cc) in pieces:
           total += pointValueMatrixforWhite[rr][cc]   # Add the values associated with the flipped pieces.
       return total
    if player == HUMAN:
       total = pointValueMatrixforBlack[r][c]          # total = the points associated with the piece played.
       for (rr,cc) in pieces:
           total += pointValueMatrixforBlack[rr][cc]   # Add the values associated with the flipped pieces.
       return total
    exit('ERROR in totalPointsGainedFromFlippingPieces() player = ' + str(player))
#----------------------------------------------------------------------------------------------------Othello--

def displayAllLegalMovesForHumanPlayer(kolor):
    for r in range(0, 8):
        for c in range(0, 8):
           kkolor = kolor
           if M[r][c] == 0:
              total  = len(LocateTurnedPieces(r, c, HUMAN))
           if M[r][c] == 0 and total != 0:
              sy = r*70 + 109
              sx = c*70 + 85
              if r == 0 or c == 0 or r == 7 or c == 7: kkolor = kolor
              canvas.create_text(sx, sy, text = str(total), fill = kkolor, \
                                 font = ('Helvetica', 15, 'bold') )
#----------------------------------------------------------------------------------------------------Othello--

def printTimeSpentThinking(startTime, player):
    assert player in {COMPUTER, HUMAN}
    if player == COMPUTER:
       msg = 'Computer thinks for ' + str(abs(round(clock() - startTime - PAUSE_TIME, 2))) + \
             ' seconds at depth of ' + str(DEPTH) +'.'
    if player == HUMAN:
       msg = 'Human thinks for '  + str(round(clock() - startTime, 2)) + ' seconds.'
    canvas.create_rectangle(620, 340, 990, 365, width = 0, fill = 'GRAY30')
    canvas.create_text(800, 352, text = msg, fill = 'WHITE',  font = ('Helvetica', 12, 'bold'))
#----------------------------------------------------------------------------------------------------Othello--

def boardScore(): # The higher the boardScore, the better for the HUMAN.
   computerTotal = 0
   humanTotal    = 0
   for r in range(0, 8):
        for c in range(0, 8):
            if M[r][c] == COMPUTER:
                computerTotal += pointValueMatrixforWhite[r][c]
            if M[r][c] == HUMAN:
                humanTotal += pointValueMatrixforBlack[r][c]
   return humanTotal - computerTotal
#----------------------------------------------------------------------------------------------------Othello--

def makeTheMoveAndTurnOverThePieces(r, c, piecesTurnedOver, player):
    global M

#---Double check that our move is made to an empty cell.
    assert M[r][c] == 0, ['player =', str(player)]

#---Make the move
    M[r][c] = player

#---Double check that the pieces we are turning over are of the opposite color of our player.
    piecesAreOppositeColorOfPlayer = True
    for (r,c) in piecesTurnedOver:
        if M[r][c] != -player:
           piecesAreOppositeColorOfPlayer = False
    assert piecesAreOppositeColorOfPlayer == True

#---Turn the pieces over.
    for (r,c) in piecesTurnedOver:
        M[r][c] = player
#----------------------------------------------------------------------------------------------------Othello--

def takeBackTheMoveAndTurnBackOverThePieces(r, c, piecesTurnedOver, player):
    global M
#---Double check that we are turning back a piece with the same color as player.
    assert M[r][c] == player, ['player =', str(player), 'M[r][c] =', M[r][c], '(r,c) =', (r,c)]

#---Take the move back.
    M[r][c] = 0

#---Double check that the pieces we are turning over are of the same color of our player.
    piecesAreSameColorAsPlayer = True
    for (r,c) in piecesTurnedOver:
        if M[r][c] != player:
           piecesAreSameColorAsPlayer = False
    assert piecesAreSameColorAsPlayer == True

#---Turn the pieces back over.
    for (r,c) in piecesTurnedOver:
        M[r][c] = -player
#-------------------------------------------=---------**---------=-----------------------------------Othello--

########################################## THE MOVES ARE MADE HERE ###########################################
def click(evt): # The evt = (evt.x, evt.y) parameter is the screen location on the mouse click.
# A legal move is guaranteed to exist.
    displayAllLegalMovesForHumanPlayer('DARKGREEN')

 #--Erase computer's thinking time as computer starts to think about the next move
    canvas.create_rectangle(620, 340, 990, 365, width = 0, fill = 'GRAY30')
 #--If move is off board, or cell full, or no opp. neighbor, then CLICK AGAIN.
    if illegalClick(evt.x, evt.y):
        canvas.create_rectangle(660, 270, 940,300, width = 0, fill = 'GRAY30')
        stng = 'Your last mouse click was an ILLEGAL MOVE.'
        canvas.create_text(800, 280, text = stng, fill = 'RED',  font = ('Helvetica', 9, 'bold'))
        return

 #--Find matrix coordinates (c,r) in terms of mouse coordinates (evt.x, evt.y).
    r = (evt.y-70)//70
    c = (evt.x-50)//70

 #--if none of the COMPUTER's pieces will be turned, then CLICK AGAIN.
    pieces     = LocateTurnedPieces(r, c, HUMAN)
    if pieces == []:
       canvas.create_rectangle(660, 270, 940,300, width = 0, fill = 'GRAY30')
       stng = 'Your last mouse click did NOT turn a piece.'
       canvas.create_text(800, 280, text = stng, fill = 'ORANGE',  font = ('Helvetica', 9, 'bold'))
       displayAllLegalMovesForHumanPlayer('YELLOW')
       return

 #--MAKE HUMAN MOVE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    copyOldBoardToScreenInMiniaturizedForm(r, c)
    makeMove(r, c, pieces, HUMAN) # The HUMAN clicked on position r,c.
    if legalMove(HUMAN) and not legalMove(COMPUTER):
        return

 #--FIND AND MAKE COMPUTER REPLY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    if legalMove(COMPUTER):
        startTime = clock()
        bestRow, bestCol, finalPieces = computersMove(DEPTH) # best COMPUTER response for given depth
        makeMove(bestRow, bestCol, finalPieces, COMPUTER)
        printTimeSpentThinking(startTime, COMPUTER)

    while legalMove(COMPUTER) and not legalMove(HUMAN): # If the human can't move then move again.
        startTime = clock()
        bestRow, bestCol, finalPieces = computersMove(DEPTH) # best COMPUTER Response for depth
        makeMove(bestRow, bestCol, finalPieces, COMPUTER)
        printTimeSpentThinking(startTime, COMPUTER)

    displayAllLegalMovesForHumanPlayer('RED')
    startTime = clock()
    if not legalMove(HUMAN) and not legalMove(COMPUTER): quit()
 #-- Note: legal move for human must now necessarily exist.
    return
#----------------------------------------------------------------------------------------------------Othello--

def computersMove(depth): # (even ply) This function is similar to the minValue function.
#---Initialize.
    depth = depth-1
    beta  = float( 'inf')
    alpha = float('-inf')
    setOfMoveValuesAndMoves = []

#---Look at all possible moves for the COMPUTER, and there may be no moves (special case).
    for r in range(8):
        for c in range(8):
            if M[r][c] != 0:
               continue
            piecesTurnedOver = LocateTurnedPieces(r, c, COMPUTER)
            if not piecesTurnedOver:
               continue

            if depth == 0:
              return boardScore()
            if not(legalMove()):
              return maxValue(depth-1, alpha, beta),r,c

#-----------Make a COMPUTER move, determine its depth-ply value, take it back (and then make another move).
            makeTheMoveAndTurnOverThePieces(r, c, piecesTurnedOver, COMPUTER) # COMPUTER makes a move.
            childValue = maxValue(depth-1, alpha, beta),r,c   # = boardScore and location for each  move.
            setOfMoveValuesAndMoves.append(childValue)
            takeBackTheMoveAndTurnBackOverThePieces(r,c, piecesTurnedOver, COMPUTER)

#-----------Reduce beta if possible.
            if childValue < beta: beta = childValue
            if beta <= alpha: return childValue

#---Return the move with minimum boardScore of all possible COMPUTER moves in the current position.
    return min(setOfMoveValuesAndMoves)
#----------------------------------------------------------------------------------------------------Othello--

def maxValue(depth, alpha, beta): # Recursive (odd ply) returns best move for HUMAN
#---Return the HUMAN move with MAXIMUM value that can be obtained after COMPUTER's previous move.
#   The returned tuple looks like this: (value, row, col).

#---Initialize.
    depth = depth-1
    setOfMoveValuesAndMoves = []
    tuplesOfValuesWithTheirMoves = []

#---Look at all possible moves for HUMAN, and there may be no moves (an important special case).
    for r in range(8):
        for c in range(8):
            if M[r][c] != 0:
               continue
            piecesTurnedOver = LocateTurnedPieces(r, c, HUMAN)
            if not piecesTurnedOver:
               continue

            if depth == 0:
              return boardScore()
            if not(legalMove()):
              return minValue(depth-1, alpha, beta)

#-----------Make a HUMAN move and store the move with its value in tuplesOfValuesWithTheirMoves.
#           The value of the HUMAN move is the minimum score the COMPUTER can obtain in response.
            makeTheMoveAndTurnOverThePieces(r, c, piecesTurnedOver, HUMAN) # HUMAN makes a move.
            childValue = minValue(depth-1, alpha, beta) # recursive case.
            setOfMoveValuesAndMoves.append(childValue)
            takeBackTheMoveAndTurnBackOverThePieces(r,c, piecesTurnedOver, HUMAN)

#-----------Attempt alpha-beta pruning.
            if childValue > alpha: alpha = childValue
            if beta <= alpha: return childValue

#---Return
    return max(setOfMoveValuesAndMoves)
#----------------------------------------------------------------------------------------------------Othello--

def minValue(depth, alpha, beta): # Recursive (even ply) Returns best move for COMPUTER.
#---Return the COMPUTER move with MINIMUM value that can be made after HUMAN's previous move. The returned
#   tuple looks like this: (value, row, col).

#---Initialize.
    depth = depth-1
    setOfMoveValuesAndMoves = []
    tuplesOfValuesWithTheirMoves = []

#---Look at all possible moves for HUMAN, and there may be no moves (an important special case).
    for r in range(8):
        for c in range(8):
            if M[r][c] != 0:
               continue
            piecesTurnedOver = LocateTurnedPieces(r, c, COMPUTER)
            if not piecesTurnedOver:
               continue

            if depth == 0:
              return boardScore()
            if not(legalMove()):
              return maxValue(depth-1, alpha, beta)

#-----------Make a COMPUTER move and store the move with its value in tuplesOfValuesWithTheirMoves.
#           The value of the COMPUTER's move is the maximum score the HUMAN can obtain in response.
            makeTheMoveAndTurnOverThePieces(r, c, piecesTurnedOver, COMPUTER) # COMPUTER makes a move.
            childValue = maxValue(depth-1, alpha, beta) # recursive case.
            setOfMoveValuesAndMoves.append(childValue)
            takeBackTheMoveAndTurnBackOverThePieces(r,c, piecesTurnedOver, COMPUTER)

#-----------Attempt alpha-beta pruning.
            if childValue < beta: beta = childValue
            if beta <= alpha: return childValue

#---Return
    return min(setOfMoveValuesAndMoves)
#====================================<GLOBAL CONSTANTS and GLOBAL IMPORTS>====================================

from tkinter  import Tk, Canvas, YES, BOTH  # <-- Use Tkinter (capital "T") in Python 2.x
from time     import clock, sleep
from sys      import setrecursionlimit; setrecursionlimit(100) # 1000 = default.
PAUSE_TIME =  0.5                           # used to see the tiles changinging colors.
root       =  Tk()
canvas     =  setUpCanvas(root)
pointValueMatrixforWhite, pointValueMatrixforBlack =  initializePointMatrices() # <-- Global.
M          =  createMatrix()            # <-- Global, because no variable can be passed to the click function.
HUMAN      =  1 # = Black
COMPUTER   = -1 # = White
DEPTH      =  6 # if DEPTH = 4, the computer can be beaten occasionally, and 2/3 of the nodes are pruned!
                # At depth = 8, the computer will rarely take longer than 11 seconds.
#===================================================<MAIN>====================================================

def main():
    root.bind('<Button-1>', click) # 1 = LEFT  mouse button calls the click function.
    root.bind('<Button-3>', click) # 3 = RIGHT mouse button calls the click function.
    setUpInitialBoard()
    root.mainloop()                # The window waits for the click function to be called.
#----------------------------------------------------------------------------------------------------Othello--
if __name__ == '__main__':  main()
###############################################<END OF PROGRAM>###############################################