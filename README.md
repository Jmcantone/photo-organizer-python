# Photo organizer by year and month
This Python script organizes photos in a folder by the year of creation and, if the number of photos per year is greater than a user-specified threshold, organizes the photos by month.

#Requirements
Python 3.6 or higher

# Usage
Download the script and save it to a directory of your choice.
Open the terminal or command line and navigate to the directory where you saved the script.
Run the command python organize_photos.py and follow the on-screen instructions.
The script will organize the photos into folders by the year of creation and, if necessary, into folders by month.

# Customization
You can adjust the threshold value to control when the photos should be organized by month instead of by year. Simply enter the desired value when prompted to do so when running the script.
If you wish to customize the location of the photos, change the directory specified in the script.

# Limitations
The script currently assumes that the photos have a creation date that can be extracted from the file name. If the photos do not have a creation date in the file name, the script may not work correctly.
This script does not check if the photos are already organized into folders by year and month. If you run the script multiple times, the photos may be moved multiple times into different folders.
