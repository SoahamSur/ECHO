import requests
import pyttsx3
import json
import speech_recognition as sr
import webbrowser
import musicLibrary
import google.generativeai as genai
import pyjokes
import datetime
from googleapiclient.discovery import build

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 140)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


newsapi="766adcc894a04cd8ae44fce2de56e762"
weatherApi = "4e6a3856412b4922bb5141121240207"
youtube_api_key = "AIzaSyAvB_quNhnHvJbZSvpWYOYhfjfQvca3aFw"


def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_weather_info(location):
    try:
        url = f"http://api.weatherapi.com/v1/current.json?key={weatherApi}&q={location}"

        # Fetch weather data
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        weatherdict = response.json()

        giveInfo = [
            f"Current temperature at {location} is {weatherdict['current']['temp_c']} degree Celsius",
            f"Current weather condition is {weatherdict['current']['condition']['text']}",
            f"Feels like temperature is {weatherdict['current']['feelslike_c']} degree Celsius",
            f"Humidity is {weatherdict['current']['humidity']}%",
            f"Precipitation is {weatherdict['current']['precip_mm']} mm",
            f"Cloud cover is {weatherdict['current']['cloud']}%"
        ]

        for info in giveInfo:
            speak(info)
        
    except requests.exceptions.RequestException as e:
        speak("Failed to fetch weather data. Please check your internet connection and try again.")
    except KeyError as e:
        speak("Unexpected data format received from the weather service.")
    except Exception as e:
        speak(f"An error occurred: {str(e)}")
    finally:
        speak("Thank you for using our service")

def aiProcess(command):
    gemini_key = "AIzaSyDl-Ksq6sPBdzMu-60qHDfdJJtX_9cd63c"
    genai.configure(api_key=gemini_key)
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    prompt = f'You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud. Give Short Responses but also vary the length according to users queries.Do not use emojis,special characters like *.Here is your command: {command}'
    
    response = model.generate_content(prompt)
    response_text = response.candidates[0].content.parts[0].text

    return response_text


def search_youtube(query):
    youtube = build('youtube', 'v3', developerKey=youtube_api_key)
    request = youtube.search().list(
        part="snippet",
        q=query,
        type="video",
        maxResults=1
    )
    response = request.execute()
    video_id = response['items'][0]['id']['videoId']
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    return video_url

def processComand(c):
    if 'open google' in c.lower():
        webbrowser.open("https://google.com")
    
    elif 'open youtube' in c.lower():
        webbrowser.open("https://youtube.com")
    
    elif 'open facebook' in c.lower():
        webbrowser.open("https://facebook.com")
    
    elif 'open linkedin' in c.lower():
        webbrowser.open("https://linkedin.com")
        
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        if link:
            webbrowser.open(link)
        else:
            ytlink=search_youtube(link)
            webbrowser.open(ytlink)
      
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
        if articles:
             speak(f"Here are the top important news articles:")
             for i, article in enumerate(articles[:2]):
            
                    speak(f"News {i + 1}: {article['title']}")
        else:
            speak("I couldn't find any news articles.")
        
    
    elif "joke" in c.lower():
        joke = pyjokes.get_joke()
        speak(joke)  
        
    elif 'time' in c.lower():
        hour = datetime.datetime.now().strftime("%H")  
        min = datetime.datetime.now().strftime('%M')
        speak(f'The time is {hour}:{min}')
    
    elif 'weather' in c.lower():
            speak("Please say your location: ")
            with sr.Microphone() as source:
                locn_audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
            try:
                location = recognizer.recognize_google(locn_audio)
                get_weather_info(location)
            except sr.UnknownValueError:
                speak("Sorry, I did not understand the location. Please try again.")
            except sr.RequestError as e:
                speak(f"Could not request results; {e}")
                
    elif 'search youtube' in c.lower():
        speak("What do you want to search on YouTube?")
        with sr.Microphone() as source:
            search_audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
        try:
            search_query = recognizer.recognize_google(search_audio)
            ytlink = search_youtube(search_query)
            webbrowser.open(ytlink)
        except sr.UnknownValueError:
            speak("Sorry, I did not understand the search query. Please try again.")
        except sr.RequestError as e:
            speak(f"Could not request results; {e}")
    
    elif 'create' in c.lower():
        content=aiProcess(c)
        speak("Here it is:\n")
        print(content)   
              
    elif 'quit' in c.lower():
        speak("See ya")
        exit()
            
    else:
        output = aiProcess(c)
        speak(output)
       
if __name__ == "__main__":
    speak("Welcome to Echo")
    while True:
        recognizer = sr.Recognizer()
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=2)
                
            wakeWord = recognizer.recognize_google(audio)
            if wakeWord.lower() == 'echo':
             speak("Echo activated. How can I assist you?")
            while True:
                    with sr.Microphone() as source:
                        print("Listening....")
                        audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
                        command = recognizer.recognize_google(audio)
                        processComand(command)

        except Exception as e:
            print(f"Error: {e}")
