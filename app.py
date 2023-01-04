import speech_recognition as sr
import pyttsx3
import openai

r = sr.Recognizer()
openai.api_key = "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"

def SpeakText(command):
	
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()

while(1):

    try:

        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)

            audio2 = r.listen(source2)

            text = r.recognize_google(audio2)

            text = text.lower()

            response = openai.Completion.create(model="text-davinci-003",prompt=text,temperature=0.6,max_tokens=150,top_p=1,frequency_penalty=1,presence_penalty=1)

            jsonData = response["choices"]

            for x in jsonData:
                values = x.values()
            print(list(values)[0])
            SpeakText(list(values)[0])

    except sr.RequestError as e:
        # print("Could not request results; {0}".format(e))
        continue

    except sr.UnknownValueError:
        # print("Unknown Value error")\
        continue


