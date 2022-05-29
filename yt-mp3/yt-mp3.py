from pytube import YouTube
import sys

link = input("Enter YouTube song link: ")
yt = YouTube(link)


def input_error():
    if link == "":
        print(
            "USAGE: \n",
            "   yt-mp3 [YT_LINK < 43]"
        )
        sys.exit()
    elif len(link) > 43:
        print(
            "USAGE: \n",
            "   yt-mp3 [YT_LINK < 43]"
        )
        sys.exit()


def yt_mp3():
    aud = yt.streams.get_audio_only()
    print(f"Downloading song with these parameters: {aud}")
    aud.download()
    print("Downloaded song successfully!")


if __name__ == "__main__":
    input_error()
    yt_mp3()
