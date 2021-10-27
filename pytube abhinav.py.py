from pytube import YouTube
 
#youtube_video_url = 'https://www.youtube.com/watch?v=DkU9WFj8sYo'
youtube_video_url = 'https://www.youtube.com/watch?v=4qv3iwTa65A&t=24s'
try:
    yt_obj = YouTube(youtube_video_url)
 
    filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
 
    # download the highest quality video
    filters.get_highest_resolution().download()
    print('Video Downloaded Successfully')
except Exception as e:
    print('Not downloaded')
