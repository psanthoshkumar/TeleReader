#!/bin/python

import configparser
from telethon import TelegramClient, events, utils
from telethon.tl.types import (PeerChannel)


# import properties file
config = configparser.ConfigParser()
config.read('./properties.conf')

# read api_id and api_hash
api_id = int(config.get('telegram_api', 'api_id'))
api_hash = str(config.get('telegram_api', 'api_hash'))


# Telegram channel name
channels = [x.strip("'") for x in config.get('telegram_api', 'channel_name').split(",")]
# print(channels)
var_channel_urls = []

for i in range(len(channels)):
    channel = channels[i].strip("'")
    channel_full_url = f'https://t.me/{channel}'
    var_channel_urls .append(channel_full_url)

print(f'TeleReader is listening to: {var_channel_urls}')

# if need we can enable filters to filter messages before process them
filters = []

client = TelegramClient('teleread',
                        api_id=api_id,
                        api_hash=api_hash)


# @client.on(events.NewMessage(chats=var_channel_url))
@client.on(events.NewMessage(chats=var_channel_urls))
async def listen_messages(event):

    # raw_event = event.to_dict()
    # event.stringify()
    # print(event.stringify())

    new_message = event.message.message
    channel_id = event.message.peer_id.channel_id

    entity = await client.get_entity(PeerChannel(channel_id))
    my_channel = utils.get_display_name(entity)

    print(f'from: {my_channel} => msg - {new_message}\n')

with client:
    client.run_until_disconnected()
