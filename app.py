import  speech_recognition as sr
import pyttsx3
import pywhatkit 
import pyjokes as jk
import datetime as dt
import pyowm
from playsound import playsound
import pyautogui

owm = pyowm.OWM("9bbcf4d9d6a6ef44908b6a609e426283")
weather_mgr = owm.weather_manager()
place = 'kurnool, IN'

listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id) 

def talk(command):
    engine.say(command)
    engine.runAndWait()

def playyt(song):
    print("Playing......."+song)
    talk("playing...."+song)
    pywhatkit.playonyt(song)
def sing(song):
    talk("sure enjoy this song")
    playsound(song)
def joke(command):
    tokens = list(command.split(" "))
    joke = jk.get_joke(language="en" ,category=tokens[-1])
    print(joke)
    talk(joke)
def time():
    time = dt.datetime.now().strftime("%I:%M:%S %p")
    print("current time is:",time)
    talk("current time is "+time)
def date():
    date = dt.date.today()
    print("Today date is:",date.strftime("%B-%d-%y"))
    talk("Today date is "+str(date))
def sendwhtmsg():
    # pywhatkit.sendwhatmsg("+919912706193", "Hi",15,31)
    print("sending....")
    # pywhatkit.sendwhatmsg_to_group_instantly("Team Part-time", "Hey All!")
    phone_number = "+919912706193"
    # if 'message' in command:
    #     message = command.replace('message','')
    # else:
    #     message = "Hlo"
    message = "Hlo"
    pywhatkit.sendwhatmsg_instantly(phone_number, message) 
    talk("sending....")
    
def get_weather():
    observation = weather_mgr.weather_at_place(place)
    temperature = observation.weather.temperature("celsius")["temp"]
    humidity = observation.weather.humidity
    wind = observation.weather.wind()
    talk("current weather in location is")
    print(f'Temperature: {temperature}°C')
    print(f'Humidity: {humidity}%')
    print(f'Wind Speed: {wind["speed"]} m/s')
    talk(f'Temperature: {temperature}°C')
    talk(f'Humidity: {humidity}%')
    talk(f'Wind Speed: {wind["speed"]} m/s')
    
def talk_command():
    try:
        with sr.Microphone() as source:
            print("Listening....")
            talk("I am ready to listening bujji")
            voice = listener.listen(source)
            command = listener.recognize_google(voice).lower()
            # talk(command)
            if 'what is your name' in command:
                talk("I am buji how can i help you")
            if "bujji" in command:
                command = command.replace('bujji','')
                print(command)
                # talk(command)
            else:
                print("I am bujji")
                # talk("I am buji")
                return ""        
    except:
        command = "sorry your voice is not clear"
    return command

def run_Alexa(): 
    command = talk_command()
    if 'play' in command:
        song = command.replace('play','')
        playyt(song)
    elif 'sing' in command:
        sing("D:\Gundu\DeepLearning_Projects\Alexa\Assets\[iSongs.info] 07 - Komuram Bheemudo.mp3")
        
    elif 'increase volume' in command:
        pyautogui.press('volumup')
    elif 'decrease volume' in command:
        pyautogui.press('volumdown')
    elif 'joke'  in command or 'jokes' in command:
        joke(command)
    elif 'time' in command:
        time()
    elif 'date' in command:
        date()
    elif 'send' in command:
        sendwhtmsg()
    elif 'weather' in command:
        get_weather()
    else:
        print(command)
        talk(command)
    
talk("I am buji how can i help you")     
while True:  
    run_Alexa()
    


# talk("sure enjoy the song")
# playsound("[iSongs.info] 05 - Naatu Naatu.mp3")

# print("Increse..")
# pyautogui.press('volumup')
# i=0
# while(i<10):
#     currentMouseX, currentMouseY = pyautogui.position()
#     print(currentMouseX,currentMouseY)
#     i+=1
# pyautogui.moveTo(700, 400)
# pyautogui.write('Hello world!', interval=0.5)
# with pyautogui.hold('shift'):  # Press the Shift key down and hold it.
#         pyautogui.press(['left', 'left', 'left', 'left'])  # Press the left arrow key 4 times.
# pyautogui.press('delete')

# pyautogui.hotkey('ctrl', 'c') # Press the Ctrl-C hotkey combination.


# pyautogui.alert('This is the message to display.') 




# import argparse
# import datetime
# import json
# import random

# import requests

# import form


# def fill_random_value(type_id, entry_id, options):
#     ''' Fill random value for a form entry 
#         Customize your own fill_algorithm here
#         Note: please follow this func signature to use as fill_algorithm in form.get_form_submit_request '''
#     # Customize for specific entry_id
#     if entry_id == 'emailAddress':
#         return 'your_email@gmail.com'
#     # Random value for each type
#     if type_id in [0, 1]: # Short answer and Paragraph
#         return ''
#     if type_id == 2: # Multiple choice
#         return random.choice(options)
#     if type_id == 3: # Dropdown
#         return random.choice(options)
#     if type_id == 4: # Checkboxes
#         return random.sample(options, k=random.randint(1, len(options)))
#     if type_id == 5: # Linear scale
#         return random.choice(options)
#     if type_id == 7: # Grid choice
#         return random.choice(options)
#     if type_id == 9: # Date
#         return datetime.date.today().strftime('%Y-%m-%d')
#     if type_id == 10: # Time
#         return datetime.datetime.now().strftime('%H:%M')
#     return ''

# def generate_request_body(url: str, only_required = False):
#     ''' Generate random request body data '''
#     data = form.get_form_submit_request(
#         url,
#         only_required = only_required,
#         fill_algorithm = fill_random_value,
#         output = "return",
#         with_comment = False
#     )
#     data = json.loads(data)
#     # you can also override some values here
#     return data

# def submit(url: str, data: any):
#     ''' Submit form to url with data '''
#     url = form.get_form_response_url(url)
#     print("Submitting to", url)
#     print("Data:", data, flush = True)
   
#     res = requests.post(url, data=data, timeout=5)
#     if res.status_code != 200:
#         print("Error! Can't submit form", res.status_code)

# def main(url, only_required = False):
#     try:
#         payload = generate_request_body(url, only_required = only_required)
#         submit(url, payload)
#         print("Done!!!")
#     except Exception as e:
#         print("Error!", e)

# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description='Submit google form with custom data')
#     parser.add_argument('url', help='Google Form URL')
#     parser.add_argument('-r', '--required', action='store_true', help='Only include required fields')
#     args = parser.parse_args()
#     main(args.url, args.required)
