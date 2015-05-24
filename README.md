- [x] script to generate images and fetch them in python
- [x] manually inspect downloaded images
- [ ] update crawler to choose images efficiently using zoom/orientation
- [ ] fetch many images without getting banned

Script to generate images and fetch them in python
--------------------------------------------------
 - just use wget -i <file-with-images-list-in>

Update crawler to choose images efficiently using zoom/orientation
-----------------------------------------------------------------
 - Use almost highest fov when fetching so we get decent zoom
 - Use headings in 60-80deg arc from perpendicular to heading, saves half
   of total image fetchings
 - Experiment with different zooms for different arc sections
