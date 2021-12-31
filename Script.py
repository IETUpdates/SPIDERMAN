class script(object):
    START_TXT = """<b>Hello {}</b>

<i>Iam A Simple Auto Filter + Movie Search + Manual Filter Bot. I Can Provide Movies In Telegram Groups. I Can Also Add Filters In Telegram Groups.  Just Add Me To Your Group As Admin And Enjoy</i>

<b>Made With ❤ BY @IET_Updates</b>"""
    HELP_TXT = """hey {}
I have the following features. Tap the button in which you want help."""
    ABOUT_TXT = """<b>🤖 ʙᴏᴛ ɴᴀᴍᴇ: <a href= https://t.me/MM_Spiderman_BoT>🕷️ sᴘɪᴅᴇʀ-ᴍᴀɴ</a></b>
 
<b>📝 ʟᴀɴɢᴜᴀɢᴇ :</b><b> <a href= https://www.python.org/>ᴘʏᴛʜᴏɴ³</a></b> 

<b>📚 ꜰʀᴀᴍᴇᴡᴏʀᴋ :</b><b> <a href= https://docs.pyrogram.org/>ᴘʏʀᴏɢʀᴀᴍ</a></b>

<b>📡 ʜᴏsᴛᴇᴅ ᴏɴ :</b><b> <a href= https://www.heroku.com/>ʜᴇʀᴏᴋᴜ</a></b>

<b>👨‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ :</b><b> <a href= https://t.me/Iqbal_KA>Iǫʙᴀʟ ᴋ ᴀ</a></b>

<b>💡 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ :</b><b> <a href= https://t.me/IET_Owner/724>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a></b>

<b>👥 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ :</b><b> <a href= https://t.me/IET_SUPPORT>ɪᴇᴛ sᴜᴘᴘᴏʀᴛ</a></b>

<b>📢 ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ :</b><b> <a href= https://t.me/IET_Updates>ɪᴇᴛ ᴜᴘᴅᴀᴛᴇs</a></b>"""
    SOURCE_TXT = """<b>SPIDER-MAN:</b>
- Spiderman is Not a open source project made by <a href=https://t.me/iet_owner>IQBAL K A</a>. 
- Source - <a href= https://t.me/IET_Owner/724>Click here </a>
<b><u>📽️ How To Create This BoT.?</u></b>
<a href= https://youtu.be/1ltbuCY_V6s>എങ്ങനെ ഉണ്ടാക്കാം എന്ന് അറിയാൻ ഇവിടെ ക്ലിക്ക് ചെയ്താൽ മതി. </a>

<b>Support channel:</b>
- <a href=https://t.me/IET_support>IET SUPPORT</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Spiderman will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Spiderman should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Spiderman Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Spiderman supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/iet_updatess)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message from Spiderman)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, 🔞porn and ☣️fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
Here are the extra features of Spiderman

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """<b>📁 ᴛᴏᴛᴀʟ ꜰɪʟᴇs: {}</b>

<b>👤 ᴛᴏᴛᴀʟ ᴜsᴇʀs: {} 🕸️</b>

<b>👥 ᴛᴏᴛᴀʟ ᴄʜᴀᴛs: {} 🕷️</b>

<b>⚙️ ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ: {}</b>

<b>🆓 ꜰʀᴇᴇ sᴛᴏʀᴀɢᴇ: {}</b>"""
    LOG_TEXT_G = """#NewGroup
🕸️ Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
🕷️ Name - {}
"""
