from pymediainfo import MediaInfo
import os

# Track Object
class Video:
    def __init__(self, file, codec, frame_rate, width, height, size):
        self.file = file
        self.codec = codec
        self.frame_rate = frame_rate
        self.width = width
        self.height = height
        self.size = size

    # Determine if the Video is 'better than' a given video
    def better_than(self, other):
        if self.width > other.width:
            return 1
        elif (self.width == other.width) & (self.height > other.height):
            return 1
        elif (self.width == other.width) & (self.height == other.height):
            if self.size > other.size:
                return 1
        else:
            return 0

    # Return Video represented as JSON
    def to_data(self):
        data = {
            'file' : self.file,
            'codec' : self.codec ,
            'frame_rate' : self.frame_rate,
            'width' : self.width,
            'height' : self.height,
            'size' : self.size
        }
        return data

# Given list of media files, return one with best quality
def best_version(media_list):
    bestv = Video('', '', 0, 0, 0, 0)
    for media in media_list:
        media_info = MediaInfo.parse(media, "/usr/local/lib/libmediainfo.0.dylib")
        for track in media_info.tracks:
            if track.track_type == 'Video':
                tempv = Video(media, track.encoded_library_name, track.original_frame_rate,
                              track.width, track.height, os.path.getsize(media))
                if tempv.better_than(bestv):
                    bestv = tempv
    if bestv.size != 0:
        return bestv.to_data()
    else:
        return {}