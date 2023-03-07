import openai
import time
import requests
from PIL import Image
from io import BytesIO

# Set up authentication
#PASTE UR KEY HERE::
openai.api_key = "sk-xxx"

with open("yes.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    if line == "\n":
        continue
    print(line)

    # Define the prompt
    PROMPT = str(line)

    response = openai.Image.create(
        prompt=PROMPT,
        n=1,
        size="1024x1024",
    )

    ding = response["data"][0]["url"]

    # Send an HTTP GET request to the URL and get the response
    response = requests.get(ding)

    # Open the response content as an image using Pillow
    image = Image.open(BytesIO(response.content))

    # Save the image to a file in your local directory
    image.save(str(line[0:30])+".png")
