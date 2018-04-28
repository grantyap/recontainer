# Recontainer
A Python application that copies data streams through different containers without reencoding.

Recontainer is a lightweight application that simply transfers the data streams of a .mov file to an .mp4 container.
This app does not alter the data streams, which means that there is virtually zero quality loss!

## Todo
- [ ] Perform other container transformations
- [ ] Allow users to input file paths through text
- [ ] Progress bar with ETA
- [ ] Batch processing
- [ ] File error handling
- [ ] Selectable data streams
- [X] Not use ffmpeg through some weird shell hack, instead using it natively in-app
