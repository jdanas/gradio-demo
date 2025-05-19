#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Basic Gradio Demo Application

This script creates a simple Gradio interface that takes a user's name as input
and returns a personalized greeting message.

Setup Instructions:
1. Make sure you've activated your virtual environment:
   $ source venv/bin/activate
2. Install the required packages:
   $ pip install -r requirements.txt
3. Run this script:
   $ python app.py
4. Open the URL displayed in the terminal in your web browser
"""

import gradio as gr

def greet(name):
    """
    Generate a greeting message based on the input name.
    
    Args:
        name (str): The name to include in the greeting
        
    Returns:
        str: A personalized greeting message
    """
    if not name:
        return "Hello, World!"
    return f"Hello, {name}! Welcome to your first Gradio demo!"

# Create the Gradio interface
demo = gr.Interface(
    fn=greet,                     # The function to wrap
    inputs=gr.Textbox(           # Input component - a text box
        lines=1,
        placeholder="Enter your name here..."
    ),
    outputs="text",              # Output component - plain text
    title="My First Gradio Demo",
    description="Enter your name and receive a personalized greeting!",
    examples=[["John"], ["Maria"], [""]],  # Example inputs for users to try
    theme="default"              # UI theme
)

# Launch the app
if __name__ == "__main__":
    demo.launch(share=True)      # share=True creates a public link you can share with others

