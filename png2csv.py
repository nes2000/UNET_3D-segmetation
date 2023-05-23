import os
import csv

data_dir = r"D:\dataset\Images"
csv_file = r"D:\dataset\datafilter.csv"

# Open the CSV file in write mode
with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["index", "img", "target"])  # Write header row
    index=0
    # Iterate over all files in the directory
    for filename in os.listdir(data_dir):
        if filename.endswith(".png"):

            label = 0 # Replace with the actual label for the image
            if "Calc" in filename:
                label = 1
            else:
                label = 0
            # Write the image path and label to the CSV file
            writer.writerow([ index,filename, label])
            index=index+1
