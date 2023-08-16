import time
import random
from pyrogram import Client, filters

CMD = ["/", "."]

@Client.on_message(filters.command("alive", CMD))
async def check_alive(_, message):
    await message.reply_text("Lᴜᴄᴋʟʏ I Aᴍ Aʟɪᴠᴇ :) Pʀᴇss 👉 /start \n\nPʀᴇss 👉 /help Fᴏʀ Hᴇʟᴩ ;)\n\n\nPʀᴇss 👉 /ping Tᴏ Cʜᴇᴄᴋ Mʏ Pɪɴɢ 😁")

@Client.on_message(filters.command("help", CMD))
async def help(_, message):
    await message.reply_text("Pʀᴇss 👉 /movies Fᴏʀ Hᴏᴡ Tᴏ Rᴇǫᴜᴇsᴛ Mᴏᴠɪᴇs Iɴ A Pʀᴏᴩᴇʀ Wᴀʏ 📃\n\nPʀᴇss 👉 /series Fᴏʀ Hᴏᴡ Tᴏ Rᴇǫᴜᴇsᴛ Sᴇʀɪᴇs Iɴ A Pʀᴏᴩᴇʀ Wᴀʏ 📃\n\n\nPʀᴇss 👉 /tutorial Fᴏʀ Tᴜᴛᴏʀɪᴀʟ Aʙᴏᴜᴛ Hᴏᴡ Tᴏ Gᴇᴛ Dɪʀᴇᴄᴛ Fɪʟᴇs Fʀᴏᴍ Mᴇ 🤗")

@Client.on_message(filters.command("credits", CMD))
async def help(_, message):
    await message.reply_text("Tʜɪs Is Cᴏᴅᴇᴅ Bʏ @Waldy_Writings/n/nTʜɪs Is Aɴ Oᴩᴇɴ Sᴏᴜʀᴄᴇ Pʀᴏᴊᴇᴄᴛ Sᴏ Sᴜᴩᴩᴏʀᴛ Aɴᴅ Dᴏɴ´ᴛ Sᴇʟʟ Fᴏʀ Mᴏɴᴇʏ")

@Client.on_message(filters.command("movies", CMD))
async def movie(_, message):
    await message.reply_text("⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\nᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ\n⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\n\nɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ ғʀᴏᴍ ɢᴏᴏɢʟᴇ ➠ ᴘᴀsᴛᴇ ᴄᴏᴘɪᴇᴅ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ ɪɴ ᴛʜᴇ ʙᴏᴛ ᴏʀ ʀᴇǫᴜᴇsᴛ ɢʀᴏᴜᴘ\n\nᴇxᴀᴍᴘʟᴇ : ᴠɪᴋʀᴀᴍ 2022 ᴇʟᴀ ɴᴀᴍᴇ ᴀɴᴅ ʏᴇᴀʀ ᴘᴇᴛᴀɴᴅɪ\n\n🚯 ᴅᴏɴᴛ ᴛʏᴘᴇ ɪɴ ᴛʜɪs ғᴏʀᴍᴀᴛ 🤧 ➠ :(ʟᴀɴɢᴜᴀɢᴇ ᴍᴇɴᴛɪᴏɴ ᴄʜᴇʏᴀᴋᴀɴᴅɪɪ,ᴀɴᴅ ᴍᴀɪɴ ᴛʜɪɴɢ ᴛʜᴇᴀᴛʀᴇ ᴘʀɪɴᴛs ᴀʀᴇ ɴᴏᴛ ᴜᴘʟᴏᴀᴅᴇᴅ ɪɴ ᴏᴜʀ ʙᴏᴛ⚠️⚠️)\n\nᴄᴏᴅᴇᴅ ʙʏ ᴡᴀʟᴅʏ_ᴡʀɪᴛɪɴɢꜱ")

@Client.on_message(filters.command("series", CMD))
async def series(_, message):
    await message.reply_text("⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\nꜱᴇʀɪᴇꜱ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ\n⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\n\nɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ sᴇʀɪᴇs ɴᴀᴍᴇ ᴀᴅᴅ sᴇᴀsᴏɴ ɴᴜᴍʙᴇʀ ʟɪᴋᴇ s01 ʙᴇsɪᴅᴇ sᴇʀɪᴇs ɴᴀᴍᴇ ➠ ᴘᴀsᴛᴇ ᴄᴏᴘɪᴇᴅ sᴇʀɪᴇs ɴᴀᴍᴇ ᴡɪᴛʜ sᴇᴀsᴏɴ ɪɴ ᴛʜᴇ ʙᴏᴛ ᴏʀ ʀᴇǫᴜᴇsᴛ ɢʀᴏᴜᴘ\n\nᴇxᴀᴍᴘʟᴇ : ꜱᴛʀᴀɴɢᴇʀ ᴛʜɪɴɢꜱ S01\n\n🚯ᴅᴏɴᴛ ᴛʏᴘᴇ ɪɴ ᴛʜɪs ғᴏʀᴍᴀᴛ ➠ ':(ᴍᴏɴᴇʏ ʜᴇɪsᴛ sᴇᴀsᴏɴ 1.... ᴇʟᴀ ᴛʏᴘᴇ ᴄʜᴇsᴛʜᴇ ʀᴀᴠᴜ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ғᴏʀᴍᴀᴛ ʟᴏ ᴘᴀᴍᴘᴀʟɪ ᴘᴀɪɴᴀ ғᴏʀᴍᴀᴛ ᴄʜᴜᴅᴀɴᴅɪ\n\nᴄᴏᴅᴇᴅ ʙʏ ᴡᴀʟᴅʏ_ᴡʀɪᴛɪɴɢꜱ")

@Client.on_message(filters.command("download", CMD))
async def tutorial(_, message):
    await message.reply_text("Sᴇɴᴅ Aɴʏ Mᴏᴠɪᴇs / Sᴇʀɪᴇs Nᴀᴍᴇ Wɪᴛʜ Cᴏᴛᴛᴇᴄᴛ Sᴩᴇʟʟɪɴɢ Aɴᴅ I Wɪʟʟ Sᴇɴᴅ Tʜᴇ Fɪʟᴇ Lɪɴᴋ... \n\n Cᴏʀʀᴇᴄᴛ Mᴏᴠɪᴇ Rᴇǫᴜᴇsᴛɪɴɢ Mᴇᴛʜᴏᴅ 👉 /movies \n\nCᴏʀʀᴇᴄᴛ Sᴇʀɪᴇs Rᴇǫᴜᴇsᴛɪɴɢ Mᴇᴛʜᴏᴅ 👉 /series")

@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...........")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pɪɴɢ🔥!\n{time_taken_s:.3f} ms")
