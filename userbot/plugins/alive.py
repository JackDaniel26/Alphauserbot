import asyncio
from telethon import events
from userbot.utils import admin_cmd, sudo_cmd
from userbot import ALIVE_NAME, alphaversion
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Hell User"

kraken = bot.uid

PM_IMG = "https://i.ibb.co/Swvg82s/IMG-20201029-205430-067.jpg"
pm_caption = "__**🔥🔥Aliveɮօt ɨs օռʟɨռɛ🔥🔥**__\n\n"

pm_caption += f"               __↼🄼🄰🅂🅃🄴🅁⇀__\n**『[{DEFAULTUSER}](tg://user?id={alphacracker01})』**\n\n"

pm_caption += "🛡️TELETHON🛡️ : 1.15.0 \n"

pm_caption += f"😈Hêllẞø†😈       : `{Alphaversion}`\n"

pm_caption += "⚠️CHANNEL⚠️   : [ᴊᴏɪɴ](https://t.me/httpstmejoinchatKRMA6RuflY)\n"

pm_caption += "🔱GROUP🔱.       : [ᴊᴏɪɴ](https://t.me/httpstmejoinchatKRMA6RuflY)\n"

pm_caption += "🔥CREATOR🔥    : [Nub Here](https://t.me/alphacracker01)\n\n"

pm_caption += "         [✨REPO✨](https://github.com/JackDaniel26/Alphauserbot) 🔹 [📜License📜](https://github.com/JackDaniel26/Alphauserbot/blob/master/LICENSE)"
#@command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
