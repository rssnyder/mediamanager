# mediamanager

## Goal

Use Plex API to audit duplicate movies and tv shows, provide the user with the ability to delete the lesser quality file.

## Usage

Set `PLEX_SERVER` and `PLEX_TOKEN` in your environment. Server should be in format of `http://myurlOrIPhere:32400` and token can be recived from [here](https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/)

### Movies

```python movies.py```

This is interactive, it will present you with the operation to be completed and you can accept, deny, or quit the program. It will also display disk space saved per item and total from the current run when it is completed.

```
riley@t480:~/Documents/mediamanager$ python movies.py 
A-X-L
  Keeping:  /media/Movies/2018/A.X.L. (2018)/A-X-L (2018) Bluray-1080p.mkv, 7.65 GB
  Deleting: /media/Movies/A.X.L. (2018)/A-X-L (2018) Bluray-1080p.mp4, 1.59 GB

  Delete? (y/n/q): n

A.I. Artificial Intelligence
  Keeping:  /media/Movies/2001/AI Artificial Intelligence/A.I.Artificial.Intelligence.2001.1080p.BluRay.DL.mp4, 2.00 GB
  Deleting: /media/Movies/2019/A.I. Artificial Intelligence (2001)/A.I. Artificial Intelligence (2001) Bluray-1080p Proper.mp4, 2.78 GB

  Delete? (y/n/q): n

Addams Family Values
  Keeping:  /media/Movies/2019/Addams Family Values (1993)/Addams Family Values (1993) Bluray-1080p.mp4, 1.80 GB
  Deleting: /media/Movies/1993/Addams Family Values/Addams.Family.Values.1993.720.Web-DL.DL.mkv, 0.68 GB

  Delete? (y/n/q): y
  Deleted /media/Movies/1993/Addams Family Values/Addams.Family.Values.1993.720.Web-DL.DL.mkv
  Saved 0.68GB

Amélie
  Keeping:  /media/Movies/Amélie (2001)/Amélie (2001) Bluray-1080p.mkv, 11.29 GB
  Deleting: /media/Movies/2001/Amelie/Amelie.2001.720p.BluRay.DL.mkv, 0.68 GB

  Delete? (y/n/q): q


Exiting... Saved 0.68GB
```

## TV Shows

```python tv.py```

This is interactive, it will present you with the operation to be completed and you can accept, deny, or quit the program. It will also display disk space saved per item and total from the current run when it is completed. The difference here is that if you skip (n) it will log this skip, and on the next run it will not prompt you for this entry. This was to help with shows you dont want to delete yet, but also do not want to fix (laziness).

The output is the same as for movies.

## TODO

 - Add option to split selection
