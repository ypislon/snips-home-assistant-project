from hermes_python.hermes import Hermes

MQTT_ADDR = "localhost:1883"        # Specify host and port for the MQTT broker

def subscribe_weather_forecast_callback(hermes, intent_message):    # Defining callback functions to handle an intent that asks for the weather.
    print("Parsed intent : {}".format(intent_message.intent.intent_name))
    print("Slots: {}".format(intent_message.slots))


def subscribe_play_song_callback(hermes, intent_message):
    print("Parsed intent: {}".format(intent_message.intent.intent_name))
    for slot in intent_message.slots.song_name:
        print("For slot: {}, the confidence is: {}".format(slot.slot_name, slot.confidence_score))

with Hermes(MQTT_ADDR) as h: # Initialization of a connection to the MQTT broker
    h.subscribe_intent("searchWeatherForecast", subscribe_weather_forecast_callback).subscribe_intent("playSong", subscribe_play_song_callback).start()
