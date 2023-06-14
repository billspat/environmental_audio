## using pydub http://pydub.com

from pydub import AudioSegment
import os
from time import strftime
from time import gmtime
from exiftool import ExifToolHelper
from extract_time_of_day import get_time_from_audiomoth

def milli_to_minutes(milliseconds):
    # use sprintf or something to convert to 1:10.1 or something
    len_seconds = round(milliseconds/1000,1)
    return(strftime("%H:%M:%S", gmtime(len_seconds)))
    

def clipname(filepath:str, start_secs:float, end_secs:float):
    fname, ext = os.path.basename(filepath).split(".")
    time_format = "%H:%M:%S"
    start_text = strftime(time_format, gmtime(start_secs))
    end_text = strftime(time_format, gmtime(end_secs))
    cname = f"{fname}_{start_text}-{end_text}.{ext}"
    return(cname)
 

def save_clip(audiofile, clip_start_secs, clip_end_secs, output_folder="."):
    """clips a piece of audio and saves to disk with start/end in the filename. 
    Assumes wav format, could fail at many points

    Args:
        audiofile (str): path/to/audiofile.wav 
        clip_start_secs (int): time in seconds to satr
        clip_end (_type_): _description_
        output_folder (str, optional): _description_. Defaults to ".".
    """
    
    # test if audiofile is a file
    # test if outputfolder exists

    recording = AudioSegment.from_wav(audiofile)
    
    # test if start/end is inside ths recording
    # len_milliseconds = len(recording)
    s_milli = float(clip_start_secs) * 1000
    e_milli = float(clip_end_secs) * 1000
    clip = recording[s_milli:e_milli]
    
    
    dest_filename = os.path.join(output_folder, clipname(audiofile, clip_start_secs, clip_end_secs))

    clip.export(dest_filename, type='wav')
    return(dest_filename)



def parse_clips(csv_file, output_folder = '.'):
    """ given a record, pull out the times to parse, and maybe"""
    et=ExifToolHelper()

    file_records = []
    cliplist = csv.read(csv_file)
    for row in cliplist:
        audiofile = row['something']
        # is it a file?
        if not os.path.exists(audiofile):
            print(f"could not find {audiofile}")
        starttime = row['start']
        stoptime = row['stop']
        tod = get_time_from_audiomoth(audiofile,et)
        clip_filename = save_clip(audiofile, clip_start_secs=starttime, clip_end_secs=stoptime, output_folder=output_folder)

        file_record = {}

def overlapping_slices(audiofile, output_folder=".", clip_seconds=120, overlap_seconds=15):
    """ split an audio file up into overlapping segments
    ffmpeg segement does not overlap, so using code to generate segements/windows
    
    audiofile:: full path to audio file
    output_folder: location where to put those clips, default current dir
    clip_seconds: length of clip in seconds
    overlap_seconds: overlap in seconds """
    
    if(overlap_seconds >= clip_seconds): return False

    recording = AudioSegment.from_wav(audiofile)
    # get the pieces 

    len_milliseconds = len(recording)

    num_pieces = int(len_milliseconds/( clip_seconds * 1000))  # this doesn't get the last bit! 

    for i in range(num_pieces): 
        if i == 0:
            start = 0
        else:
            start = i * (clip_seconds * 1000) - overlap_seconds * 1000
        
        # will this work to ask for time past the end of the clip to get the last bit?
        end = i + 1 * (clip_seconds * 1000)
        
        clip = recording[start:end]


    

    