<img width="24" alt="favicon" src="https://user-images.githubusercontent.com/79274516/208621370-d39bdb26-2df4-4bc3-8d14-7009fe3b3f2f.png">**te**

<br>

Checkout the sample backend programs!
Go to **tute** > **templates**. Run any of the sample python programs and the text will be synthesized to audio and played.
The following video shows how to run the sample tts programs.

https://user-images.githubusercontent.com/79274516/208628818-38f2e0ac-3feb-470c-a82b-2f63a20ce285.mp4




<br>

*---The project is currently under development for stable release---*

<br><br>


<img align = "left" width="80" alt="image" src="https://user-images.githubusercontent.com/79274516/208631243-ce1d8e4d-ef81-402a-b5b8-9f6c85c0d784.png">

<h3>Technologies used</h3>

<br>
Tute uses text to speech synthesizer **pyttsx3** to convert text to audio
And the free and open-source-software **ffmpeg** to add the audio to a video file.
<br><br>
  Back-end: Python (pyttsx3 & Django)<br><br>
  Front-end: html, css, java script<br><br>
  Database: MySQL<br><br>

The web-application is created on the Django framework.



<br><br>


<h3>How does it work?</h3>
1. The user uploads a text file (.txt) and a video file (.mp4) and it is saved in the database.<br><br>
2. The transcript-to-audio-converter python file accesses the text file from the database and synthesizes an audio file which is stored in the database.<br><br>
3. ffmpeg is used to access the audio and video from the database and merge it into a Spoken Tutorial. It is saved in the database and provided to the user.

<br><br>


<h3>Project Structure</h3>
The project is divided into two Django apps - 'audio' and 'video'.

*It is a really simple structure as of now, the transcript-to-audio-converter file is in the 'audio' folder and the audio-and-video-merger file is in the 'video' folder.*


<h3>Things I am working on...</h3>
I am currently working on the frontend and UI/UX of this web-application. The backend is pretty neat.

<br>
<h3> Frontend Mockups </h3>
![  (1)](https://user-images.githubusercontent.com/79274516/208641604-fb5a9881-e4d9-41f2-947a-004b79a8d675.jpg)
<br>
![  (2)](https://user-images.githubusercontent.com/79274516/208641617-a16ad725-f7af-4e17-86bf-1203ff9ab60b.jpg)
<br>
![  (3)](https://user-images.githubusercontent.com/79274516/208641634-ca2f0494-779d-4169-9187-3dbf68de8f1f.jpg)
<br>
![  (4)](https://user-images.githubusercontent.com/79274516/208641646-df305ffa-745e-4aec-b31e-33ce9eb8168f.jpg)
<br>
