# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Hazuki")
define k = Character("Kitsune")

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

    "Ahh.."

    "What was I worrying about again?"

    "All these small, small worries."

    "It's all meaningless. What a comforting thought."

    scene bg world
    with fade

    show hazuki back

    h "Woah, what is this world?"
    h "Where did that fox go?"









































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
