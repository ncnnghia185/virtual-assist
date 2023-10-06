import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather
def action(data):
    user_data = data.lower()
    if "what is your name" in user_data:
        text_to_speech.text_to_speech("My name is JOJO")
        return "My name is JOJO"
    elif "hello" in user_data or "hi" in user_data:
        text_to_speech.text_to_speech("Hello , How can i help you")
        return "Hello , How can i help you"
    elif "good morning" in user_data:
        text_to_speech.text_to_speech("Good morning Bro")
        return "Good morning Bro"
    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        time = str(current_time.hour) + "Hour: " + str(current_time.minute) + "Minute"
        text_to_speech.text_to_speech(time)
        return time
    elif "shut down" in user_data:
        text_to_speech.text_to_speech("Shut Down")
        return "Shut Down"
    elif "play music" in user_data:
        webbrowser.open("https://mp3.zing.vn/")
        text_to_speech.text_to_speech("Zing Mp3 is ready for you")
        return "Zing Mp3 is ready for you"
    elif "open facebook" in user_data:
        webbrowser.open("https://www.facebook.com/")
        text_to_speech.text_to_speech("Facebook opened")
        return "Facebook opened"
    elif "open youtube" in user_data:
        webbrowser.open("https://www.youtube.com/")
        text_to_speech.text_to_speech("Youtube opened")
        return "Youtube opened"
    elif "open google" in user_data:
        webbrowser.open("https://www.google.com/")
        text_to_speech.text_to_speech("Google opened")
        return "Google opened"
    elif "weather" in user_data:
        ans = weather.weather()
        text_to_speech.text_to_speech(ans)
        return ans
    else:
        text_to_speech.text_to_speech("I don't know this information")
        return "I don't know this information"