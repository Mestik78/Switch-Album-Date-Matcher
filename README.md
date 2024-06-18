# Switch Album Date Matcher
 
When exporting the album from a Nintendo Switch, you will notice that the creation and modification dates of the files reflect the day you exported them, rather than the actual dates when the photos or videos were taken. This script is designed to correct the file dates so that they accurately represent the dates the media was originally captured.

Each file is located on a folder that represents the date when it was taken (`year/month/day`). Additionally, the file name contains the date and time it was taken. This script iterates through all the files, extracts the date from their names, and updates their metadata accordingly.

## Usage

1. Make sure to make a **backup** before starting.
2. Run the script with Python. It will prompt you for the album's path.
3. Input the album's path. The process will start and the script will iterate through all the files, updating their dates based on the filenames.