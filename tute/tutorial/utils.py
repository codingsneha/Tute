import os
import pyttsx3
from moviepy.editor import VideoFileClip, AudioFileClip

def generate_spoken_tutorial(transcript_path, video_path):
    audio_path = generate_audio(transcript_path)
    final_video_path = concatenate_video_audio(video_path, audio_path)
    return final_video_path

def generate_audio(transcript_path):
    if not transcript_path:
        raise ValueError("Transcript path is required")
    
    engine = pyttsx3.init()
    with open(transcript_path, 'r') as file:
        transcript = file.read()
    audio_output_path = transcript_path + "_audio.mp3"
    print(f"Generating audio file at: {audio_output_path}")
    engine.save_to_file(transcript, audio_output_path)
    engine.runAndWait()
    return audio_output_path

def concatenate_video_audio(video_path, audio_path):
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file not found: {video_path}")
    
    print(f"Loading video from: {video_path}")
    video_clip = VideoFileClip(video_path)
    print(f"Loading audio from: {audio_path}")
    audio_clip = AudioFileClip(audio_path)
    
    # Set the audio of the video clip to the audio clip
    video_clip = video_clip.set_audio(audio_clip)
    
    out_path = "final_" + os.path.basename(video_path)
    output_path = "media/final_" + os.path.basename(video_path)
    print(f"Writing final video to: {output_path}")
    video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac', temp_audiofile='temp-audio.m4a', remove_temp=False)
    return out_path