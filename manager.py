import os, sys, getopt
import media
import re
from guessit import guessit
from pytvdbapi import api

video_types = ('.mkv', '.webm', '.wmv', '.flv', '.avi', '.mov',
               '.mp4', '.m4a', '.m4v', '.f4v', '.f4a', '.m4b', '.m4r',
               '.f4b', '.3gp', '.3gp2', '.3g2', '.3gpp', '.3gpp2',
               '.ogg', '.oga', '.ogv', '.ogx', '.wma')

def find_duplicates(episodes):
    finished = []
    for episode in episodes:
        # Look for other episodes in this season
        ep = 0
        if isinstance(episode['episode'], int):
            ep = episode['episode']
        else:
            ep = episode['episode'][1]

        if ep in finished:
            print('Already did episode ', ep)
            continue
        dups = [i['path'] for i in episodes if (ep == i['episode'])]
        if len(dups) < 2:
            # No Dups
            continue
        else:
            #episodes = [i for i in episodes if i not in dups]

            # Get best version
            best = media.best_version(dups)
            print('Keep: ' + best['file'])
            to_delete = [i for i in dups if i not in best['file']]
            print(to_delete)
            finished.append(ep)
            #for bad in to_delete:
            #    print("Delete: " + bad)
            #    if os.path.exists(bad):
            #        os.remove(bad)
            #        finished.append(episode_number)
            #    else:
            #        print("The file was already deleted")

if __name__ == "__main__":
    os.chdir('/Volumes/Media/TV Shows')
    root = os.getcwd()

    # Scan child directories
    with os.scandir(root) as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_dir() and not (entry.name == '24') and not (entry.name == 'Adventure Time'):
                # Enter TV Show Directory
                print('Checking Out ' + entry.name + '...')
                os.chdir(entry.name)

                # Get all video files
                video_files = []
                for subdir, dirs, files in os.walk(os.getcwd()):
                    for file in files:
                        if file.endswith(video_types):
                            video = os.path.join(subdir, file)
                            data = guessit(video.split('/')[-1])
                            try:
                                if ('season' in data) and ('episode' in data):
                                    data['path'] = video
                                    video_files.append(data)
                            except KeyError:
                                data = {}

                # Get video files for each season and look for dups
                for i in range(20):
                    this_season = []
                    print(i)
                    for video in video_files:
                        if video['season'] == i:
                            this_season.append(video)
                    find_duplicates(this_season)

                os.chdir(root)
