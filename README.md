# Smart Surveillance System using OpenCV

A real-time face detection based surveillance system built using Python and OpenCV.

This system uses your webcam to detect faces, plays a sound alert when someone is detected, and saves an image of the person with a timestamp.

## Features

- Real-time face detection
- Sound alert on face detection using `sounddevice`
- Captures and stores intruder images with timestamps
- Automatically saves images in `intruders/` folder

## Technologies Used

- Python
- OpenCV
- NumPy
- sounddevice
- Haar Cascade Classifiers

## Project Structure

## Project Structure

smart-surveillance/

├── intruders/           → Folder to store detected face snapshots  
├── main.py              → Main Python script  
├── requirements.txt     → Project dependencies  
└── README.md            → Project documentation

## Installation & Setup

Follow the steps below to run the Smart Surveillance System on your machine:

1. Clone the repository from GitHub:

   git clone https://github.com/SaurabhEffect/smart-surveillance.git
   cd smart-surveillance

2. Create a virtual environment:

   python -m venv venv

3. Activate the virtual environment:

   - On Windows:
     venv\Scripts\activate

   - On Linux/Mac:
     source venv/bin/activate

4. Install the required packages:

   pip install -r requirements.txt

5. Run the application:

   python main.py

   - A webcam window will open.
   - The app detects faces in real-time.
   - On detection, a beep will play and the face will be saved as an image in the "intruders" folder.
   - Press 'Q' to quit the program.

## Features

- Real-time face detection using OpenCV
- Audible alert on face detection
- Snapshot saving with date and time
- Easy to use and modify

---

## Future Enhancements

- Add email or WhatsApp alert system
- Face recognition (not just detection)
- Cloud sync for saved images
- Motion detection and activity logs

---

## Author
Made with 💙 by Saurabh  
Open to contributions and suggestions
