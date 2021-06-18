# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Hazuki")
define k = Character("Kitsune")
define t = Character("turtle")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg city
    with fade

    "Tokyo is always busy, but in Summer the humidity makes it feel even more crowded. The skyscrapers all around make it feel like we are caged in the city. "

    "I can't even see the moon."
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    scene bg office
    with fade

    show hazuki sad
    

    # These display lines of dialogue.

    h "Ahh.. Another day I'll need to do overtime.."

    h "Working in Tokyo is so constricting and I'm tired. People work so fast, and the days go by so fast. Life goes by too quickly here."

    h "It's lonely.."

    h "I wish I could go to another world..."

    scene bg street
    with fade

    "Finally it's time to get home. The trains have already stopped running, so I'll have to walk."

    show hazuki sad

    h "Yep, I can't see the moon tonight either.."

    "Sigh."


    
    show shadow figure
    show kitsune figure
    
    show hazuki surprised
    h "what is that?"
    h "I've not seen anything like that before.."

    
    scene bg street corner
    with fade

    show kitsune figure
    with fade
    "The mysterious shadow stops at the end of an alleyway. Blue light illuminates the path."

    show hazuki surprised
    with fade
    h "Hmm? What is that?"

    show kitsune figure
    k "kekeke"
    k "Come to a better world..."

    show hazuki surprised
    h "A spirit fox? ... Oh it ran away?!"
    h "Wait, take me too!"
    menu:

        h "Should I follow the shadowy figure?"

        "Yes, go to a new world!":
            jump game

        "No, it's late. Let's go home..":
            jump home

#first choice split point- strong minded
    label game:

    show hazuki happy

    h "Let's go on an adventure!"

    "I'll just run down this path, the shadow figure went this way."

    "Somewhere around here..."

    show hazuki surprised

    "Wow - it's all glowing"
    
    scene black
    with dissolve

    scene bg bioluminescene
    with fade

    "Ahh.. What is this?"

    "What was I worrying about again?"

    "All these small, small worries."

    "It's all meaningless. What a comforting thought."



#scene two
    scene bg world
    with fade

    show hazuki back

    h "Woah, what is this world?"
    h "Where did that fox go?"
    h "My phone doesn't work here at all and I can't see a single building or road."

    show hazuki curious

    h "Exciting! Let's explore what this world has to offer!"

    show turtle side

    t "ohoh, a human?"
    t "It's better you don't come any further to this world. You won't be able to turn back."

    "A talking turtle? Alright then."
    h "Good! I want to leave the city far behind."

    t "Hm, how did you get here?"

    h "Well I followed a fox-like shadow, but I'm not really sure."

    t "ohoh, if you meet the fox spirit again you may be able to return home. You can find the fox up on that mountain at the shrine."

    h "I don't want to leave."

    t "You will. There are no perfect places."

    t "For now I'll help you cross the river."

    menu:

        t "Can I give some advice before we go?"

        "Yes, go to a new world!":
            jump warning

        "No, it's late.":
            jump ignorant


    label warning:
        t "Don't eat or drink anything of this realm, else you will become one of us.. Then you will truly be unable to leave."
    label ignorant:
        t "Very well..."


    scene bg river
    with fade

    "Let me give you a ride across the river. The mountain shrine is just beyond the forest. Beware."




























#disappointing ending
    label home:

    "It's too late to be wandering the streets. I must be so tired I'm hallucinating. I guess I'll go home and just carry on with my usual work routine"

    scene black
    with dissolve

    "I'm such a weak minded person."

    "I never follow up on opportunities even when they appear in front of me. Didn't I wish for the chance to visit another world?"

    "I guess I'll never know the answer to my question now..."

    "{b}Disappointing Ending{/b}."

    return

    scene black
    with dissolve


    # This ends the game.

    return
