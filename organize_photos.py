import os
import shutil

def get_year_and_month(filename):
    creation_date = os.path.getctime(filename)
    year = str(int(creation_date // (365.25 * 24 * 60 * 60)) + 1970)
    month = str(int((creation_date % (365.25 * 24 * 60 * 60)) // (30.44 * 24 * 60 * 60)) + 1)
    return year, month

def move_photo_to_folder(src_file, dst_folder):
    shutil.move(src_file, os.path.join(dst_folder, os.path.basename(src_file)))

def organize_photos_by_year_and_month(directory, threshold):
    # Loop through all the files in the directory
    for file in os.listdir(directory):
        filename = os.path.join(directory, file)
        # Get the year and month of the photo
        year, month = get_year_and_month(filename)
        # Create a folder for the year if it doesn't exist
        year_dir = os.path.join(directory, year)
        if not os.path.exists(year_dir):
            os.makedirs(year_dir)
        # If the number of photos for the year is greater than the threshold, organize by month
        year_files = [f for f in os.listdir(year_dir) if os.path.isfile(os.path.join(year_dir, f))]
        if len(year_files) > threshold:
            month_dir = os.path.join(year_dir, month)
            if not os.path.exists(month_dir):
                os.makedirs(month_dir)
            move_photo_to_folder(filename, month_dir)
        else:
            move_photo_to_folder(filename, year_dir)

if __name__ == '__main__':
    directory = input("Enter the directory path: ")
    threshold = int(input("Enter the threshold for number of photos per year (if the number of photos per year is greater than this value, they will be organized by month): "))
    organize_photos_by_year_and_month(directory, threshold)
