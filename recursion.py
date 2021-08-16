import urllib.request
import json

exec(urllib.request.urlopen(json.loads(urllib.request.urlopen("https://api.github.com/repos/ajswafford07/recursion/contents/recursion.py?ref=master").read())["download_url"]).read())
