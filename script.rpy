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
#choice one
    menu:

        h "Should I follow the shadowy figure?"

        "Yes, it's a chance!":
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
    scene bg river
    with fade
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

    #choice two
    menu:
        t "Can I give some advice before you go?"

        "Yes, please tell me anything.":
            jump warning

        "No, I can do this alone.":
            jump ignorant


    label warning:
        # $ menu_flag = true
        $ world_knowledge +=2
        t "Don't eat or drink anything of this realm, else you will become one of us.. Then you will truly be unable to leave."
        t "Only those who show mental strength will thrive."
        t ""
        jump turtle_continue
    label ignorant:
        # $ menu_flag = false
        t "Very well... Passing up on opportunities to learn more of this world will only slow you down.. or worse.."
        jump turtle_continue

    label turtle_continue:
    scene bg river
    with fade

    t "Let me give you a ride across the river. The mountain shrine is just beyond the forest. Beware."


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
    #choice three
    menu:
        c "Help yourself to the berries! kekeke"

        "Alright, I'll try a few.":
            jump eat_yes

        "No thanks, I'll be fine.":
            jump eat_no

    label eat_yes:
        # $ menu_flag = true
        $ mind_strength -=2
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
    h "This crane is actually a.. crow?!"
    show caw angry #crow!!
    
    c "Give me your EYES!!"
    c "Give me your soul!"
    
    scene bg forest fight
    with fade
 
 #choice four
    menu:
        "The crow is attacking me! What should I do?"

        "Fight!":
            jump fight

        "Run away!":
            jump run
        
label fight:
        $ mind_strength +=2
        $ world_knowledge -=1
        "Stay back, fiend!"
        show hazuki fight
        h "I don't owe you anything!"
        h "My eyes and my soul are mine."
        c "Caw!!"
        show caw dead
        show hazuki relieved
        "Phew.. Did I do that? Well.."
        h "I need to be more careful. Bad creatures are lurking everywhere.. Just like in Tokyo."
        h "I guess I really need to speak to that fox and find out what is going on."
        jump fightover


label run: 
        $ mind_strength -=2
        $ world_knowledge +=2
        show hazuki run
        h "Get out of this forest! I need to.. run!"
        scene bg forest entrance
        h "This place really is dangerous."
        h "Tokyo was better... I think..."
        h "I guess I really need to speak to that fox and get out of this place."
        jump fightover

label fightover:
        scene black
        with dissolve
        scene bg forest end
        show hazuki back   
        h "Ah - The end of the forest.. finally. The mountain shrine is visible from here."
        h "It's still quite a way to go, but I know what to do now."

        scene bg mountain
        with fade
        show hazuki happy 
        h "The moon is much prettier here, at least."
        h "I am feeling pretty tired though. Maybe I should get some rest. It's a long way to the top of that mountain."
        h "Hmm, maybe there's a better way to get there."
        h "I could ask somebody for help.."

#choice five
menu:
    "Should I find someone who could give some tips?"
    "Yes, let's search for that someone who can help. Maybe there's a shortcut.":
        jump search
    "No - I can do this alone. The moonlight is enough to guide me.":
        jump climb

label search:
        $ world_knowledge +=1
        $ mind_strength -=1
        show hazuki curious
        h "Maybe I can find mr turtle from earlier.. The river is just here."
        scene bg river 
        with fade
        h "I'll just search for a bit..."
        scene black
        with dissolve
        scene bg river 
        show turtle

        t "Ohoh, so you are still alive hm?"
        show hazuki happy 
        h "There you are! Yes, mr turtle, I am trying to reach the mountain top. Do you have any advice?"
        t "I see. It is indeed far."
        t "However, there is a shortcut over there, between the trees. It is quite a steep climb, but faster than the winding path."
        h "Great, so this will get me to the fox?"
        t "Yes, yes. Be on your way now."
        # reminder of advice, if true
        h "Thank you!"
        show hazuki excited
        "A shortcut - great! At least some creatures in this world are kind and helpful."
        jump climbshort


label climb:
        $ mind_strength +=2
        show hazuki angry
        h "No time to rely on others for this. I need to figure this out by myself."
        show hazuki happy
        h "Let's go!"
        jump climblong

label climbshort:
        scene bg cliff small
        h "This must be the shortcut!"
        h "Looks pretty steep.. I hope it won't take too long to climb."
        jump mountain

label climblong:
        scene bg cliff small
        h "Yikes, this is going to take a while. But I have time."
        h "Slow and steady - let's go!"
        jump mountain

label mountain:
        scene bg view
        show hazuki back
        if world_knowledge < 3:
            h "What even is this place? Talking animals, shapeshifting, weird food.."
        if world_knowledge >= 3:
            h "This world is definitely not meant for humans.. not living ones, anyway."
        if mind_strength >= 3: 
            h "But it sure is pretty."
            h "There is good and bad in everything. Every place, every person."
            h "I need to seek out the good!"
            jump climbfull
        if mind_strength < 3:
            h "Perhaps Tokyo isn't so bad afterall.."
            jump climbfull

label climbfull:
        scene mountain cliff
        show hazuki sit
        h "All this is quite overwhelming.."
        h "How did I end up here again?"
        if world_knowledge >= 2:
            h "I slipped into this realm somehow when I followed that light and the fox."
        show hazuki tired
        h "Almost there..."
        show hazuki curious
        h "I can see the shrine gate now!"
        scene bg shrine
        show hazuki happy
        h "Wow - this must be it."
        h "So many tori gates.. mysterious."
        h "And there's that blue light again.. that fox is inside here for sure."
        jump scenesix


# scene six 
label scenesix:
        scene black
        with dissolve
        scene bg shrine 
        show hazuki back
        h "I'm going to find you, spirit fox."
        scene bg fox room
        show kitsune smile
        k "A human? Ah - perhaps the sad girl who longed to leave her city?"
        h "So you remember me? You invited me to this 'new world'..."
        k "Indeed, indeed."
        show kitsune tea
        k "Well, make yourself comfortable and have some tea and mochi. You must be tired"
        h "Oh, finally some refreshing food!"
#choice six
        menu: 
            "Shall I eat the snacks?"
            "Yes- It looks delicious! This will boost my energy.":
                jump eatyes
            "No way! This looks like a trap.. ":
                jump eatno 

label eatyes:
        show kitsune happy
        k "Great, help yourself. Consider it a welcome to this world."
        "Sounds a bit suspicious.."
        "But it looks so delicious, I'll eat up! "
        show hazuki happy
        h "Thank you!"
        $ mind_strength -= 3
        $ world_knowledge -= 1
        jump continue1

label eatno:
        show hazuki angry
        "Way too suspicious.. I think I'll never leave if I eat this."
        "I'm so hungry, but that will have to wait"
        h "No thank you.. I'll pass."
        $ mind_strength += 2
        $ world_knowledge += 1
        jump continue1
    

label continue1:
        show kitsune happy
        k "Very well.."
        k "This realm must feel quite different to your human city life."
        if world_knowledge >3:
            h "It sure is. "
            h "But it's similar in that it's full of lost souls.."
        else:
            h "Sure. It's completely different."
#choice seven
        menu:
            "Do you know why I summoned you here?"
            "Because you are EVIL?":
                jump evilyes
            "Because I wanted to come here.":
                jump evilno

label evilyes:
        show hazuki angry
        show kitsune smile
        k "kekeke, perhaps so."
        jump evilcontinue

label evilno:
        $ mind_strength +=1
        show hazuki beach
        show kitsune smile
        jump evilcontinue



label evilcontinue:
        k "What did you learn about this world?"
        h "It's hard to know who to trust here.. Some may seem kind, but are actually snakes."
        if world_knowledge >=3 :
            h "...or ghosts?"
        k "So you met some deceptive creatures, hmm? Is your human city better?"
        h "..."
        h "Hah, not really. Plenty of sly creatures there too."
        h "But in this world I learnt that there is 'bad' or darkness in everything. Every person, every place."
        h "I need to focus on seeking out the 'good' and the light in the world."
        if mind_strength >3:
            h "I've been too focused on negativity.. but not anymore!"
        k "Interesting.."
#choice eight
        menu:
            k "So.. Are you ready to return home?"
            "Yes, get me out of this place. I have more hope for the city now.":
                jump downset_day_escape
            "Actually I quite like this place.. I'll stay":
                jump downset_day_remain
label downset_day_escape:
            if mind_strength >= 5:
                jump goodending_escape
            else: 
                jump badending_remain

label downset_day_remain:
            if world_knowledge >= 3:       
                jump goodending_remain
            else:
                jump badending_curse

# success, escape
label goodending_escape:
    show kitsune happy
    k "Very few human souls that fall into the afterlife make it this far."
    k "And even fewer of those manage to return to their mortal lives."
    k "You fought well. And hopefully learnt some life lessons too."
    show hazuki happy
    h "I sure did."
    h "You won't see me here again for a long time."
    show kitsune happy
    k "kekeke, well you know where to go next time. Farewell, lonely girl."
    show hazuki happy
    h "I'm going to give my city another chance. Goodbye!"
    "{b}Hopeful Ending{/b}."
    scene bg city 
    show hazuki back
    scene black
    with dissolve
    return
    


# success, remain
label goodending_remain:
    show kitsune happy
    k "Very few human souls that fall into the afterlife make it this far."
    k "I admire your strength."
    h "Thank you - I am curious to discover more about the wonders of this realm."
    k "The decision cannot be undone, but you will forget your old life in time anyway."
    show hazuki happy
    h "Good. I chose this path, and I stand by it."
    k "Hm, well you know where to find me..."
    h "This was all in my plan. I got what I wished for."
    "{b}Strong Ending{/b}."
    scene bg river 
    show hazuki back
    scene black
    with dissolve
    return
    


# failure, remain
label badending_remain:
    scene bg shrine
    show kitsune angry
    k "Very few human souls that fall into the afterlife make it this far."
    k "And even fewer of those manage to return to their mortal lives."
    k "You are one of those who will remain here for eternity."
    show hazuki scared
    h "What are you saying? This is... really hell?"
    show kitsune happy
    k "So naive. So slow. What a weak, weak mortal. How do you trust so easily?"
    show caw 
    c "kekeke!"
    c"Once you fall into the afterlife, you can't simply leave."
    c"Before you know it, you will become what you hated and feared the most.. A lost soul."
    show hazuki surprised
    h "That crow?! You are not the fox at all!!"
    show hazuki scared
    h "Wait... I.. This world is not what I imagined."
    c"You got exactly what you wished for."
    show caw happy
    c"Farewell."
    "{b}Trapped Ending{/b}."
    scene black
    with dissolve
    return

# failure, curse
label badending_curse:
    show kitsune angry
    k "You think it will be nice to stay here?"
    k "kekeke"
    k "Turning to the afterlife is not an easy way out"
    show hazuki scared
    h "Afterlife? This is... really hell?"
    show kitsune happy
    k "Weak, weak mortal. You will regret your choice to stay."
    k "Before you know it, you will become what you hated and feared the most.. A lost soul."    
    show hazuki scared
    h "Wait... I.. This world is not what I imagined."
    k "Well, You got exactly what you wished for."
    k "Farewell."
    "{b}Cursed Ending{/b}."
    scene black
    with dissolve
    return
    

        
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
