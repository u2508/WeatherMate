# WeatherMate - Real-Time Weather Web Application

**WeatherMate** is a responsive, Flask-based web application that lets users search and view real-time weather information for any city. With data sourced from the OpenWeatherMap API, WeatherMate offers users a visually appealing and interactive experience to keep track of weather conditions worldwide.

---

## Table of Contents

1. [Features](#features)
2. [Project Structure](#project-structure)
3. [Setup and Installation](#setup-and-installation)
4. [Requirements](#requirements)
5. [Running the Application](#running-the-application)
6. [Minimum System Specifications](#minimum-system-specifications)
7. [Troubleshooting](#troubleshooting)
8. [License](#license)

---

## Features

- **Real-Time Weather Search**: Get up-to-date weather information for any city, including temperature, weather description, and icons.
- **City-Based Search**: Users enter the city name to retrieve weather details.
- **Responsive Design**: Built with Tailwind CSS for an adaptive layout on both mobile and desktop screens.
- **Secure Login System**: A basic login and registration feature for user authentication, paving the way for future enhancements.
- **Error Handling**: Notifies users when a city is not found or if an API error occurs.

---

## Project Structure

```plaintext
WeatherMate/
├── instance/                 # Instance configuration (if needed)
├── static/                   # Static assets (CSS, JS, images)
│   ├── css/
│   └── js/
├── templates/                # HTML templates for Flask
│   ├── login.html            # Login page
│   ├── registration.html     # Registration page
│   └── weather.html          # Weather search and display page
├── app.py                    # Main Flask application file
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## Setup and Installation

### 1. Clone the Repository

Start by cloning the project repository to your local machine:

```bash
git clone https://github.com/u2508/WeatherMate.git
cd WeatherMate
```

### 2. Set Up a Virtual Environment (Optional but Recommended)

To keep dependencies isolated, create a virtual environment:

#### For Windows
```bash
python -m venv .venv
.venv\Scripts\activate
```

#### For macOS/Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

With the virtual environment activated, install the required packages:

```bash
pip install -r requirements.txt
```

### 4. Configure OpenWeatherMap API Key

To enable weather data retrieval, sign up on [OpenWeatherMap](https://openweathermap.org/) to obtain an API key. Replace `'YOUR_API_KEY'` in `app.py` with your actual API key:

```python
api_key = 'YOUR_API_KEY'
```

---

## Running the Application

1. **Start the Flask Server**

   Run the application by executing:

   ```bash
   python app.py
   ```

2. **Access the Application**

   Open your web browser and go to `http://127.0.0.1:8000`. You’ll start on the **login page**; after logging in, navigate to the weather search page to enter a city name and view weather details.

---

## Minimum System Specifications

- **Operating System**: Windows, macOS, or Linux
- **Processor**: 1 GHz or faster
- **RAM**: 512 MB minimum (1 GB recommended)
- **Python Version**: 3.7 or higher
- **Storage**: At least 100 MB of free space

For best performance, ensure Python 3.7+ is installed.

---

## Troubleshooting

- **Unable to Start Flask Server**: Ensure that the virtual environment is activated and all dependencies are installed.
- **API Key Issues**: Verify that your API key is valid and properly configured in `app.py`.
- **Dependency Errors**: Run `pip install --upgrade -r requirements.txt` to update dependencies.

---

## License

This project is licensed under the MIT License. For details, see the `LICENSE` file.

---

This documentation provides a streamlined guide to setting up, running, and troubleshooting WeatherMate.