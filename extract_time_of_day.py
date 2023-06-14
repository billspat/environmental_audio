import csv
from exiftool import ExifToolHelper

# constants

file_path_key = 'obs_file_path'
time_of_day_key = 'time_of_day'


def get_time_from_audiomoth(audiofile, et=ExifToolHelper())->str:
    """ pull the time of day string from an audio moth file"""

    exifkey = "RIFF:Comment"
    comment = et.get_tags(audiofile, exifkey)[0][exifkey]
    time_of_day = comment.split(' ')[2]
    return(comment)

def extract_time_of_day_csv(filelist:list)->list:
    """ for each file in the list, pull t of d as string"""
    filelist = [] # list of files and paths

    file_records = [{file_path_key: f} for f in filelist]
    audiofile="20230604_074001.WAV"

    with ExifToolHelper() as et:
        file_records = [{file_path_key: f, time_of_day_key: get_time_from_audiomoth(f,et)} for f in filelist]

    return(file_records)


def write_file_records(file_records,csvfilename):

    fieldnames = [file_path_key,time_of_day_key]
    
    with open(csvfilename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writeheader()
        writer.writerows(file_records)
    
    return(True)


if __name__ == "__main__":
    """ read all files in folder, write csv file of [filename, time_of_day]"""
    import sys
    audiopath = sys.argv[1]
    csv_file_name = sys.argv[2]

    ###### TODO WALK DIRECTORIES ##########
    
    filelist = [audiopath] # get all the files and subfolder path :(
    file_records = extract_time_of_day_csv(filelist)
    result = write_file_records(file_records, )
    if (not result):
        exit(1)

    

