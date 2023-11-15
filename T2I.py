import os
import shutil
import pandas as pd

# Dataset
dataset_folder = "images/images"
output_folder = "Desktop/test"
# Creating the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)


# input text
input_text = "Pikachu driving a car, Squirtle eating ice cream, Deerling is laughing, Chandelure is sleeping."

# Read the CSV file into a DataFrame
csv_file_path = "pokemon.csv"  # CSV for image context
data_df = pd.read_csv(csv_file_path)

# Extract potential keys from the input text
potential_keys = [name.capitalize() for name in data_df["Name"] if name.capitalize() in input_text]


for response in potential_keys:
    image_filename = f"{response}.png"
    image_path = os.path.join(dataset_folder, image_filename)

    if os.path.exists(image_path):
        output_path = os.path.join(output_folder, image_filename)
        shutil.copy(image_path, output_path)
        print(f"Image saved for {response} at {output_path}")
    else:
        print(f"Image not found for {response}")
