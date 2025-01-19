import streamlit as st
from PIL import Image



def display_dice(dice_value, container):
    image_path = f"./DiceVisualisation/assets/standard/dice_{dice_value}.png"
    try:
        img = Image.open(image_path)
        container.image(img, caption=f"Dice shows: {dice_value}")
    except FileNotFoundError:
        container.error(f"Image for dice value {dice_value} not found!")
