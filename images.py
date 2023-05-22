import openai
from dotenv import load_dotenv
import os
import requests

# Load the environment variables from the .env file
load_dotenv()

# Set the OpenAI API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def download_image(image_url, image_path):
    response = requests.get(image_url)

    with open(image_path, 'wb') as file:
        file.write(response.content)

def convert_to_rgba(image):
    with Image.open(image) as img:
        img_rgba = img.convert("RGBA")
        img_rgba.save(image)

from PIL import Image




# # Create a mask image
# mask_result = openai.Image.create(
#   prompt="A mask for a cat",
#   n=1,
#   size="1024x1024"
# )
#
# mask_url = mask_result["data"][0]["url"]
# download_image(mask_url, 'mask.png')
#
# # 1st example
# result = openai.Image.create(
#     prompt="A Cute little cat",
#     n=1,
#     size="1024x1024"
# )
#
# image_url = result["data"][0]["url"]
# download_image(image_url, 'cat.png')

convert_to_rgba("cat.png")
convert_to_rgba("mask.png")

# # 2nd example
# result = openai.Image.create_edit(
#     image=open("cat.png", "rb"),
#     mask=open("mask.png", "rb"),
#     prompt="Kitten warning a mask",
#     n=1,
#     size="1024x1024"
# )
#
# image_url = result["data"][0]["url"]
# download_image(image_url, 'cat_with_beret.png')


# 3rd example
result = openai.Image.create_variation(
    image=open("cat.png", "rb"),
    n=1,
    size="1024x1024"
)

image_url = result["data"][0]["url"]
download_image(image_url, 'cat_variation.png')
