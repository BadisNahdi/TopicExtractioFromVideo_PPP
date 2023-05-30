from youtube_transcript_api import YouTubeTranscriptApi
from PIPe import preprocess_classify





if __name__ == '__main__':
    url = input("Enter the video url: ")
    start_index = url.index("?v=") + 3
    end_index = url.index("&")
    video_id = url[start_index:end_index]
    Tx = YouTubeTranscriptApi.get_transcript(video_id , languages=['en'])
    Transcript = ""
    for i in Tx:
        Transcript+=(i['text'])
    preprocess_classify(Transcript)