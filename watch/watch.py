import re
import sys


def main():
    print(parse(input("HTML: ")))


# stage 3
def Convert(link):
    rc = None

    matches = re.search(r"^(.+)embed/(.+)$", link)
    if matches:
        first, second = matches.groups()
        rc = "https://youtu.be/" + second

    return rc


# stage 2
def Match(link):
    rc = None

    if re.match(
        r"""
        ^
        (http://)|(https://)(www.)?(youtube.com/embed/).+
        $
        """, link, flags=re.VERBOSE
    ):
        rc = Convert(link)

    return rc


# stage 1
def Clean(link):
    rc = None

    match = re.match(
        r"""
        <iframe [^>]*src="([^"]+)
        """, link, flags=re.VERBOSE
    )
    if match:
        rc = Match( match.group(1) )

    return rc


# interface
def parse(s):
    rc = Clean(s)
    return rc


if __name__ == "__main__":
    main()
