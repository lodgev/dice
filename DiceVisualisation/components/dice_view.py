import streamlit as st
from PIL import Image

def display_dice(dice_value, col):
    """
    Відображає зображення кубика відповідно до його значення.
    """
    image_path = f"./DiceVisualisation/assets/standard/dice_{dice_value}.png"
    try:
        img = Image.open(image_path)
        col.image(img, caption=f"Dice shows: {dice_value}", width=150, output_format="PNG")
    except FileNotFoundError:
        col.error(f"Image for dice value {dice_value} not found!")
