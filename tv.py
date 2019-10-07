from plexapi.server import PlexServer
import time

from pprint import pprint

baseurl = 'http://192.168.1.2:32400'
token = ''
plex = PlexServer(baseurl, token)

start_time = time.time()
totalsaved = 0.0
tv = plex.library.section('TV Shows')
for video in tv.search(libtype='episode', duplicate=True):
    if len(video.media) <= 2:
        saved = 0.0
        print("%s: %s %s" % (video.grandparentTitle, video.parentTitle, video.title))
        keep = video.media[0].parts[0]
        print("  Keeping:  %s, %.2f GB" % (keep.file, (keep.size / 1073741824)))
        totoss = []
        for dup in video.media[1:]:
            toss = dup.parts[0]
            print("  Deleting: %s, %.2f GB" % (toss.file, (toss.size / 1073741824)))
            totoss.append(dup)
        reply = input("\n  Delete? (y/n/q): ")
        if reply == 'y':
            for dup in totoss:
                try:
                    # Hack to make delete work
                    dup._initpath = video.key
                    dup.delete()
                    print("  Deleted %s" % dup.parts[0].file)
                    saved += dup.parts[0].size
                except:
                    print("  ERR: Unable to delete %s, rerun to try again." % dup.parts[0].file)
            totalsaved += saved
            print("  Saved %.2fGB" % (saved  / 1073741824))
        if reply == 'q':
            print("\n\nExiting... Saved %.2fGB" % (totalsaved / 1073741824))
            exit()
        print()
print("Done! Saved %.2fGB in %.2f seconds." % ((totalsaved / 1073741824), (time.time() - start_time)))
