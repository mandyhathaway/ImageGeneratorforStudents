# -*- coding: utf-8 -*-
"""Image Generator for Camp as app with notes.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15EHsWecvsiryVzXUpWOZOBTj2iuu6Bxr
"""

# Import PyTorch library for tensor computations and GPU support
import torch

# Import classes for loading and running Stable Diffusion
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler

# Import Gradio for creating a web interface
import gradio as gr

# Clear unused memory from the GPU to prevent memory errors
torch.cuda.empty_cache()

# SpecifY the model name to load from Hugging Face
model_id = "stabilityai/stable-diffusion-2-1"

# Load the Stable Diffusion model with half-precision floats
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)

# Replace the default scheduler with a more efficient one
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)

# Move the model to the GPU for faster processing
pipe = pipe.to("cuda")

# (Commented out) Example prompt for image generation
#prompt = "a bedroom in a green lush forest with moss and vines hanging down from the tree tops, and a mossy forest floor covred in moss and stumps, photo realistic"

# Define a function that generates an image from a text prompt
def generate_image(prompt):
    # Generate an image of specified size and gets the first result
    image = pipe(prompt, width = 1000, height=1000).images[0]
    # Return the generated image
    return image

# Set up the Gradio web interface with text input and image output
gr.Interface(
    fn = generate_image,  # Set the function to call when a prompt is entered
    inputs = "text",  # Input type is text
    outputs = "image",  # Output will be an image
    title = "My Personal Stable Diffusion Generator",  # Title of the web interface
    description = "Enter a prompt to bring your imagination to life!"  # Description shown on the interface
).launch()  # Launches the Gradio web interface