# ==========================================
# - Only loops and functions
# ==========================================

# --------- Function to print empty space ----------
def print_space(count):
    for i in range(count):
        print(" ", end="")

# --------- Function to print hash characters ----------
def print_hash(count):
    for i in range(count):
        print("#", end="")

# --------- Function to print newline ----------
def new_line():
    print()

# --------- Top Head ----------
def head_top():
    for i in range(3):
        print_space(14)
        print_hash(11)
        new_line()

# --------- Upper Face ----------
def upper_face():
    for i in range(2):
        print_space(10)
        print_hash(19)
        new_line()

# --------- Forehead ----------
def forehead():
    print_space(7)
    print_hash(6)
    print_space(3)
    print_hash(9)
    print_space(3)
    print_hash(6)
    new_line()

# --------- Face Sides ----------
def face_sides():
    for i in range(2):
        print_space(5)
        print_hash(5)
        print_space(6)
        print_hash(9)
        print_space(6)
        print_hash(5)
        new_line()

# --------- Eyes ----------
def eyes():
    print_space(4)
    print_hash(4)
    print_space(2)
    print_hash(3)
    print_space(4)
    print_hash(3)
    print_space(2)
    print_hash(4)
    new_line()

# --------- Eye Detail ----------
def eye_detail():
    print_space(4)
    print_hash(4)
    print_space(2)
    print_hash(1)
    print_space(1)
    print_hash(1)
    print_space(4)
    print_hash(1)
    print_space(1)
    print_hash(1)
    print_space(2)
    print_hash(4)
    new_line()

# --------- Nose ----------
def nose():
    for i in range(2):
        print_space(11)
        print_hash(3)
        new_line()

# --------- Mouth ----------
def mouth():
    print_space(8)
    print_hash(9)
    new_line()

# --------- Smile ----------
def smile():
    print_space(7)
    print_hash(11)
    new_line()

# --------- Chin ----------
def chin():
    print_space(9)
    print_hash(7)
    new_line()

# --------- Lower Face ----------
def lower_face():
    for i in range(2):
        print_space(6)
        print_hash(13)
        new_line()

# --------- Neck ----------
def neck():
    for i in range(2):
        print_space(11)
        print_hash(3)
        new_line()

# --------- Collar ----------
def collar():
    print_space(8)
    print_hash(9)
    new_line()

# --------- Body Top ----------
def body_top():
    for i in range(3):
        print_space(6)
        print_hash(13)
        new_line()

# --------- Body Middle ----------
def body_middle():
    for i in range(4):
        print_space(5)
        print_hash(15)
        new_line()

# --------- Body Bottom ----------
def body_bottom():
    for i in range(3):
        print_space(6)
        print_hash(13)
        new_line()

# --------- Base ----------
def base():
    print_space(7)
    print_hash(11)
    new_line()

# --------- Signature ----------
def signature():
    new_line()
    print("       ASCII ART : MR. BEAN")
    print("       Created using Loops & Functions")
    print("       Minor Project - Python")

# --------- Main Function ----------
def draw_mr_bean():
    head_top()
    upper_face()
    forehead()
    face_sides()
    eyes()
    eye_detail()
    nose()
    mouth()
    smile()
    chin()
    lower_face()
    neck()
    collar()
    body_top()
    body_middle()
    body_bottom()
    base()
    signature()

# --------- Program Execution ----------
draw_mr_bean()
