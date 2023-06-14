""" abandoned: the metamoth lib does not parse the comment, and the comment is where
the time of daty is embeeded.  See extract_time_of_day.py"""
from metamoth import parse_metadata
import os
from datetime import datetime, timezone


def get_all_audio_files(p):
    return list('a','b','c')

audiopath = '/somewhere'

audio_meta = []
for afile in get_all_audio_files(audiopath):
    audiometadata = parse_metadata(afile)
    dt = audiometadata.datetime
    tz = audiometadata.timezone

    if tz == timezone.utc:
        dt
    # convert this into something we can use



#  07:40:01 04/06/2023 (UTC+8)
# datetime.datetime(2023, 6, 4, 7, 40, 1)
# audiometadata.datetime
