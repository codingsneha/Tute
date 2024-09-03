<img width="24" alt="favicon" src="https://user-images.githubusercontent.com/79274516/208621370-d39bdb26-2df4-4bc3-8d14-7009fe3b3f2f.png">**te** 

# Spoken Tutorial Generator

Welcome to **Tute**, a powerful tool designed to effortlessly create spoken tutorials by combining your text transcripts with video files. Tute streamlines the process, converting your written content into speech and merging it seamlessly with video, making it an ideal solution for educational content creators, tutorial developers, and anyone looking to enhance their video presentations.

## Key Features
- **Automatic Transcript to Audio Conversion**: Tute uses `pyttsx3` to convert your text transcript into clear, spoken audio.
- **Seamless Video and Audio Merging**: The generated audio is automatically synced and merged with your video using `ffmpeg`, ensuring smooth and professional results.
- **User-Friendly Interface**: The application features an intuitive upload and download system, allowing you to easily manage your files.

## How to Run This Project

### Step 1: Set Up Your Environment

#### 1.1 Clone the Repository
Start by cloning the project repository to your local machine:

```bash
git clone https://github.com/codingsneha/Tute
cd Tute
```

#### 1.2 Create a Virtual Environment (Recommended)
Creating a virtual environment is recommended to manage dependencies efficiently:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 2: Install Dependencies

#### 2.1 Install Required Python Packages
Once the virtual environment is activated, install the necessary Python packages, including Django, `pyttsx3`, and `moviepy`:

```bash
pip install django pyttsx3 moviepy
```

### Step 3: Set Up the Django Project

#### 3.1 Apply Migrations
Set up your database by applying the necessary migrations:

```bash
python manage.py migrate
```

### Step 4: Run the Development Server

#### 4.1 Start the Django Development Server
Start the server to begin using the application:

```bash
python manage.py runserver
```

You can now access the project in your web browser at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

### Step 5: Using the Application

#### 5.1 Upload a Transcript and Video
Navigate to the upload page in the application:

- Upload your text transcript file.
- Upload the mute video file you want to process.
- Submit the files for processing.

#### 5.2 Process the Files
Tute will:

1. Convert the text transcript into an audio file using `pyttsx3`.
2. Merge the generated audio with the video file using `ffmpeg`.

#### 5.3 Download the Final Output
After the processing is complete, you will be redirected to a success page. Here, you can view and download the final spoken tutorial.


<img align = "left" width="80" alt="image" src="https://user-images.githubusercontent.com/79274516/208631243-ce1d8e4d-ef81-402a-b5b8-9f6c85c0d784.png">

<h3>Technologies used</h3>

<br>
Tute uses text to speech synthesizer **pyttsx3** to convert text to audio
And the free and open-source-software **ffmpeg** to add the audio to a video file.
<br><br>
  Back-end: Python (pyttsx3 & Django)<br><br>
  Front-end: html, css<br><br>

The web-application is created on the Django framework.



<br><br>


<h3> Frontend Mockups </h3>

![8](https://user-images.githubusercontent.com/79274516/208644218-38c27b4d-726d-487f-9482-f1e4cb875bb3.jpg)
![9](https://user-images.githubusercontent.com/79274516/208644224-8a4df6d2-3766-4491-b3f1-e04f940b06e4.jpg)
![10](https://user-images.githubusercontent.com/79274516/208644229-b5a86142-fe01-4588-92c2-9e49307e66ce.jpg)
![11](https://user-images.githubusercontent.com/79274516/208644232-d71a03f8-d7d5-425f-b024-986d3135fece.jpg)


---

Thank you for using **Tute**! If you encounter any issues or have suggestions for improvement, please feel free to contribute to the project or reach out. Happy creating!
