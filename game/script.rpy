# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Narrator")
define g = Character("Gomas")
define l = Character("Luma")
define p = Character("Poppy")

transform sprite_pos:
    ypos 0.47
    xpos 0.7


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg home 

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # shows the first sentence of text
    show Narrator happy at sprite_pos

    # These display lines of dialogue.

    e "It is a beautiful day in Cute Monsters Village."

    hide Narrator

    # intial animation
    $ renpy.movie_cutscene("movies/Introscene.mpg")

    show Luma happy at sprite_pos

    l "Why did Grandster Joe leave this box in his inheritance?"

    hide Luma

    show Gomas happy at sprite_pos

    g "That box seems important, maybe it is a clue”"

    hide Gomas

    # changes the bacgkround scene.
    scene bg forest1 
    
    # Screen changes with the Menu 
    menu:
        "Choose one of these options:"
    
        "Option 1Ask Poppy to help":
            # Play video Poppy Blushing animation
            $ renpy.movie_cutscene("movies/LumaWave.mpg")
            jump optionA_menu

        "Option 2Follow Gomas idea":
            # Play video Gomas salute animation
            $ renpy.movie_cutscene("movies/Gomassalute.mpg")
            jump optionB_menu


        "Option 3Let Luma inspect the box":
            # Play video of Luma waving.
            $ renpy.movie_cutscene("movies/PoppyWave.mpg")
            jump optionC_menu

           

    # Poppy help
label optionA_menu:
    menu:
        
        "Choose one of these options:"

        "Press stars on box pattern":
            jump videoA1

        "Rotate different shapes":
            jump videoA2

        "Double tap stars":
            jump videoA3

label videoA1:

    # changes the bacgkround scene.
    scene bg forest1

    show Luma happy at sprite_pos

    l "Luma you are good with symbols; can you figure out how to open this?"

    hide Luma

    show Poppy happy at sprite_pos

    p "Lets try a pattern. These triangles must mean something"

    hide Poppy
    $ renpy.movie_cutscene("movies/Startpuzzle.mpg")

    #Poppy speaks 
    show Poppy  happy at sprite_pos

    p "Come on guys the box seems glowing more lets go"

    hide Poppy

    #shows a subchpice video 
    $ renpy.movie_cutscene("movies/Subchoice.mpg")

    #shows texts of Poppy
    show Poppy  happy at sprite_pos

    l "Look Guys"

    hide Poppy
    
    # Shows keyfround and chest 
    $ renpy.movie_cutscene("movies/Keyfround.mpg")  
    $ renpy.movie_cutscene("movies/OpenTree.mpg")
    
    # plys the final aniamtion 
    $ renpy.movie_cutscene("movies/TresureOneGem.mpg")

    show Luma  happy at sprite_pos

    l "Wow guys we made it"
    l "What a siblings adventure"

    hide Luma
    
    return 

label videoA2:
    
    show Poppy happy at sprite_pos

    p "Let me try this way"

    hide Poppy
    $ renpy.movie_cutscene("movies/Matchpuzzle.mpg")
    

    #This is what i added
    show Poppy  happy at sprite_pos

    p "Look guys the box is glowing more"

    hide Poppy

    #shows a subchpice video 
    $ renpy.movie_cutscene("movies/Subchoice.mpg")

    #shows texts of Poppy
    show Luma  happy at sprite_pos

    l "What is happening I think the box will explode"

    hide Luma
    
    # Shows keyfround and chest 
    $ renpy.movie_cutscene("movies/Keyfround.mpg")  
    $ renpy.movie_cutscene("movies/OpenTree.mpg")

    # plys the final aniamtion 
    $ renpy.movie_cutscene("movies/Tresureche3Gems.mpg")
    

    show Poppy  happy at sprite_pos

    p "Wow guys look at all these Gems"
    p "One for you Luma"
    p "One for you Gomas to add to your chain and one for Me"
    p "We made it guys.Thanks Grandpa Joe"

    hide Poppy
    
    return


label videoA3:
    show Gomas  happy at sprite_pos

    g "You can do it"

    hide Gomas
    show Poppy happy at sprite_pos

    p "I think this one… and this one… yes!"

    hide Poppy

    $ renpy.movie_cutscene("movies/Puzzlesolved.mpg")
    #"You choose option 3."

    #This is what i added
    show Poppy  happy at sprite_pos

    p "Look guys lets follow that fire fly I think it will leads us somewhere"

    hide Poppy

    #shows a subchpice video 
    $ renpy.movie_cutscene("movies/Allpathswalks.mpg")

    #shows texts of Poppy
    show Luma  happy at sprite_pos

    l "I am a little bit scared its been a few hours now walking "

    hide Luma

    # Shows keyfround and chest 
    $ renpy.movie_cutscene("movies/Keyfround.mpg")  
    $ renpy.movie_cutscene("movies/OpenTree.mpg")
    
   
    show Poppy  sad  at sprite_pos

    p "Oh no "

    hide Poppy

    # plys the final aniamtion 
    $ renpy.movie_cutscene("movies/StopZone.mpg")


    show Poppy  sad  at sprite_pos

    p "Oh no we didnt solve the mystery"
    p "Sorry guys"

    hide Poppy


    show Gomas  sad  at sprite_pos
    g "Don't worry Poppy"

    hide Gomas 
    return

# Gomas Options choice

label optionB_menu:
    menu:
        "Choose one of these options:"

        "Follow the Star marked":
            jump videoB1

        "River Path":
            jump videoB2

        "Double check the map":
            jump videoB3

label videoB1:

    # changes the bacgkround scene.
    scene bg forest2
    
    show Narrator happy at sprite_pos

    e "Gomas leads the group along a sunny path."

    hide Narrator

    $ renpy.movie_cutscene("movies/Starmarked.mpg")
    #"You choose option 1."

    show Gomas happy at sprite_pos

    g "We re getting close!"

    hide Gomas

    #shows a subchpice video 
    $ renpy.movie_cutscene("movies/Gomaswalks.mpg")

    #shows texts of Poppy
    show Poppy  happy at sprite_pos

    p "Gomas are you sure you read the right coordiantes on the map "

    hide Poppy
    
    # Shows keyfround and chest 
    $ renpy.movie_cutscene("movies/Lostincave.mpg")

    show Gomas  sad  at sprite_pos
    g "Sorry guys,but I think I confused North and South"

    hide Gomas

    show Poppy  sad  at sprite_pos
    g "Don't worry Gomas,things that can happen"

    hide Poppy 

    
    return

label videoB2:
    show Gomas happy at sprite_pos

    g "The box likes this path. Look at the water!"

    hide Gomas
    
    $ renpy.movie_cutscene("movies/RiverPath.mpg")
    #"You choose option 2."


    #shows a subchpice video 
    $ renpy.movie_cutscene("movies/Allpathswalks.mpg")

    #shows texts of Poppy
    show Luma  happy at sprite_pos

    l "Look guys the box keeps glowing and glowing"

    hide Luma

    # Shows keyfround and chest 
    $ renpy.movie_cutscene("movies/Keyfround.mpg")  
    $ renpy.movie_cutscene("movies/OpenTree.mpg")
    
    show Gomas  happy at sprite_pos

    g "Look at that chest guys"

    hide Gomas

   
    # plys the final aniamtion of letter found
    $ renpy.movie_cutscene("movies/Tresurechest letter.mpg")
    
    show Poppy  happy at sprite_pos

    p "WooooWWW"

    hide Poppy

    show Luma happy at sprite_pos

    l "GrandPa Joe left us this letter,that we need to tresure for all our live"
    l "Well Done brother you lead us to the right path"

    hide Luma
  
    return

label videoB3:

    scene bg forest1

    show Gomas happy at sprite_pos

    g "Oh! I missed this symbol. It means old trees"

    hide Gomas

    show Poppy happy at sprite_pos

    p "Then that s where we go."

    hide Poppy
    

    $ renpy.movie_cutscene("movies/Recheckmapg.mpg")
    #"You choose option 3."


    #shows texts of Poppy
    show Gomas  happy at sprite_pos

    l "Look guys over there!"

    hide Gomas
    
    # plys the final aniamtion of Cave
    $ renpy.movie_cutscene("movies/Lostincave.mpg")
    
    show Gomas  happy at sprite_pos

    l "Guys I think we got Lost in ahh see the box stoped Glowing"

    hide Gomas

    show Luma happy at sprite_pos

    l "Lets go back home"
    l "Dont' worry Gomas"
    

    hide Luma
    return

label optionC_menu:
    menu:
        "Choose one of these options:"

        "Luma Flips the switch":
            jump videoC1

        "Stop":
            jump videoC2

        "Shake the box":
            jump videoC3

label videoC1:
    
    show Narrator happy at sprite_pos

    e "Poppy flips the tiny switch. The box pops slightly and sparkles burst out."

    hide Narrator

    $ renpy.movie_cutscene("movies/FlipSwitch.mpg")
    #"You choose option 1."

    #shows texts of Poppy
    show Poppy  happy at sprite_pos

    p "Lets follow that spark"

    hide Poppy

    #shows a subchpice video 
    $ renpy.movie_cutscene("movies/Allpathswalks.mpg")

    show Poppy  happy at sprite_pos

    p "Sibling come on "

    hide Poppy
    # plys the final aniamtion of lost in the forest 
    $ renpy.movie_cutscene("movies/StopZone.mpg")
    
    
    show Poppy happy at sprite_pos

    p "Oh no were lost in this Cave"
    p "Sorry guys"
    
    hide Poppy
    
    return
   

label videoC2:
    show Narrator happy at sprite_pos

    e "Luma moves Poppy aside"

    hide Narrator

    show Poppy happy at sprite_pos

    p "Careful Luma"

    hide Poppy
    
    
    $ renpy.movie_cutscene("movies/Boxflys.mpg")
    #"You choose option 2."

    show Luma  happy at sprite_pos

    l "See it want us to follow"

    hide Luma

    #shows a subchpice video 
    #$ renpy.movie_cutscene("movies/Subchoice.mpg")

    #shows texts of Poppy
    show Luma  happy at sprite_pos

    l "Come on guys lets follow the box"

    hide Luma

    # Shows keyfround and chest 
    $ renpy.movie_cutscene("movies/Keyfround.mpg")  
    $ renpy.movie_cutscene("movies/OpenTree.mpg")


    # plys the final aniamtion of letter found
    $ renpy.movie_cutscene("movies/Tresurechest letter.mpg")
    
    show Luma  happy at sprite_pos

    l "He wanted to leave us a special message "

    hide Luma

    return

label videoC3:
    show Narrator happy at sprite_pos

    e "Luma shakes the box a tiny wooden compass pops out and magically spins and points to the north."

    hide Narrator

    show Luma happy at sprite_pos

    l "Siblings it s' tresure time"

    hide Luma
    #

    $ renpy.movie_cutscene("movies/Compass.mpg")
    # "You choose option 3."

    #shows a subchpice video 
    $ renpy.movie_cutscene("movies/Gomaswalks.mpg")

    #shows texts of Poppy
    show Luma  happy at sprite_pos

    l "Come on guys over there"

    hide Luma

    # Shows keyfround and chest 
    $ renpy.movie_cutscene("movies/Keyfround.mpg")  
    $ renpy.movie_cutscene("movies/OpenTree.mpg")

    # plys a unique ending and found a frame
    $ renpy.movie_cutscene("movies/Framefound.mpg")
    
    show Luma happy at sprite_pos

    l "We did is siblings welL Done"

    hide Luma

    show Gomas happy at sprite_pos

    g "Well done Luma"

    hide Gomas

    show Poppy happy at sprite_pos

    p "Sweet Grandpaster Joe"
    p "He wanted to give us this picture who he tresure a lot"

    hide Poppy


    return





    
    
