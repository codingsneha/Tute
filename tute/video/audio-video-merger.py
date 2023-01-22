import ffmpeg

input_video = ffmpeg.input('./test/test_video.webm')

input_audio = ffmpeg.input('./test/test_audio.webm')

ffmpeg.concat(input_video, input_audio, v=1, a=1).output('./processed_folder/finished_video.mp4').run()
