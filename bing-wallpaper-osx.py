import urllib
import json
import tempfile
import subprocess

SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""

def set_desktop_background(filename):
    subprocess.Popen(SCRIPT % filename, shell=True)

BASE_BING_URL = "https://www.bing.com"
BING_WP_API_URL = BASE_BING_URL + "/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US"

response = json.loads(urllib.urlopen(BING_WP_API_URL).read())
wallpaper_url = BASE_BING_URL + response["images"][0]["url"]

wallpaper_file = tempfile.NamedTemporaryFile(delete=False)
wallpaper_file.write(urllib.urlopen(wallpaper_url).read())
set_desktop_background(wallpaper_file.name)
wallpaper_file.close()
