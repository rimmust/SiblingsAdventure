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

transform sprite_possad:
    ypos 0.50
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
    $ renpy.movie_cutscene("movies/Intoscenecolo.mpg")

    show Luma happy at sprite_pos

    l "Why did Grandpa Joe leave this box in his inheritance?"

    hide Luma

    show Gomas happy at sprite_pos

    g "That box seems important, maybe it is a clue."

    hide Gomas

    show Poppy happy at sprite_pos

    p "I think there is something hidden in that box, Siblings. We should check"

    hide Poppy

    # changes the bacgkround scene.
    scene bg forest1 
    
    # Screen changes with the Menu 
    menu:
        "Choose one of these options:"
    
        "Option 1 Ask Poppy to help":
            # Play video Poppy Blushing animation
            $ renpy.movie_cutscene("movies/LumaWavem.mpg")
            jump optionA_menu

        "Option 2 Let Gomas help out":
            # Play video Gomas salute animation
            $ renpy.movie_cutscene("movies/Gomassalute.mpg")
            jump optionB_menu


        "Option 3 Let Luma inspect the box":
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

        "Solve the puzzle":
            jump videoA3

label videoA1:

    # changes the bacgkround scene.
    scene bg forest1

    show Luma happy at sprite_pos

    l "Poppy, you are good with symbols; can you figure out how to open this?"

    hide Luma

    show Poppy happy at sprite_pos

    p "Let's try a pattern. These stars must mean something"

    hide Poppy
    $ renpy.movie_cutscene("movies/Fireflyout.mpg")

    #Poppy speaks 
    show Poppy  happy at sprite_pos

    p "Come on, guys, the box is glowing more let's go."
    p "Look guys, let's follow that firefly. I think it will lead us somewhere."

    hide Poppy

    #shows a subchpice video 
    $ renpy.movie_cutscene("movies/Subchoicemodified.mpg")

    #shows texts of Poppy
    show Poppy  happy at sprite_pos

    p "Look Guys"

    hide Poppy
    
    # Shows keyfround and chest 
    $ renpy.movie_cutscene("movies/Keyfround.mpg")  
    $ renpy.movie_cutscene("movies/OpenTree.mpg")
    
    # plys the final aniamtion 
    $ renpy.movie_cutscene("movies/TresureOneGem.mpg")

    show Luma  happy at sprite_pos

    l "Wow guys, we made it."
    l "What a siblings adventure."

    hide Luma

    scene bg happyscene
    show Narrator happy at sprite_pos

    e "Luma, Gomas, and Poppy head back home, happy that their sibling adventure has come to an end."

    hide Narrator
    
    return 

label videoA2:
    
    show Poppy happy at sprite_pos

    p "Let me try this way"

    hide Poppy
    $ renpy.movie_cutscene("movies/Matchpuzzle.mpg")
    

    #This is what i added
    show Poppy  happy at sprite_pos

    p "Look guys, the box is glowing more."

    hide Poppy

    #shows a subchpice video 
    $ renpy.movie_cutscene("movies/Subchoicemodified.mpg")

    #shows texts of Poppy
    show Luma  happy at sprite_pos

    l "What is happening? I think the box will explode."

    hide Luma
    
    # Shows keyfround and chest 
    $ renpy.movie_cutscene("movies/Keyfround.mpg")  
    $ renpy.movie_cutscene("movies/OpenTree.mpg")

    # plys the final aniamtion 
    $ renpy.movie_cutscene("movies/3gemsfound.mpg")
    

    show Poppy  happy at sprite_pos

    p "Wow guys, look at all these gems."
    p "One for you, Luma"
    p "One for you, Gomas, to add to your chain, and one for me."
    p "We made it guys.Thanks Grandpa Joe"

    hide Poppy
    
    scene bg happyscene

    show Narrator happy at sprite_pos

    e "Luma, Gomas, and Poppy head back home, happy that their sibling adventure has come to an end."

    hide Narrator
    return


label videoA3:
    show Gomas  happy at sprite_pos

    g "You can do it."

    hide Gomas
    show Poppy happy at sprite_pos

    p "I think this one… and this one… yes!"

    hide Poppy

    $ renpy.movie_cutscene("movies/Puzzlesolved.mpg")
    #"You choose option 3."

    
    #shows a subchpice video 
    $ renpy.movie_cutscene("movies/Allpathswalkmod.mpg")

    #shows texts of Poppy
    show Luma  happy at sprite_pos

    l "I am a little bit scared… it's been a few hours now walking."

    hide Luma

    # plys the final aniamtion 
    $ renpy.movie_cutscene("movies/StopZone.mpg")

    
    show Poppy  sad at sprite_possad

    p "Oh no, we haven't solved the mystery!"
    p "Sorry guys."

    hide Poppy

   
    show Gomas  sad  at sprite_pos
    g "Don't worry Poppy."

    hide Gomas 
    
    return

# Gomas Options choice

label optionB_menu:
    menu:
        "Choose one of these options:"

        "Follow the Star marked":
            jump videoB1

        " Follow River Path":
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

    g "We're getting close!"

    hide Gomas

    #shows a subchpice video 
    $ renpy.movie_cutscene("movies/Gomaswalks.mpg")

    #shows texts of Poppy
    show Poppy  happy at sprite_pos

    p "Gomas, are you sure you read the right coordinates on the map?"

    hide Poppy
    
    # Shows keyfround and chest 
    $ renpy.movie_cutscene("movies/Lostincave.mpg")

    show Gomas  sad  at sprite_pos
    g "Oops, sorry… but I think I confused North and South."

    hide Gomas


    show Poppy  sad  at sprite_pos
    g "Don't worry, Gomas, things like that can happen."

    hide Poppy 

    
    return

label videoB2:
    show Gomas happy at sprite_pos

    g "The box likes this path. Look at the water!"

    hide Gomas
    
    $ renpy.movie_cutscene("movies/RiverPath.mpg")
    #"You choose option 2."


    #shows a subchpice video 
    $ renpy.movie_cutscene("movies/Allpathswalkmod.mpg")

    #shows texts of Poppy
    show Luma  happy at sprite_pos

    l "Look guys, the box keeps glowing and glowing."

    hide Luma

    # Shows keyfround and chest 
    $ renpy.movie_cutscene("movies/Keyfround.mpg")  
    $ renpy.movie_cutscene("movies/OpenTree.mpg")
    
    show Gomas  happy at sprite_pos

    g "Look at that chest, guys!"

    hide Gomas

   
    # plys the final aniamtion of letter found
    $ renpy.movie_cutscene("movies/Tresurechestletterfound.mpg")
    
    

    show Luma happy at sprite_pos

    l "Grandpa Joe left us this letter, that we need to treasure for all our life."
    l "Well done, brother — you led us to the right path."

    hide Luma

    scene bg happyscene
    show Narrator happy at sprite_pos

    e "Luma, Gomas, and Poppy head back home, happy that their sibling adventure has come to an end."

    hide Narrator
  
    return

label videoB3:

    scene bg forest1

    show Gomas happy at sprite_pos

    g "Oh! I missed this symbol.It means old trees."

    hide Gomas

    show Poppy happy at sprite_pos

    p "Then that's where we go"

    hide Poppy
    

    $ renpy.movie_cutscene("movies/Recheckmapg.mpg")
    #"You choose option 3."


    #shows texts of Poppy
    show Gomas  happy at sprite_pos

    g "Look guys, over there!"

    hide Gomas
    
    # plys the final aniamtion of Cave
    $ renpy.movie_cutscene("movies/Lostincave.mpg")
    
    show Gomas  happy at sprite_pos

    g "Guys, I think we got lost… ahh, see? The box stopped glowing."

    hide Gomas

    show Luma happy at sprite_pos

    l "Let's go back home."
    l "Don't worry, Gomas"
    
    hide Luma


    return

label optionC_menu:
    menu:
        "Choose one of these options:"

        "Luma Presses the buzzer.":
            jump videoC1

        "Stop.":
            jump videoC2

        "Shake the box.":
            jump videoC3

label videoC1:
    
    show Narrator happy at sprite_pos

    e "Poppy presses a small buzzer. The box pops slightly and sparkles burst out."

    hide Narrator

    $ renpy.movie_cutscene("movies/FlipSwitch.mpg")
    #"You choose option 1."

    #shows texts of Poppy
    show Poppy  happy at sprite_pos

    p "Let's follow that spark."

    hide Poppy

    #shows a subchpice video 
    $ renpy.movie_cutscene("movies/Allpathswalkmod.mpg")

    show Poppy  happy at sprite_pos

    p "Siblings, come on "

    hide Poppy
    # plys the final aniamtion of lost in the forest 
    $ renpy.movie_cutscene("movies/StopZone.mpg")
    
    
    show Poppy happy at sprite_pos

    p "Oh no, we're lost"
    p "Sorry guys."
    
    hide Poppy

  
    
    return
   

label videoC2:
    show Narrator happy at sprite_pos

    e "Luma moves Poppy aside."

    hide Narrator

    show Poppy happy at sprite_pos

    p "Careful, Luma."

    hide Poppy
    
    
    $ renpy.movie_cutscene("movies/Boxflys.mpg")
    #"You choose option 2."

    show Luma  happy at sprite_pos

    l "See? It want us to follow."

    hide Luma

    #shows a subchpice video 
    #$ renpy.movie_cutscene("movies/Subchoice.mpg")

    #shows texts of Poppy
    show Luma  happy at sprite_pos

    l "Come on guys lets follow the box."

    hide Luma

    # Shows keyfround and chest 
    $ renpy.movie_cutscene("movies/Keyfround.mpg")  
    $ renpy.movie_cutscene("movies/OpenTree.mpg")


    # plys the final aniamtion of letter found
    $ renpy.movie_cutscene("movies/Tresurechestletterfound.mpg")
    
    show Luma  happy at sprite_pos

    l "Sweet Grandpa  Joe"
    l "He wanted to leave us a special message "

    hide Luma

    scene bg happyscene

    show Narrator happy at sprite_pos

    e "Luma, Gomas, and Poppy head back home, happy that their sibling adventure has come to an end."

    hide Narrator

    return

label videoC3:
    show Narrator happy at sprite_pos

    e "Luma shakes the box. A tiny wooden compass pops out and magically spins, pointing to the north."

    hide Narrator

    #

    $ renpy.movie_cutscene("movies/Compass.mpg")
    # "You choose option 3."

    #shows a subchpice video 
    $ renpy.movie_cutscene("movies/Gomaswalks.mpg")

    #shows texts of Poppy
    show Luma  happy at sprite_pos

    l "Come on guys, over there."

    hide Luma

    # Shows keyfround and chest 
    $ renpy.movie_cutscene("movies/Keyfround.mpg")  
    $ renpy.movie_cutscene("movies/OpenTree.mpg")

    # plys a unique ending and found a frame
    $ renpy.movie_cutscene("movies/Framefound.mpg")
    
    show Luma happy at sprite_pos

    l "We did it, siblings. Well done!"

    hide Luma

    show Gomas happy at sprite_pos

    g "Well done,Luma"

    hide Gomas

    show Poppy happy at sprite_pos

    p "Sweet Grandpaster Joe"
    p "He wanted to give us this picture, the one he treasured a lot."

    hide Poppy

    scene bg happyscene
    
    show Narrator happy at sprite_pos

    e "Luma, Gomas, and Poppy head back home, happy that their sibling adventure has come to an end."

    hide Narrator


    return





    
    
