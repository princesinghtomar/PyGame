satisfied requirements: == >
    ~   2 kinds of obstacles = > done lasers, black holes and the diagonally moving asteroids

        --------------ENHANCED - -----------------REQUIREMENT - ---------------------------------------------

    ~           2 diff player one at start and another at the end / ** ENHANCED to a more difficult question
                TO 2 PLAYER STARTING FROM SAME STARTING POSITION WITH DIFFERENT controls
                --------- -> IF Any Query on Why I enhanced this min. requirement
                -------------------------------REFER - ----------------------------------------------------
                -------------------- ANS of Query ASKED ON MOODLE - ---------- -===>
                -

                ANS GIVEN ON 14 FEB TITLE - "Starting Postion of players" = >

                The requirements given are minimum expectations you can certainly add / enhance features**/

                -
        --------------------------------------------------------------------------------------------------

    ~   player wins based on time taken to complete = Timer is set on upper right corner of game window to end game 
                                                    if players runs out of time
    ~   player dies ater hiting to obatacle
    ~   points accured while crossing obstacles given below: 
    ~   score is being shown and updated on the game window
    ~   more than 5 partition 
    ~   detecting collision between the obstacles and players 
    ~   both players have diff. controls REFER controls.
    ~   pep8 standard followed
    ~   config file made


score system :
    +10 for crossing the laser beam
    +5 for croosing fixed obstacles 

    --------------------------------------EXTRA ADDED----------------------------------------------------
    +15 for crossing the asteroid
    +40 for taking a scoreup
    -1 for using every 2 seconds
    -2 for collision with lasers
    -5 for collision with fixed  obstacles
    -10 for collision with asteroid
    +15 for reaching the end before the first player
        # This makes the other player to terminate the game and play next round 
    -----------------------------------------------------------------------------------------------------

Winner :

    ----------------------------------------Modified--------------------------------------------------
    Decides on the basis of total score by each player over the 7 matches
    -----------------------------------------------------------------------------------------------------

obstacles :
    2 types :
        moving :

            -----------------------------------EXTRA ADDED-----------------------------------------------
            - asteroid : moves diagonally from random position
            ---------------------------------------------------------------------------------------------

            - lasers : fired from the alien space ship continous randomly placed in each matches
        fixed :
            - 2 Small black holes randomly placed on the the game screen

player : 
    2 player starting at the same time from the same starting line 
    advantage given to the one who wins the race in form of extra points 
                - which are used in the last to decide the winner of the game after all 7 levels

controls :
    player 2 : w - up , d - left , a - right , s - down 
    player 1 : control  by arrows key on the keyboard

-----------------------------------------EXTRA ADDED-------------------------------------------------------
start and closing screens after each levels and Game :
    - a starting screening 
    - a level ending screen to ask if want to end the game or continue the game 
    - a game closing screen to ask for closing the game or if want to play it again
    - a counter to limit wastage of time by players
-----------------------------------------------------------------------------------------------------------


-----------------------------------------Special Function--------------------------------------------------
    - Special Slow Motion effect for increasing the chances of player to Win the game with some interval
      gaps continuosly everything in this function is random.
-----------------------------------------------------------------------------------------------------------
