import os
import shutil

def organize_photos_by_year_and_month(directory, threshold):
    # Loop through all the files in the directory
    for file in os.listdir(directory):
        # Get the creation date of the file
        creation_date = os.path.getctime(os.path.join(directory, file))
        year = str(int(creation_date // (365.25 * 24 * 60 * 60)) + 1970)
        month = str(int((creation_date % (365.25 * 24 * 60 * 60)) // (30.44 * 24 * 60 * 60)) + 1)
        # Create a folder for the year if it doesn't exist
        if not os.path.exists(os.path.join(directory, year)):
            os.makedirs(os.path.join(directory, year))
        # If the number of photos for the year is greater than the threshold, organize by month
        year_dir = os.path.join(directory, year)
        year_files = [f for f in os.listdir(year_dir) if os.path.isfile(os.path.join(year_dir, f))]
        if len(year_files) > threshold:
            if not os.path.exists(os.path.join(year_dir, month)):
                os.makedirs(os.path.join(year_dir, month))
            shutil.move(os.path.join(directory, file), os.path.join(year_dir, month, file))
        else:
            shutil.move(os.path.join(directory, file), os.path.join(year_dir, file))

if __name__ == '__main__':
    directory = input("Enter the directory path: ")
    threshold = int(input("Enter the threshold for number of photos per year (if the number of photos per year is greater than this value, they will be organized by month): "))
    organize_photos_by_year_and_month(directory, threshold)
