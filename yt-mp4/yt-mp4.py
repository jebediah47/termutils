from pytube import YouTube
import sys

link = input("Enter YouTube video link: ")
yt = YouTube(link)


def input_error():
    if link == "":
        print(
            "USAGE: \n",
            "   yt-mp4 [YT_LINK < 43]"
        )
        sys.exit()
    elif len(link) > 43:
        print(
            "USAGE: \n",
            "   yt-mp4 [YT_LINK < 43]"
        )
        sys.exit()


def yt_mp4():
    vid = yt.streams.get_highest_resolution()
    vid.download()
    print(f"Completed the download of {vid}")


if __name__ == "__main__":
    input_error()
    yt_mp4()
