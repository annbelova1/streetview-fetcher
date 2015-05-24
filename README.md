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

Fetch many images without getting banned
----------------------------------------
 - Use --wait <time> --random-wait and --user-agent (-U) options in wget
 - wget --no-clobber --wait 2 --random-wait -U 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36' -i ../urls.txt
 - Run in image directory
