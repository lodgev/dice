# import streamlit as st
# import random
# from matplotlib import pyplot as plt
# from PIL import Image

# st.markdown("<h1 style='text-align: center;font-size: 62px; color: Blue;'>Dice Roller</h1>", unsafe_allow_html=True)

# def make_grid(cols,rows):
#     grid = [0]*cols
#     for i in range(cols):
#         with st.container():
#             grid[i] = st.columns(rows)
#     return grid
    
# m = st.markdown("""
# <style>
# div.stButton > button:first-child {
#     background-color: #0099ff;
#     color:#ffffff;
# }
# div.stButton > button:hover {
#     background-color: #1BAF14;
#     color:#ffffff;
#     }
# </style>""", unsafe_allow_html=True)

# mygrid = make_grid(3,3)  




# no=1 

# mygrid_1 = make_grid(3,5) 
# submitted = mygrid_1[2][2].button("Roll the Dice!") 
# if submitted:
# # Generates a random number
#     # between 1 and 6 (including both 1 and 6)
#     no = random.randint(1,6)

    

# if no == 1:
#     img = Image.open(r"./dice_images/dice_1.png")
#     mygrid[1][1].image(img) 

# if no == 2:
#     img = Image.open(r"./dice_images/dice_2.png")
#     mygrid[1][1].image(img)

# if no == 3:
#     img = Image.open(r"./dice_images/dice_3.png")
#     mygrid[1][1].image(img)

# if no == 4:
#     img = Image.open(r"./dice_images/dice_4.png")
#     mygrid[1][1].image(img)

# if no == 5:
#     img = Image.open(r"./dice_images/dice_5.png")
#     mygrid[1][1].image(img)

# if no == 6:
#     img = Image.open(r"./dice_images/dice_6.png")
#     mygrid[1][1].image(img)
import streamlit as st
import random
from PIL import Image

# Page Title
st.markdown("<h1 style='text-align: center;font-size: 62px; color: Blue;'>Dice Roller</h1>", unsafe_allow_html=True)

# Custom Button Style
st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0099ff;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #1BAF14;
    color:#ffffff;
}
</style>
""", unsafe_allow_html=True)


def make_grid(cols, rows):
    grid = [0] * cols
    for i in range(cols):
        with st.container():
            grid[i] = st.columns(rows)
    return grid

# displaying dice
def display_dice_image(dice_value, grid_position):
    image_path = f"./dice_images/dice_{dice_value}.png"  
    img = Image.open(image_path)
    grid_position.image(img)



# grid & buttons
dice_grid = make_grid(3, 3)

button_grid = make_grid(3, 5)
roll_button = button_grid[2][2].button("Roll the dice!")

# 2 dices
dice_1_value = 1
dice_2_value = 1

# roll the dice 
if roll_button:
    dice_1_value = random.randint(1, 6)
    dice_2_value = random.randint(1, 6)

display_dice_image(dice_1_value, dice_grid[1][0])  
display_dice_image(dice_2_value, dice_grid[1][2])  
