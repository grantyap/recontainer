# Recontainer
A Python application that copies data streams through different containers without re-encoding.

Recontainer is a lightweight application that simply transfers the data streams of a .mov file to an .mp4 container.
This app does not alter the data streams, which means that there is virtually zero quality loss!

## Install
Install dependencies with
```
pip install -r requirements-latest.txt
```
You can run this with `python3 recontainer.py` or you can build an app bundle with
```
pyinstaller recontainer.spec
```
The app bundle is created in `dist/`

## Todo
- [X] Not use FFmpeg through some weird shell hack, instead using it natively in-app
- [ ] Not use CLI FFmpeg, instead forcing myself to learn to use libav
- [ ] Perform other container transformations
- [ ] Allow users to input file paths through text
- [ ] Progress bar with ETA
- [ ] Batch processing
- [ ] File error handling
- [ ] Selectable data streams
