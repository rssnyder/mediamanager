from plexapi.server import PlexServer
import time
#baseurl = 'http://192.168.1.2:32400'
baseurl = 'http://207.45.83.202:32400'
token = ''
plex = PlexServer(baseurl, token)

start_time = time.time()
saved = 0.0
tv = plex.library.section('TV Shows')
for video in tv.search(libtype='episode', duplicate=True):
    if len(video.media) > 2:
        size = 0.0
        for dup in video.media:
            toss = dup.parts[0]
            print("  %s:  %s, %.2f GB" % (video.grandparentTitle, toss.file, (toss.size / 1073741824)))
            size += toss.size
        print("  Total size: %.2f\n\n" % (size / 1073741824))
    continue

    print("%s - %s" % (video.grandparentTitle, video.title))
    keep = video.media[0].parts[0]
    print("  Keeping: %s, %.2f GB" % (keep.file, (keep.size /  1073741824)))
    for dup in video.media[1:]:
        toss = dup.parts[0]
        print("  Deleting:  %s, %.2f GB" % (toss.file, (toss.size / 1073741824)))
        try:
            dup._initpath = video.key
            #dup.delete()
            saved += toss.size
        except:
            print("ERR: Unable to delete %s, rerun to try again." % toss.file)
    break
print("Done! Saved %.2fGB in %.2f seconds." % ((saved / 1073741824), (time.time() - start_time)))
