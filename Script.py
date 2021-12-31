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

- Fɪʟᴛᴇʀ ɪs ᴛʜᴇ ғᴇᴀᴛᴜʀᴇ ᴡᴇʀᴇ ᴜsᴇʀs ᴄᴀɴ sᴇᴛ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ʀᴇᴘʟɪᴇs ғᴏʀ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴋᴇʏᴡᴏʀᴅ ᴀɴᴅ Sᴘɪᴅᴇʀᴍᴀɴ ᴡɪʟʟ ʀᴇsᴘᴏɴᴅ ᴡʜᴇɴᴇᴠᴇʀ ᴀ ᴋᴇʏᴡᴏʀᴅ ɪs ғᴏᴜɴᴅ ᴛʜᴇ ᴍᴇssᴀɢᴇ.

<b>NOTE:</b>
1. Sᴘɪᴅᴇʀᴍᴀɴ sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
2. ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴀᴅᴅ ғɪʟᴛᴇʀs ɪɴ ᴀ ᴄʜᴀᴛ.
3. ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴs ʜᴀᴠᴇ ᴀ ʟɪᴍɪᴛ ᴏғ 64 ᴄʜᴀʀᴀᴄᴛᴇʀs.


<b>Commands and Usage:</b>
• /filter - <code>ᴀᴅᴅ ᴀ ғɪʟᴛᴇʀ ɪɴ ᴄʜᴀᴛ</code>
• /filters - <code>ʟɪsᴛ ᴀʟʟ ᴛʜᴇ ғɪʟᴛᴇʀs ᴏғ ᴀ ᴄʜᴀᴛ</code>
• /del - <code>ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ғɪʟᴛᴇʀ ɪɴ ᴄʜᴀᴛ</code>
• /delall - <code>ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴡʜᴏʟᴇ ғɪʟᴛᴇʀs ɪɴ ᴀ ᴄʜᴀᴛ (ᴄʜᴀᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Sᴘɪᴅᴇʀᴍᴀɴ Sᴜᴘᴘᴏʀᴛs ʙᴏᴛʜ ᴜʀʟ ᴀɴᴅ ᴀʟᴇʀᴛ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴs.

<b>NOTE:</b>
1. Tᴇʟᴇɢʀᴀᴍ ᴡɪʟʟ ɴᴏᴛ ᴀʟʟᴏᴡs ʏᴏᴜ ᴛᴏ sᴇɴᴅ ʙᴜᴛᴛᴏɴs ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴄᴏɴᴛᴇɴᴛ, sᴏ ᴄᴏɴᴛᴇɴᴛ ɪs ᴍᴀɴᴅᴀᴛᴏʀʏ.
2. Sᴘɪᴅᴇʀᴍᴀɴ sᴜᴘᴘᴏʀᴛs ʙᴜᴛᴛᴏɴs ᴡɪᴛʜ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ.
3. Bᴜᴛᴛᴏɴs sʜᴏᴜʟᴅ ʙᴇ ᴘʀᴏᴘᴇʀʟʏ ᴘᴀʀsᴇᴅ ᴀs ᴍᴀʀᴋᴅᴏᴡɴ ғᴏʀᴍᴀᴛ

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/iet_updatess)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message from Spiderman)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Mᴀᴋᴇ ᴍᴇ ᴛʜᴇ ᴀᴅᴍɪɴ ᴏғ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪғ ɪᴛ's ᴘʀɪᴠᴀᴛᴇ.
2. ᴍᴀᴋᴇ sᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴅᴏᴇs ɴᴏᴛ ᴄᴏɴᴛᴀɪɴs ᴄᴀᴍʀɪᴘs, 🔞ᴘᴏʀɴ ᴀɴᴅ ☣️ғᴀᴋᴇ ғɪʟᴇs.
3. Fᴏʀᴡᴀʀᴅ ᴛʜᴇ ʟᴀsᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴇ ᴡɪᴛʜ ǫᴜᴏᴛᴇs.
 I'ʟʟ ᴀᴅᴅ ᴀʟʟ ᴛʜᴇ ғɪʟᴇs ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴍʏ ᴅʙ."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Usᴇᴅ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʙᴏᴛ ᴛᴏ PM ғᴏʀ ᴍᴀɴᴀɢɪɴɢ ғɪʟᴛᴇʀs 
- ɪᴛ ʜᴇʟᴘs ᴛᴏ ᴀᴠᴏɪᴅ sᴘᴀᴍᴍɪɴɢ ɪɴ ɢʀᴏᴜᴘs.

<b>NOTE:</b>
1. Oɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴀᴅᴅ ᴀ ᴄᴏɴɴᴇᴄᴛɪᴏɴ.
2. Sᴇɴᴅ <code>/ᴄᴏɴɴᴇᴄᴛ</code> ғᴏʀ ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴍᴇ ᴛᴏ ᴜʀ PM

<b>Commands and Usage:</b>
• /connect  - <code>ᴄᴏɴɴᴇᴄᴛ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ ᴛᴏ ʏᴏᴜʀ PM</code>
• /disconnect  - <code>ᴅɪsᴄᴏɴɴᴇᴄᴛ ғʀᴏᴍ ᴀ ᴄʜᴀᴛ</code>
• /connections - <code>ʟɪsᴛ ᴀʟʟ ʏᴏᴜʀ ᴄᴏɴɴᴇᴄᴛɪᴏɴs</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
Hᴇʀᴇ ᴀʀᴇ ᴛʜᴇ ᴇxᴛʀᴀ ғᴇᴀᴛᴜʀᴇs ᴏғ Sᴘɪᴅᴇʀᴍᴀɴ

<b>Commands and Usage:</b>
• /id - <code>ɢᴇᴛ ɪᴅ ᴏғ ᴀ sᴘᴇᴄɪғᴇᴅ ᴜsᴇʀ.</code>
• /info  - <code>ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜsᴇʀ.</code>
• /imdb  - <code>ɢᴇᴛ ᴛʜᴇ ғɪʟᴍ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ғʀᴏᴍ IMDB sᴏᴜʀᴄᴇ.</code>
• /search  - <code>ɢᴇᴛ ᴛʜᴇ ғɪʟᴍ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ғʀᴏᴍ ᴠᴀʀɪᴏᴜs sᴏᴜʀᴄᴇs.</code>"""
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
