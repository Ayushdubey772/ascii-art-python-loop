# Mr. Bean Face - Realistic Shape (Hairline Removed - Clean Forehead)
# Pure loops only - no ~ ~ ~ or any top hair characters

# Forehead start (smooth oval top)
for i in range(5):
    sp = 19 - i
    w  = 23 + i * 2
    print(" " * sp + "(" + " " * (w - 2) + ")")

# Eyebrows - arched
print(" " * 18 + " " * 2 + "‾‾‾‾" + " " * 5 + "‾‾‾‾" + " " * 2)
print(" " * 18 + " " * 1 + "‾‾‾‾‾" + " " * 4 + "‾‾‾‾‾" + " " * 1)

# Eyes - realistic shape with lids + iris
print(" " * 17 + "/"  + " " * 3 + "(" + " " * 2 + "●" + " " * 1 + "✦" + " " * 1 + "●" + " " * 2 + ")" + " " * 3 + "\\")
print(" " * 17 + "|"  + " " * 4 + "O" + " " * 3 + "O" + " " * 4 + "|")
print(" " * 17 + "\\" + " " * 3 + " "  + "\\" + "_" + " " * 2 + "_" + "/" + " "  + " " * 3 + "/")

# Nose - bridge + rounded tip
print(" " * 21 + "|" + " " * 7 + "|")
print(" " * 20 + "/" + " " * 9 + "\\")
print(" " * 20 + "|" + " " * 3 + "o" + " " * 3 + "|")
print(" " * 21 + "\\" + "_" + "/" + " " * 4)

# Cheeks + mouth - natural smirk
for r in range(6):
    if r == 0:
        print(" " * 15 + "/" + " " * 5 + "(" + " " * 10 + ")" + " " * 5 + "\\")
    elif r == 1:
        print(" " * 14 + "/" + " " * 6 + "‿" + " " * 1 + "‿" + " " * 6 + "\\")
    elif r == 2:
        print(" " * 13 + "/" + " " * 7 + ")" + " " * 8 + "(" + " " * 7 + "\\")
    elif r == 3:
        print(" " * 14 + "/" + " " * 18 + "\\")
    elif r == 4:
        print(" " * 15 + "\\" + " " * 16 + "/")
    else:
        print(" " * 16 + "\\" + " " * 14 + "/")

# Chin - soft rounded bottom
for i in range(6):
    sp = 20 + i
    w  = 21 - i * 2
    if i >= 4:
        print(" " * sp + " " * (w // 2 - 1) + "." + " " * (w // 2 - 1))
    else:
        print(" " * sp + ")" * w)