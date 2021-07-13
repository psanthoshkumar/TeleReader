## Read Telegram Messages

#### The purpose of this repo is to read telegram messages using python and process as you desire for next steps.

#### sample use case benefit from this project are:

1. Notify your customers with emails and/or Text Messages.
2. if your fan/customer base is more in other platforms(whatsApp, Slack and Discord etc..), it's possible to notify other platform users by using this middleware.


#### Steps and pre-reqs to fulfill:
1. install python3
2. install telethon package

`pip3 install telethon`

3. Create `API_ID` and `API_HASH` using https://my.telegram.org/apps
   
4. download this source code
5. update properties.conf file
6. start the application

#### Note: Do not share API_ID and API_HASH to anyone.
#### Working Example:

After Starting the application, we can wait until having the message in the listening group. For this instance, I joining on dummy channel as an user (which has API access) called testing-group2. 
Once Channel admin posts message in that channel, I am able to read message from CLI without opening Telegram app.

###### Here is the Screenshot of posted message in channel:
![screenshot of group](./docs/screenshot_Msg1.png)

###### Example CLI ouptut:

    (venv) varma@varmas-Mac-mini listenTelegramMsgs % python teleReader.py
    ['xxxxx', 'xxxxxx']
    TeleReader is listening to: ['https://t.me/xxxxxx', 'https://t.me/xxxxxx']
    Please enter your phone (or bot token): +xxxxxxxx
    Please enter the code you received: xxxxx
    Signed in successfully as xxxxxx
    from: testing-group2 => msg - Hello this is testing Message 1 <-- Validate Test Message from TeleRead CLI


## Next steps???

As we see messages in Python CLI, it's easy to hookup with other external services like Slack Webhooks, Email servers and/or Paging systems to notify customer base.


