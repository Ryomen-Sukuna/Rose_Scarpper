from RSc import ubot, vbot, wbot, xbot, ybot, OWNER_ID
from telethon import events
import io
from telethon.tl.functions.messages import ImportChatInviteRequest

@tbot.on(events.NewMessage(pattern="^/start$"))
async def event(event):
 await event.reply("RSc Scrapper is online With 5/15 Clients Active.")

members = []

@tbot.on(events.NewMessage(pattern="^/scrape ?(.*)"))
async def sc(event):
 if not event.sender_id == OWNER_ID:
    return
 if not event.pattern_match.group(1):
    return await event.reply("Please enter the chat username to start scrapping members.")
 chat_username = event.pattern_match.group(1)
 try:
   chat = await tbot.get_entity(chat_username)
   username = chat.username
 except:
   return await event.reply("❌Invalid chat provided.")
 try:
  await ubot(ImportChatInviteRequest(hash=event.chat.username))
  await vbot(ImportChatInviteRequest(hash=event.chat.username))
  await wbot(ImportChatInviteRequest(hash=event.chat.username))
  await xbot(ImportChatInviteRequest(hash=event.chat.username))
  await ybot(ImportChatInviteRequest(hash=event.chat.username))
 except:
  continue
 try:
  await ubot(ImportChatInviteRequest(hash=username))
  await vbot(ImportChatInviteRequest(hash=username))
  await wbot(ImportChatInviteRequest(hash=username))
  await xbot(ImportChatInviteRequest(hash=username))
  await ybot(ImportChatInviteRequest(hash=username))
 except:
  continue
 async for user in ubot.iter_participants(username):
   if not user.bot:
     if user.username:
       members.append(user.username)

@tbot.on(events.NewMessage(pattern="^/members$"))
async def mem(event):
 if len(members) == 0:
   return await event.reply("Scrape some members first")
 with io.BytesIO(str.encode(str(members))) as out_file:
    out_file.name = "members.txt"
    await tbot.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=str(len(members)),
                reply_to=reply_to_id,
            )
