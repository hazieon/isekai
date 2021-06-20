# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Hazuki")
define k = Character("Kitsune")
define t = Character("Turtle")
define c = Character("Caw")

# The game starts here.

label start:
    $ mind_strength = 0
    $ world_knowledge = 0
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

    show Turtle 

    t "ohoh, a human?"
    t "It's better you don't come any further to this world. You won't be able to turn back."

    "A talking Turtle? Alright then."
    h "Good! I want to leave the city far behind."

    t "Hm, how did you get here?"

    h "Well I followed a fox-like shadow, but I'm not really sure."

    t "ohoh, if you meet the fox spirit again you may be able to return home. You can find the fox up on that mountain at the shrine."

    h "I don't want to leave."

    t "You will. There are no perfect places."

    t "For now I'll help you cross the river."

    menu:

        t "Can I give some advice before we go?"

        "Yes, please tell me anything.":
            jump warning

        "No, I can do this alone.":
            jump ignorant


    label warning:
        # $ menu_flag = true
        $ world_knowledge +=2
        t "Don't eat or drink anything of this realm, else you will become one of us.. Then you will truly be unable to leave."
        jump turtle_continue
    label ignorant:
        # $ menu_flag = false
        $ mind_strength +=1
        t "Very well..."
        jump turtle_continue

    label turtle_continue:
    scene bg river
    with fade

    "Let me give you a ride across the river. The mountain shrine is just beyond the forest. Beware."


    scene black
    with dissolve

    "The walk to the forest wasn't far at all. What was that Turtle worried about? This place is so beautiful."

    scene bg forest entrance
    show hazuki happy 

    h "Great, there's the forest entrance!"

    show caw happy 

    c "Hey, shiny eyed girl, where are you going?"
    
    "A talking crane now, huh?"

    h "I'm heading to the mountain shrine to meet some fox.. I think."

    c "Through the forest? Meet the fox spirit? Wow - an adventurous soul!"

    h "..."

    c "I know shortcuts through the forest. You can take shelter and find food easily there too. Come on, come on."

    h "Oh that would be great, thank you!"

    "Wow everyone here is so kind! I'll be able to meet that fox in no time."

    c "kekeke - come on, come on."




#scene 2.5
    scene bg forest path
    show hazuki scared
    
    h "It's a bit spooky here actually..."
    show caw happy
    c "But you are ADVENTUROUS, right? Right?"
    h "Yes! I want to see more. But.."
    c "Come on, come on!"
     

    scene black
    with dissolve

    show hazuki sad
    h "It's getting late"
    c "Indeed, you must be tired. Have some berries..."

    scene forest fruit
    with fade

    h "Hmm they don't look that great.. but I am exhausted."

    show caw happy
    menu:
        c "Help yourself to the berries! kekeke"

        "Alright, I'll try a few.":
            jump eat_yes

        "No thanks, I'll be fine.":
            jump eat_no

    label eat_yes:
        # $ menu_flag = true
        $ mind_strength -=1
        c "Caaaaw kekeke"
        jump caw_done

    label eat_no:
        # $ menu_flag = false
        $ mind_strength +=2
        c "Caw.."
        jump caw_done

    label caw_done:
    
    scene bg forest dark
   

    show hazuki surprised
    h "What the?!"
    show caw angry #crow!!
    c "Rotten humans!"
    c "Dead to the core!"
    h "That crane was actually a.. crow?!"
    show caw angry #crow!!
    
    c "Give me your EYES!!"
    c "Give me your soul!"
    
    scene bg forest fight
    with fade
 
    menu:
        "The crow is attacking me! What should I do?"

        "Fight!":
            jump fight

        "Run away!":
            jump run
        
label fight:
        $ mind_strength +=2
        "Stay back, fiend!"
        show hazuki fight
        h "I don't owe you anything!"
        h "My eyes and my soul are mine."
        c "Caw!!"
        show caw dead
        show hazuki relieved
        "Phew.. Did I do that? Well.."
        h "I need to be more careful. Bad creatures are lurking everywhere.. Just like in Tokyo."
        jump fightover


label run: 
        $ mind_strength -=1
        $ world_knowledge +=1
        show hazuki run
        h "Get out of this forest! I need to.. run!"
        scene bg forest entrance
        h "This place really is dangerous."
        h "Well, I got what i wished for, a change of worlds. and this place is like hell."
        h "Tokyo was better... I think..."
        jump fightover

label fightover:
        scene black
        with dissolve
        scene bg forest end
        show hazuki back   
        h "I guess I really need to speak to that fox and find out what is going on."
        h "The end of the forest.. finally. The mountain shrine is visible from here."
        h "It's still quite a way to go, but I know what to do now."

    # if points >= 10:
    # jump best_ending
    # elif points >= 5:
    # jump good_ending
    # elif points >= 1:
    # jump bad_ending
    # else:
    # jump worst_ending

    

















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
