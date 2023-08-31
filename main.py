# Key features:
# Flexible with prompts ☑️
# Google search for queries ☑️
# Showing wikipedia results for queries (todo)
# Opening sites and files ☑️
# Playing music on YouTube ☑️
# Playing music on Spotify using Spotify API (todo)
# Date and Time ☑️
# OpenAI implementation (todo)
# WhatsApp automation (todo)
# Alarm and Timer support (todo)
# Chatbot (todo)
# Google automation (todo)
# GUI (todo)


import speech_recognition as sr
import os
import random
import data
import webbrowser as web
import datetime as dt
import pywhatkit as ytPlayer
from playsound import playsound


# text to speech function


def say(text):
    os.system(f"say {text}")


# function to take and recognize command from user


def getCommand():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        audio = listener.listen(source)
        try:
            command = listener.recognize_google(audio, language="en-in")
            return command.lower()
        except:
            say(random.choice(data.audioErrorMsgs))
            return None


# function to greet user


def greet():
    msg = random.choice(data.welcomeMsgs)
    say(msg)
    print(msg)


if __name__ == "__main__":
    print(f"Say 'Hey {data.AI_name}'")
    query = getCommand()

    # print user command

    if query != "":
        print(f"You said: {query}")

    # greet user if 'hey <AI_name>' in query and remove it to process command

    if f"hey {data.AI_name.lower()}" in query.lower():
        playsound("chime sound effect.mp3")
        if f"hey {data.AI_name.lower()}" == query.lower():
            greet()
            print("Listening...")
            query = (
                getCommand().lower().replace(f"hey {data.AI_name.lower()}", "").strip()
            )
        else:
            query = query.lower().replace(f"hey {data.AI_name.lower()}", "").strip()

        # Following functions only work if 'hey <AI_name>' is heard

        # open websites

        notFound = 0
        for site in data.sites:
            if "open" in query and site[0].lower() in query:
                say(f"Opening {site[0]}...")
                print(f"Opening {site[0]}...")
                web.open(site[1])
            elif "open" in query and site[0].lower() not in query:
                notFound += 1
        if notFound == len(data.sites):
            say(
                "site or file not found. To add additional sites or files, see documentation in README.md and modify data.py"
            )

        # google search

        if "search" in query:
            target = (
                query.replace("search", "")
                .replace("for", "")
                .replace("on google", "")
                .strip()
            )
            say(f"Searching {target}...")
            print(f"Searching {target}...")
            web.open(f"https://www.google.com/search?q={target}")

        # date and time

        for dateQuery in data.dateQueries:
            if dateQuery in query:
                currentDate = dt.date.today()
                say(
                    f"It is {currentDate.day}th{currentDate.strftime('%B')},{currentDate.year}"
                )
                print(f"today's date: {currentDate}")

        for timeQuery in data.timeQueries:
            if timeQuery in query:
                currentTime = dt.datetime.now()
                say(f"It is {currentTime.strftime('%I:%M %p')}")
                print(f"Current time : {currentTime}")

        # youtube/spotify song player

        for songQuery in data.songQueries:
            if songQuery in query:
                songPlatform = "on YouTube" if "spotify" not in query else "on Spotify"
                song = (
                    query.replace(songQuery, "")
                    .replace(songPlatform.lower(), "")
                    .strip()
                )
                say(f"Now playing {song} {songPlatform}...")
                print(f"Now playing {song} {songPlatform}...")
                if songPlatform.lower() == "on spotify":
                    web.open(f"https://open.spotify.com/search/{song}")
                else:
                    ytPlayer.playonyt(song)
                break
