COLOUR_CODES = {"black": "#000000", "grey2": "#050505", "ivory1": "#fffff0", "moccasin": "#ffe4b5", "orchid": "#da70d6",
                "red1": "#ff0000", "RoyalBlue4": "#27408b", "saddlebrown": "#8b4513", "salmon": "#fa8072"}

colour = input("Enter Colour Name: ").lower()
while colour != "":
    if colour in COLOUR_CODES:
        print(colour, "is", COLOUR_CODES[colour])
    else:
        print("Invalid Colour Name")
    colour = input("Enter Colour Name: ").lower()