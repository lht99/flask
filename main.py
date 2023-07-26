import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InputMediaVideo


api_id = 11278509
api_hash = "46b8cf52db33933409348af1b7c22c6b"
app = Client("my_account", api_id=api_id, api_hash=api_hash,bot_token = '6389568336:AAH3GtFv7fJ3guA8Z6row6BjOehidS4ABis')


async def tuan(chatID, message):
  try:
    t = await message.reply_text(f"Hello: {chatID}")
    async def progress(current, total):
      await t.edit_text(f"{current * 100 / total:.1f}%")
    #await message.reply_video(video="C:\\Users\\KITECH2\\Downloads\\iCloud Photos.zip", progress=progress)
    #await message.reply_text(l)
  except:
    await message.reply_text("Loi khong gui duoc video")
    print('loi')

@app.on_message(filters.private)
async def echo(client, message):
                            chatID = message.chat.id
                            await tuan(chatID, message)

print("Bot started")
app.run()
print("Bot Stopped")
