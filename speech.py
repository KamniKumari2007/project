# trying a simple text to speech thing in python
# i saw pyttsx3 works offline so using that
# pip install pyttsx3

import pyttsx3

print("Text to Speech Tool (my version)")
print("type exit to close\n")

try:
    engine = pyttsx3.init()
except:
    print("engine not loading")
    exit()

# default settings
engine.setProperty("rate", 165)   # speed
engine.setProperty("volume", 0.85)

# i just wanted to check available voices once
v = engine.getProperty("voices")
print("voices:")
for i in range(len(v)):
    print(i, "-", v[i].name)

# by default i just use 0, but can change later
try:
    engine.setProperty("voice", v[0].id)
except:
    pass

print("\nYou can type normal text and it will speak.")
print("If you want to save audio:  save filename.wav text here\n")

while True:
    data = input(">> ")

    if data.strip() == "":
        continue

    if data.lower() == "exit":
        print("closing program..")
        break

    # saving audio option
    if data.startswith("save "):
        # example: save hello.wav this is my text
        parts = data.split(" ", 2)
        if len(parts) < 3:
            print("use like: save abc.wav your text here")
            continue

        file = parts[1]
        msg = parts[2]

        if not file.endswith(".wav"):
            file = file + ".wav"

        try:
            print("saving file...", file)
            engine.save_to_file(msg, file)
            engine.runAndWait()
            print("saved.")
        except Exception as e:
            print("error while saving:", e)

        continue

    # speaking normally
    try:
        engine.say(data)
        engine.runAndWait()
    except Exception as e:
        print("some error happened:", e)