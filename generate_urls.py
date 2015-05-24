# Open panorama file which has the format
# <google-panorama-id>\t<lat>\t<lng>
# ...

from urllib.parse import urlencode
import sys

API_KEY = open('google_maps_key.txt').read().strip() 
# The number of degrees we need to get clear signs
FOV_DEG = 25
# String parameter for image size - always max
IMG_SIZE = '600x600'

SV_IMG_URL = 'https://maps.googleapis.com/maps/api/streetview'

crawler_file = sys.argv[1]


def generate_view_urls(pid, heading):
    # LatLng isn't needed for these, since we have pano data
    params = {
        'pano': pid,
        'size': IMG_SIZE,
        'fov': FOV_DEG,
        'key': API_KEY
    }

    # The lowest angle perpendicular to the heading
    perp_heading = (float(heading) + 90) % 180

    # Fan out evenly from perpendicular angle
    fanned_headings = [
        perp_heading - 2 * FOV_DEG,
        perp_heading - 1 * FOV_DEG,
        perp_heading,
        perp_heading + 1 * FOV_DEG,
        perp_heading + 2 * FOV_DEG
    ]

    # Add headings from opposite side of the road
    fanned_headings += [h + 180 for h in fanned_headings]

    # Capture all headings at 30deg increments
    for h in fanned_headings:
        params['heading'] = h
        print('{0}?{1}'.format(SV_IMG_URL, urlencode(params)))


with open(crawler_file) as panoramas:
    # Each line is laid out as pid, lat, lng, heading
    for p in panoramas:
        pid, lat, lng, heading = p.split()
        generate_view_urls(pid, heading)
