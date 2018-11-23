# This code will be able to print and use ANSI escape sequences for colour printing.
colours = {
    "black":    0,
    "red":      1,
    "green":    2,
    "yellow":   3,
    "blue":     4,
    "magenta":  5,
    "cyan":     6,
    "white":    7,
}

# Print an ANSI escape sequence and text
def ansi_code(text):
    print(
        chr(27)+text,
        end="",
        flush=True
    )

# Will clear the screen
def clear():
    ansi_code("[2J")

# set the graphics mode of the terminal
def set_graphics_mode(code):
    ansi_code("["+str(code)+"m")

# Make the text background this colour
def set_background(colour):
    # Background colour codes are offset by 40
    code = colours[colour] + 40
    set_graphics_mode(code)

# Make text this colour
def set_text(colour):
    # foreground colour codes are offset by 30
    code = colours[colour] + 30
    set_graphics_mode(code)

# Abstraction of functions to call like a print statement.
def colour_print(
        text,
        end="\n",
        flush=False,
        bg="black",
        tx="white"
):
    set_background(bg)
    set_text(tx)
    print(text,end=end,flush=flush)
    # Clear set colours
    set_graphics_mode(0)