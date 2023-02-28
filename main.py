from datetime import date

from pytube import YouTube

from application.salary import calculate_salary
from application.db.people import get_employees


def print_date():
    """print current date"""
    today = date.today()
    print("Today's date:", today.strftime("%d.%m.%Y"))

def download_from_YouTube():
    """Download video from YouTube"""
    link = input("Input YouTube video URL: ")
    if link:
        yt = YouTube(link)
        res = yt.streams.get_highest_resolution()
        print("Downloading ...")
        res.download("./YouTubeVideos/")
        print(f"Title: {yt.title}, has downloaded.")

if __name__ == '__main__':
    print_date()
    calculate_salary()
    get_employees()
    download_from_YouTube()


