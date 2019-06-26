#!/usr/bin/env python2

from hermes_python.hermes import Hermes, MqttOptions
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import secrets

# Specify host and port for the MQTT broker
MQTT_ADDR = "localhost:1883"

# Bootstrap spotipy to connect to spotify api
client_credentials_manager = SpotifyClientCredentials(client_id=secrets.spotify_client_id, client_secret=secrets.spotify_client_secret)
cache_token = client_credentials_manager.get_access_token()
sp = spotipy.Spotify(cache_token)

result = sp.search(q="life", limit=20)

# Define callback functions for every intent
def subscribe_play_song_callback(hermes, intent_message):
    print("Parsed intent: {}".format(intent_message.intent.intent_name))
    print("slot value: {}".format(intent_message.slots.song_name.first().value))
    session_id = intent_message.session_id
    user_input = intent_message.input
    slot_value = intent_message.slots.song_name.first().value

    for slot in intent_message.slots.song_name:
        print("For slot: {}, the confidence is: {}".format(slot.slot_name, slot.confidence_score))

    result = sp.search(intent_message.slots.song_name.first().value)
    print(result)

    return hermes.publish_continue_session(session_id, user_input, [])

# Start mosquitto server and subscribe to intents
# with Hermes(MQTT_ADDR) as h: # Initialization of a connection to the MQTT broker
#     h.subscribe_intent("playSong", subscribe_play_song_callback) \
#       .subscribe_intent("", subscribe_play_song_callback) \
#       .subscribe_intent("", subscribe_play_song_callback) \
#       .subscribe_intent("", subscribe_play_song_callback) \
#       .start()
