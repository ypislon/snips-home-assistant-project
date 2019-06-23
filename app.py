from hermes_python.hermes import Hermes

MQTT_ADDR = "localhost:1883"        # Specify host and port for the MQTT broker

def subscribe_weather_forecast_callback(hermes, intent_message):    # Defining callback functions to handle an intent that asks for the weather.
    print("Parsed intent : {}".format(intent_message.intent.intent_name))

with Hermes(MQTT_ADDR) as h: # Initialization of a connection to the MQTT broker
    h.subscribe_intent("searchWeatherForecast", subscribe_weather_forecast_callback).start()
