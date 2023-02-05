import ffmpeg
 
input_video = ffmpeg.input("D:/Coding/Tute/tute/video/test.mp4")

input_audio = ffmpeg.input("D:/Coding/Tute/tute/video/test.mp3")

ffmpeg.concat(input_video, input_audio, v=1, a=1).output("output.mp4").run()