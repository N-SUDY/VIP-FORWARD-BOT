class script(object):
    ABOUT_TXT = """
    ✯ 𝙰𝙳𝙼𝙸𝙽 : <a href=https://t.me/Snowball_official>𝙎𝙉𝙊𝙒𝘽𝘼𝙇𝙇</a>
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈 : 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴 : 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴 : 𝙼𝙾𝙽𝙶𝙾-𝙳𝙱
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁 """

    START_TXT = """
    Hi {},
This is a simple bot to forward all messages from one channel to other

⚠️Warning
Your account may get banned if you forward more files(from private channels). Use at Own Risk!!
"""

    HELP_TXT = """
Available commands:-

➪ /index - To index a channel
➪ /forward - To start forwarding
➪ /total - Count total messages in DB
➪ /status - Check Current status
➪ /help - Help data
➪ /stop - To stop all running processes.

Use /index to index messages from a channel to database.

After indexing you can start forwarding by using /forward.

<b>Note:</b>
You will require the following data to index a channel:-

<b>Channel Invite Link</b>:- If channel is a Private channel User needs to join channel to acces the messages. Please note that do not leave channel until forwarding completes.

<b>Channel ID</b>:- If channel is a private channel you may need to enter Channel ID. Get it from @MissRose_bot.

<b>SKIP_NO</b>:-From where you want to start Forwarding files.Give 0 if from starting

<b>Caption</b>:- Custom Caption for forwarded files. Use 0 to use default captions.

After fowarding completes use the /cleardb command to clean your database.
"""