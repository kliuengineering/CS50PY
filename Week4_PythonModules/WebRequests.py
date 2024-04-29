import requests
import json
import sys

def GrabItunesAPI(argv):
    response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + argv)
    # return json.dumps( response.json() )
    return response.json()


def GetTrack(data):

    array_track = []

    for itr in data["results"]:
        array_track.append( itr["trackName"] )

    return array_track


def Print(data):
    for itr in data:
        print(itr)


def main():

    if len(sys.argv) < 2:
        sys.exit()
    argv = sys.argv[1] + " " + sys.argv[2]

    data = GrabItunesAPI(argv)
    # print(data)
    Print( GetTrack(data) )


main()
