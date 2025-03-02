# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Cairn", color="#ff4040")
define m = Character("Makoto", color="#e4439c")


transform left:
    xalign 0.1 yalign 1.0

transform right:
    xalign 0.9 yalign 1.0

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene forest

    show cairn_happy at left 

    # These display lines of dialogue.

    c "Testing testing!"

    m "Testing testing!"

    # This ends the game.

    return
