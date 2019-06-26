if len(intentMessage.slots.volume_higher) > 0:
    volume_level = intentMessage.slots.house_room.first().value # We extract the value from the slot "house_room"
else:
    volume_level = 80

data = {'entity_id': 'all', 'volume_level': volume_level}
# logging.info(volume_level)
hass.services.call('media_player', 'volume_set', data)
