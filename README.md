# Urine Strip Analyzer

This project is a web-based application that allows users to upload an image of a urine strip and identify the colors on the strip. The application processes the image and returns the results as a JSON object with 10 colors (RGB values) corresponding to different tests on the strip.

## Features

- **Upload Interface**: Users can upload an image of a urine strip through a web interface.
- **Image Analysis**: The application processes the image using OpenCV to extract color information.
- **JSON Output**: The extracted colors are returned as a JSON object with predefined labels.
- **Responsive Design**: The web interface is designed to be user-friendly and works on various devices.

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Frontend**: HTML, CSS, Vanilla JavaScript, jQuery
- **Image Processing**: OpenCV, PIL (Python Imaging Library)
- **API**: RESTful API for image upload and processing

## Prerequisites

- Python 3.6 or higher
- Django 3.1 or higher
- OpenCV
- Pillow
- Django REST Framework

## Installation

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/your-username/urine-strip-analyzer.git
   cd urine-strip-analyzer
