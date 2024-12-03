import os
import requests

# Define fashion categories and their corresponding directories
categories = {
    0: 'Casual',
    1: 'Formal',
    2: 'Bohemian',
    3: 'Streetwear',
    4: 'Athleisure'
}

# Define gender subcategories
genders = ['Male', 'Female']

# Function to download and save an image
def download_image(image_url, save_dir, image_name):
    try:
        response = requests.get(image_url, stream=True)
        response.raise_for_status()  # Check if the request was successful
        with open(os.path.join(save_dir, image_name), 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {image_name} to {save_dir}")
    except requests.RequestException as e:
        print(f"Failed to download {image_url}. Error: {e}")

# Function to scrape image URLs (placeholder function, update with real scraping logic)
def scrape_image_urls(category, gender):
    # Placeholder URLs; replace with actual image URL extraction logic
    placeholder_urls = {
        (0, 'Male'): ['https://via.placeholder.com/150?text=Casual_Male1', 'https://via.placeholder.com/150?text=Casual_Male2'],
        (0, 'Female'): ['https://via.placeholder.com/150?text=Casual_Female1', 'https://via.placeholder.com/150?text=Casual_Female2'],
        (1, 'Male'): ['https://via.placeholder.com/150?text=Formal_Male1', 'https://via.placeholder.com/150?text=Formal_Male2'],
        (1, 'Female'): ['https://via.placeholder.com/150?text=Formal_Female1', 'https://via.placeholder.com/150?text=Formal_Female2'],
        (2, 'Male'): ['https://via.placeholder.com/150?text=Bohemian_Male1', 'https://via.placeholder.com/150?text=Bohemian_Male2'],
        (2, 'Female'): ['https://via.placeholder.com/150?text=Bohemian_Female1', 'https://via.placeholder.com/150?text=Bohemian_Female2'],
        (3, 'Male'): ['https://via.placeholder.com/150?text=Streetwear_Male1', 'https://via.placeholder.com/150?text=Streetwear_Male2'],
        (3, 'Female'): ['https://via.placeholder.com/150?text=Streetwear_Female1', 'https://via.placeholder.com/150?text=Streetwear_Female2'],
        (4, 'Male'): ['https://via.placeholder.com/150?text=Athleisure_Male1', 'https://via.placeholder.com/150?text=Athleisure_Male2'],
        (4, 'Female'): ['https://via.placeholder.com/150?text=Athleisure_Female1', 'https://via.placeholder.com/150?text=Athleisure_Female2']
    }
    return placeholder_urls.get((category, gender), [])

# Main function to orchestrate image downloading
def main():
    # Create directories for each fashion category and gender
    for category_id, category_name in categories.items():
        for gender in genders:
            save_dir = os.path.join(category_name, gender)
            os.makedirs(save_dir, exist_ok=True)

    # Download images for each category and gender
    for category_id, category_name in categories.items():
        for gender in genders:
            image_urls = scrape_image_urls(category_id, gender)
            for idx, image_url in enumerate(image_urls):
                download_image(image_url, os.path.join(category_name, gender), f"{category_name}_{gender}_{idx+1}.jpg")

if __name__ == '__main__':
    main()
