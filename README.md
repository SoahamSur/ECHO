

---

# Echo : Your Own Virtual Assistant

## About
Echo is a virtual assistant designed to perform a variety of tasks such as fetching weather information, playing music, telling jokes, providing news updates, and interacting with users through natural language processing. It uses Google's Generative AI to generate human-like responses and integrates with various APIs for enhanced functionality.

## Tech Stack
- **Python**: The primary programming language used for scripting and automation.
- **Google Generative AI (Gemini-1.5-flash)**: The model used to generate human-like responses.
- **Various APIs**: For weather, news, YouTube search, and more.
- **Pyttsx3**: For text-to-speech conversion.
- **SpeechRecognition**: For recognizing voice commands.
- **Requests**: For making HTTP requests to APIs.
- **Webbrowser**: For opening web pages.
- **Pyjokes**: For generating jokes.
- **Datetime**: For fetching the current time.

## Libraries Used
- **Pyttsx3**: To convert text to speech.
  - Installation: `pip install pyttsx3`
- **SpeechRecognition**: For speech-to-text conversion.
  - Installation: `pip install SpeechRecognition`
- **Requests**: For making HTTP requests to APIs.
  - Installation: `pip install requests`
- **Google Generative AI**: For generating human-like responses.
  - Installation: Follow Google's documentation to install and configure the generative AI library.
- **Pyjokes**: For generating jokes.
  - Installation: `pip install pyjokes`
- **Google API Client**: For accessing Google APIs like YouTube.
  - Installation: `pip install google-api-python-client`

## Unique Selling Points (USPs)
- **Multi-functional**: Capable of performing a wide range of tasks, from fetching weather information to telling jokes and playing music.
- **Human-like Responses**: Uses Google's Generative AI to generate responses that mimic natural human conversations.
- **Voice Interaction**: Recognizes voice commands and responds via text-to-speech.
- **Real-time Information**: Provides real-time updates on weather, news, and more using various APIs.
- **Customizable and Extensible**: Easily extendable to include more features and functionalities.

## Getting Started
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/SoahamSur/ECHO.git
   cd ECHO
   ```
2. **Install Dependencies**:
   ```bash
   pip install pyttsx3 SpeechRecognition requests pyjokes google-api-python-client
   ```
3. **Configure API Keys**:
   - Sign up for necessary APIs (Weather API, News API, YouTube API, Google Generative AI) and obtain API keys.
   - Replace the placeholder API keys in the script with your actual API keys.
4. **Run the Script**:
   ```bash
   python echo_assistant.py
   ```

## Usage
1. Run the script to start the Echo assistant.
2. Say "Echo" to activate the assistant.
3. Give commands such as "What's the weather?", "Tell me a joke", "Play [song name]", "Search YouTube for [query]" or "Any general tasks".
4. The assistant will recognize your voice command, process it, and respond accordingly.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.


---
