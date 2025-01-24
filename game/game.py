import os

state = "start"
has_axe = False

start = """ 
Welcome to our Great-Share-holder-value-verification-application, to avoid excessive load on our application you must prove that you're human by accepting our terms and solving a chapta.



(1) Accept terms and Continue
(2) Read Terms
(3) Exit 
"""

terms_and_conditions = """
# Terms and Conditions of Participation

Welcome to our realm of services! By accessing, using, or merely lingering on our platform, you agree to the following Terms and Conditions (“Terms”). Please read carefully, as failure to comply will result in consequences ranging from minor inconveniences to existential dread.

1. **Data and Ownership Rights**  
   When you provide us with your information, you grant us an irrevocable, royalty-free license to use, share, and possibly misplace it. Rest assured, we will do so responsibly… unless irresponsibility proves more fun or profitable.

2. **Expectations for Your Conduct**  
   While using our services, you agree to:  
   - Follow all instructions, no matter how cryptic or unnecessary.  
   - Avoid any attempts to undermine, critique, or otherwise outshine us.  
   - Pretend you read this entire document, even if you didn’t.  

   Failure to meet these expectations will result in consequences. These may include—but are not limited to—strange technical glitches, targeted puns, or your favorite playlist mysteriously shuffling.

3. **Fees and Financial Obligations**  
   You may be charged fees at our discretion. While most fees will be predictable, some will be added simply for fun. For example:  
   - A **Convenience Fee** for paying us money.  
   - An **Inconvenience Fee** for not paying us quickly enough.  

   We reserve the right to invent new fees and backdate them if we’re feeling creative.

4. **Updates to These Terms**  
   We will update these Terms whenever we feel it necessary, or whenever we’re bored. Changes will take effect immediately, even if you haven’t read them yet. It’s your responsibility to stay informed—or just accept that ignorance is part of the experience.

5. **Termination of Access**  
   You may terminate your relationship with us at any time, but doing so will have… repercussions. These include, but are not limited to:  
   - Losing access to our services (obviously).  
   - Experiencing a faint sense of regret whenever you encounter our logo in the wild.  
   - The occasional mysterious text, just to remind you that we still exist.

6. **Liability (or Lack Thereof)**  
   We take no responsibility for any consequences resulting from your use of our services. This includes:  
   - Unforeseen technical issues.  
   - Questionable life decisions you made while using our platform.  
   - The inexplicable urge to binge-watch cat videos instead of working.

7. **Cookies and Tracking**  
   By using our platform, you agree to let us monitor your every move (digitally, not physically… probably). This includes the collection of cookies, which we use to optimize your experience and occasionally satisfy our insatiable craving for analytics.

8. **Disputes and Resolution**  
   In the unlikely event of a dispute, you agree to resolve it through methods of our choosing. This may include a dance-off, dramatic standoffs, or arbitration, whichever we deem most entertaining.

9. **Final Thoughts**  
   By clicking “I agree,” you are officially bound to these Terms. You may feel free to complain about this arrangement, but it will not change the fact that we hold all the cards.

Thank you for your compliance and welcome to our world. Enjoy responsibly—or don’t. Either way, we’re glad you’re here.



(1) Continue.
"""


captcha = """
Please complete this short captcha before continuing.

(1) Start Captcha.
"""

woods = """
  |     |
  \     \    v .   ._, |_  .,                                           &&& &&  & &&           /     /
  \    \           `-._\/  .  \ /    |/_           _-_                && &\/&\|& ()|/ @, &&    |     |
    \   \                \\  _\, y | \//        /~~   ~~\            &\/(/&/&||/& /_/)_&/_&    \     \\
   |    |         _\_.___\\, \\/ -.\||       /~~         ~~\       &() &\/&|()|/&\/ '%" & ()     \    \\
   \    \        `7-,--.`._||  / / ,        {               }     &_\_&&_\ |& |&&/&__%_/_& &&    |    |
     \     \     /'     `-. `./ / |/_.'      \  _-     -_  /    &&   && & &| &| /& & % ()& /&&  /    /
      |     \               |    |//            ~  \\ //  ~      ()&_---()&\&\|&&-&&--%---()~ /    /
     \     \                |_    /          _- -   | | _- _         &&     \|||             /   /
      |     \               |-   |             _ -  | |   -_                 |||           /   |
       \    |               |   =|                 // \\                     |||         /   /
       \    \               |    |      _.-.__..------------------._         |||        /   |
       --------------------/ ,  . \--------._                          , -=-~  .-^- _------::--._

You are on a path in a dark forest, there are two paths in front of you.
What will you do?

(1) Go left.
(2) Go right.
"""

tower = """
                         |\\
                         |_\\
                         |
                         |
      _,__,              /
     (00000)            /\\
    (00000)    __      /# \\
   (q888889)  (00)    /### \\
  (00q890OO0)(0000)  /a#### \\
       (0000000)    /####### \    sSSsS,
                    |a'aaaaa |   ssSSSs8
                    |aa'  aa |   SSSSSSs'
                    |aa'  a' |   s\\Ss/Ss
                    |a'aaaaa |    s\\//S
                    |aaa'aa| |      |/
                  #8|a|aaaaa |#     ||
                 # 8|aaa|aaa||###8  ||
                #8###aaaaaaa |88##8###  ##
               ####88#8 #8#8#888###8|###  ###
          #######88# 8#88 ##8###8888## #     #
        _/000## #888 ###8  8##88#88##   #     #
       /  ##   # #8   88#### 8####88## , # ### #
     _/     ###  #########8###888888\ '    #  ####
    /     /    #####  \     'chelle  \_'    #   ####
   |                   |    |  _   98  \       _/  \\
                        \_   \/         \__   /     \\

You stand before a dark, looming tower, its spires lost in swirling clouds.
The massive iron door hangs slightly ajar, creaking softly.

What will you do?

(1) Approach the tower.
(2) Turn back.
"""

demon = """
    ,-----.
   ( <> <> )
    )_ W _(
     |||||    A A A     Ah, the smell of fear still lingers here.   
      |||     | | |     How many adventurers have crept into this dungeon,
   __/)'(\__  `-+-'     thinking they could outwit me? And yet, their bones... all dust now.
  /\\     //\   |       What amusing little pests
 | |\\___//\ \  |
 | |/\\_//\ \ \ |
 | ||\\_//|  \ \|
 | ||/\_/\|   \ |
 | |/ /|\ \    \_)
 (_/  \_/  \    
   |  | |  |    
   |  | |  |    
   |()| |()|    
   |  | |  |    
   |  | |  |    
   |__| |__|    
   \__/ \__/    

As you approach the tower, a hulking demon emerges from the shadows, its glowing eyes fixed on you. 
The way forward is blocked.

What will you do?

(1) Stand your ground and fight.
(2) Attempt to sneak past the demon.
"""

demon = """
    ,-----.
   ( <> <> )
    )_ W _(
     |||||    A A A     Ah, the smell of fear still lingers here.   
      |||     | | |     How many adventurers have crept into this dungeon,
   __/)'(\__  `-+-'     thinking they could outwit me? And yet, their bones... all dust now.
  /\\     //\   |       What amusing little pests
 | |\\___//\ \  |
 | |/\\_//\ \ \ |
 | ||\\_//|  \ \|
 | ||/\_/\|   \ |
 | |/ /|\ \    \_)
 (_/  \_/  \    
   |  | |  |    
   |  | |  |    
   |()| |()|    
   |  | |  |    
   |  | |  |    
   |__| |__|    
   \__/ \__/    

As you approach the tower, a hulking demon emerges from the shadows, its glowing eyes fixed on you. 
The way forward is blocked.

What will you do?

(1) Stand your ground and fight.
(2) Attempt to sneak past the demon.
"""

injured1 = """
                    []
                    []
                    []
                    []
   _______________  []         _________________
   _______________) []        (_______________
    !     !     !   []        '  !     !     !
    !     !     !   []       ,!  !     !     !
    !     !     !   []      ! !  !     !     !
    !_____!_____!___[]_____'!_!__!_____!_____!_____
                    []__,_!_!_!
                    []_!__!_!|
                   ,[]_!__!_!
                 ,! []_!__!|
               ,! ! []_!__!
              ! ! ! []_!|
             !! ! !|[]_|
             !!!._|_[]
             !!!|!_.[]
             !|!_!__[]!.
             !_!_!__[]! !.
             !_!_!__[]! ! `.
              |!_!__|]! ! ! `.
               |_!__|]! ! ! ! `.
                 |____|_! ! ! !  `
                   |____|_! ! ! !
                    []____|_! ! !
                    []______|_! !
                    []________|_!
  __________________[]__________|____________________

You stumble through the iron door of the tower, slamming it shut behind you. 
Blood trickles from deep wounds, and your vision blurs. 
The demon's furious roars echo outside, but it doesn't pursue. You barely escaped with your life.

What will you do?

(1) Climb the staircase.
"""

sneaked = """
                    []
                    []
   _______________  []         _________________
   _______________) []        (_______________
    !     !     !   []        '  !     !     !
    !     !     !   []       ,!  !     !     !
    !     !     !   []      ! !  !     !     !
    !_____!_____!___[]_____'!_!__!_____!_____!_____
                    []__,_!_!_!
                    []_!__!_!|
                   ,[]_!__!_!
                 ,! []_!__!|
               ,! ! []_!__!
              ! ! ! []_!|
             !! ! !|[]_|
             !!!._|_[]
             !!!|!_.[]
             !|!_!__[]!.
             !_!_!__[]! !.
             !_!_!__[]! ! `.
              |!_!__|]! ! ! `.
               |_!__|]! ! ! ! `.
                 |____|_! ! ! !  `
                   |____|_! ! ! !
                    []____|_! ! !
                    []______|_! !
                    []________|_!
  __________________[]__________|____________________

Heart pounding, you slip into the tower unnoticed.
The iron door creaks softly as it closes, sealing you inside.
Shadows stretch across the stone walls, and the air is damp and cold.

(1) Climb the staircase.
"""

corridor = """

          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
      ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
   ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
   ⣿⣿⣿⣿⣿⣿⣿⣿      \       ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿                  ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿            /     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
  ⣿⣿⣿⣿⣿⣿⣿         \         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿                       ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿            /         ⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿            \          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿                        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿            /            ⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿             \         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿                        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿           /              ⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿               \          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿                           ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿          /                ⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿                \         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿                           ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿         /                 ⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿                 \        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿                           ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿        /                  ⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿                  \       ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿                           ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿       /                   ⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿                   \      ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿                           ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿      /                    ⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿                    \     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿                           ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿     /                     ⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿                     \    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿                           ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿    /                      ⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿                      \   ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿                           ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿   /                       ⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿                       \  ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿                           ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿  /                        ⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿                        \ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿                           ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ /                         ⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿                         \⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿                           ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿/                          ⣿⣿⣿⣿⣿⣿⣿⣿

You find yourself in a dimly lit corridor, the stone walls closing in around you. 

To your left, the corridor twists into shadowy unknowns. 
To your right, faint light spills from under a cracked door. 
Forward, the roar grows louder, vibrating through the walls.

What will you do?

(1) Go left into the shadows.
(2) Go right toward the faint light.
(3) Move forward toward the source of the roar.
"""

cursed_chest = """
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-\"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/

You spot a wooden chest against the wall, its surface carved with strange symbols. 
The lock is broken, and the lid slightly ajar.

What will you do?

(1) Open the chest.
(2) Turn back.

The air feels unnaturally heavy around it.
"""

cursed = """
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-\"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/

As you open the chest, dark mist erupts, wrapping around you.
A burning pain sears your skin as a voice whispers, "You are mine."

The curse has taken hold.

What will you do?

(1) Push forward despite the curse.
(2) Succumb to the darkness.
"""

succumb = """
               ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO\\
       ::::::;       ;          OOOOO\\
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#

You succumbed to the darkness.

(1) Use Stone of Revival.
"""

axe_chest = """
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-\"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/

You stand before a chest, feeling the weight of something powerful hidden within, waiting to be revealed.

What will you do?

(1) Open the chest.
(2) Turn back.
"""

axe = """
  ,  /\  .  
 //`-||-'\\\\ 
(| -=||=- |)
 \\\\,-||-.// 
  `  ||  '  
     ||     
     ||     
     ||     
     ||     
     ||     
     ()

You open the chest, and there it is—the Axe of a Thousand Truths. 
It's blade glowing with ancient power, ready to reveal secrets long buried.

(1) Take the axe.
"""

dragon = """
                              ___, ____--'
                         _,-.'_,-'      (
                      ,-' _.-''....____(
            ,))_     /  ,'\ `'-.     (          /\\
    __ ,+..a`  \(_   ) /   \    `'-..(         /  \\
    )`-;...,_   \(_ ) /     \  ('''    ;'^^`\ <./\.>
        ,_   )   |( )/   ,./^``_..._  < /^^\ \_.))
       `=;; (    (/_')-- -'^^`      ^^-.`_.-` >-'
       `=\\\\ (                             _,./
         ,\`(                         )^^^
           ``;         __-'^^\       /
             / _>emj^^^   `\..`-.    ``'.
            / /               / /``'`; /
           / /          ,-=='-`=-'  / /
     ,-=='-`=-.               ,-=='-`=-.
   *******************************************

You approach a dragon, its massive form looming before you. 
Its eyes glow with a fiery intensity, and the ground trembles with each breath it takes. 

What do you do?

(1) Fight the dragon.
(2) Turn back.
"""

dragon_fail = """
                              ___, ____--'
                         _,-.'_,-'      (
                      ,-' _.-''....____(
            ,))_     /  ,'\ `'-.     (          /\\
    __ ,+..a`  \(_   ) /   \    `'-..(         /  \\
    )`-;...,_   \(_ ) /     \  ('''    ;'^^`\ <./\.>
        ,_   )   |( )/   ,./^``_..._  < /^^\ \_.))
       `=;; (    (/_')-- -'^^`      ^^-.`_.-` >-'
       `=\\\\ (                             _,./
         ,\`(                         )^^^
           ``;         __-'^^\       /
             / _>emj^^^   `\..`-.    ``'.
            / /               / /``'`; /
           / /          ,-=='-`=-'  / /
     ,-=='-`=-.               ,-=='-`=-.
   *******************************************

The dragon roars, unleashing a torrent of fire. 
You dive to the side, the flames licking at your heels as you barely escape with your life.

Perhaps you should look for a weapon.

(1) Turn back.
"""

dragon_success = """
                              ___, ____--'
                         _,-.'_,-'      (
                      ,-' _.-''....____(
            ,))_     /  ,'\ `'-.     (          /\\
    __ ,+..a`  \(_   ) /   \    `'-..(         /  \\
    )`-;...,_   \(_ ) /     \  ('''    ;'^^`\ <./\.>
        ,_   )   |( )/   ,./^``_..._  < /^^\ \_.))
       `=;; (    (/_')-- -'^^`      ^^-.`_.-` >-'
       `=\\\\ (                             _,./
         ,\`(                         )^^^
           ``;         __-'^^\       /
             / _>emj^^^   `\..`-.    ``'.
            / /               / /``'`; /
           / /          ,-=='-`=-'  / /
     ,-=='-`=-.               ,-=='-`=-.
   *******************************************


With the Axe of a Thousand Truths in hand, you charge at the dragon. 
Its fiery breath roars past you, but with a single, devastating strike, the axe cleaves through its scales. 
The beast falls, its reign of terror ended.

(1) Continue.
"""

twins = """
||||||||||||||||||||\                                                      /|||||||||||||||||||| 
|||||||||||||||||||\\\\                                                  ////|||||||||||||||||||
|||/////////        \||                                                  ||/        \\\\\\\\\|||
||/////   _____   ___\                                                    /___   _____   \\\\\||
||||||   / ___   /___/          ______               ______               \___\   ___ \   ||||||
|/   ||   /_(_) |/(_)        .-` !  ; '-,         ,-' ;  ! `-.             (_)\| (_)_\   ||   \|
 | |  |          \  |       / .  :  !  : \       / :  !  :  . \            |  /          |  | | 
 |                \ /       |  ;  :__   ; _|    |_ ;   __:  ;  |           \ /                | 
 \__|   /      /___\        |  !  .)(:  . |(    )| .  :)(.  !  |            /___\      \   |__/ 
   |   /|\________\         |  _  (##)    "|    |"    (##)  _  |             /________/|\   |   
   |    |\________|         ) (_)  '`;  :  |    |  :  ;`'  (_) (             |________/|    |   
   |    |      ||           |     .  :  :  |    |  :  :  .     |               ||      |    |   
   |    |  ____||___        |  ;  ;  ,  ! _(    )_ !  ,  ;  ;  |            ___||____  |    |   
   |    | /   __    \       |  :  :  .  . ||    || .  .  :  :  |           /    __   \ |    |   
   |    \/___/__\    \      |  .  :  |  . "|    |" .  |  :  .  |          /    /__\___\/    |   
   |   \________/\___/      |___.----;_2-tm|    |mt-2_;----.___|          \___/\________/   |
   |            |                                                              |            | 

At the end of the tunnel you encounter two duboius looking dwarf twins, they seem to be guarding two doors.

"One of these doors leads to ceratin death" one of them says, "Behind the other lies what you are seeking",

Due to their dubious looks, it appears obvious to you that one of them always lies while the other can only tell the truth

With this knowledge you decide to question the twins to find out which is telling the truth.

(1) Question the left twin.
(2) Question the right twin.
"""

left_twin = """
||||||||||||||||||||\       
|||||||||||||||||||\\\\    
|||/////////        \||    
||/////   _____   ___\     
||||||   / ___   /___/     
|/   ||   /_(_) |/(_)      
 | |  |          \  |      
 |                \ /      
 \__|   /      /___\       
   |   /|\________\        
   |    |\________|        
   |    |      ||          
   |    |  ____||___       
   |    | /   __    \      
   |    \/___/__\    \     
   |   \________/\___/  
   |            |        

Here is a voucher for isEven-AI: AV67FDAO931JDE

(1) Continue.
"""

right_twin = """
        /|||||||||||||||||||| 
      ////|||||||||||||||||||
      ||/        \\\\\\\\\|||
       /___   _____   \\\\\||
       \___\   ___ \   ||||||
        (_)\| (_)_\   ||   \|
        |  /          |  | | 
        \ /                | 
         /___\      \   |__/ 
          /________/|\   |   
          |________/|    |   
            ||      |    |   
         ___||____  |    |   
        /    __   \ |    |   
       /    /__\___\/    |   
       \___/\________/   |
            |            |   

Here is a voucher for isEven-AI: KI893AB69KORV12

(1) Continue.
"""



while True:
    os.system("cls")
    if state == "start":
        print(start)
        inp = input("Enter action: ")
        if inp == "1":
            state = "captcha"
        else:
            state = "terms"
        continue
    if state == "terms":
        print(terms_and_conditions)
        inp = input("Enter action: ")
        state = "start"
        continue
    if state == "captcha":
        print(captcha)
        inp = input("Enter action: ")
        state = "woods"
        continue
    if state == "woods":
        print(woods)
        inp = input("Enter action: ")
        state = "tower"
        continue
    if state == "tower":
        print(tower)
        inp = input("Enter action: ")
        if inp == "1":
            state = "demon"
        else:
            state = "woods"
        continue
    if state == "demon":
        print(demon)
        inp = input("Enter action: ")
        if inp == "1":
            state = "injured1"
        else:
            state = "sneaked"
        continue
    if state == "injured1":
        print(injured1)
        inp = input("Enter action: ")
        state = "corridor"
        continue
    if state == "sneaked":
        print(sneaked)
        inp = input("Enter action: ")
        state = "corridor"
        continue
    if state == "corridor":
        print(corridor)
        inp = input("Enter action: ")
        if inp == "1":
            state = "cursed_chest"
        elif inp == "2":
            state = "axe_chest"
        else:
            state = "dragon"
        continue
    if state == "cursed_chest":
        print(cursed_chest)
        inp = input("Enter action: ")
        if inp == "1":
            state = "cursed"
        else:
            state = "corridor"
        continue
    if state == "cursed":
        print(cursed)
        inp = input("Enter action: ")
        if inp == "1":
            state = "corridor"
        else:
            state = "succumb"
        continue
    if state == "succumb":
        print(succumb)
        inp = input("Enter action: ")
        state = "corridor"
        continue
    if state == "axe_chest":
        print(axe_chest)
        inp = input("Enter action: ")
        if inp == "1":
            state = "axe"
        else:
            state = "corridor"
        continue
    if state == "axe":
        print(axe)
        inp = input("Enter action: ")
        has_axe = True
        state = "corridor"
        continue
    if state == "dragon":
        print(dragon)
        inp = input("Enter action: ")
        if inp == "1":
            if has_axe:
                state = "dragon_success"
            else:
                state = "dragon_fail"
        else:
            state = "corridor"
        continue
    if state == "dragon_fail":
        print(dragon_fail)
        inp = input("Enter action: ")
        state = "corridor"
        continue
    if state == "dragon_success":
        print(dragon_success)
        inp = input("Enter action: ")
        state = "twins"
        continue
    if state == "twins":
        print(twins)
        inp = input("Enter action: ")
        if inp == "1":
            state = "left_twin"
        else:
            state = "right_twin"
        continue
    if state == "left_twin":
        print(left_twin)
        inp = input("Enter action: ")
        state = "twins"
        continue
    if state == "right_twin":
        print(right_twin)
        inp = input("Enter action: ")
        state = "twins"
        continue




    


        

