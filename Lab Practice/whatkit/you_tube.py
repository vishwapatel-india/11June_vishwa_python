from pytubefix import YouTube
url="https://youtu.be/SuIB13fMEvY?si=wQcBOHT5JiRNX558"

YouTube(url).streams.first().download()