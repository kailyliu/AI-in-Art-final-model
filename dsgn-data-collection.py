import requests 
import os 
from openai import OpenAI 
from datetime import datetime 

# Initialize OpenAI client
client = OpenAI() 

# Generate image using OpenAI API 
response = client.images.generate(
    model="dall-e-3", 
    prompt="Generate a colored, profile photo of a real lawyer on a white background. It should look similar to an ID photo. Make it look like a camera took the photo. Make sure the person looks like a real human being", 
    size="1024x1024", 
    quality="standard", 
    n=1,
)

# Extract URL from the response 
image_url = response.data[0].url

# Create a folder to save the iamges if it doesn't exist 
folder_path = "generated_images_lawyerr"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Generate a unique image name with timestamp 
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
image_name = f"generated_image_{timestamp}.jpg"
image_path = os.path.join(folder_path, image_name)

# Fetch the iamge from the url 
image_data = requests.get(image_url).content

# Save the image to the folder 
with open(image_path, "wb") as f: 
    f.write(image_data)

print("Image downloaded and saved! ")