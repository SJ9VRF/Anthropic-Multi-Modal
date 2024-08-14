# Main script to run your application logic.

# src/main.py
from anthropic_api import AnthropicAPI
from image_loader import load_directory_images
from structured_output import TickerList

def main():
    api_key = 'Your ANTHROPIC_API_KEY_here'
    anthropic = AnthropicAPI(api_key)

    image_documents = load_directory_images('../data/images/')
    prompt = "Describe the images as an alternative text"

    response = anthropic.complete(prompt, image_documents)
    print(response)

if __name__ == "__main__":
    main()
