# downoad web page
import urllib.request as request

url = "https://en.wikipedia.org/wiki/Main_Page"
data = request.urlopen(url).read()
print(data.decode("utf8"))

# Save html file
with open("data.html","w") as fl:
    fl.write(data.decode("utf8"))
print("\n\nFinishh")
print("File saved with name (current directory): data.html\n")

