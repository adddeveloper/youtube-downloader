# youtube downloader mp3/mp4

Download youtube videos as mp3 or mp4 using python, which you can turn to .exe to run on any computer.

The `youtube_downloader.py` file is the python file, and you need to download these:

```
pip install pytube
pip install pyinstaller
```

The pyinstaller is used:

```
pyinstaller --onefile youtube_downloader.py
```

That turns the python file into an executable `.exe` file that can be found in the `dist` folder.

I provided the `youtube_downloader.exe` file in the `dist` of this repo.
