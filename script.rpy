# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Hazuki")


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



    # This ends the game.

    return
