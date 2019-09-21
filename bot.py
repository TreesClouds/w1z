import discord
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

client = discord.Client()
cli = MongoClient(os.getenv('MONGO'))
db = cli.heroku_zq5cdk49

bal = db.doc.find_one({'_id': ObjectId('5d5779523f5cc0f1bdd8511a')})
status = db.doc.find_one({'_id': ObjectId('5d5779523f5cc0f1bdd8511b')})
rqtype = db.doc.find_one({'_id': ObjectId('5d5779523f5cc0f1bdd8511c')})
rqdesc = db.doc.find_one({'_id': ObjectId('5d5779523f5cc0f1bdd8511d')})
rqserv = db.doc.find_one({'_id': ObjectId('5d5779523f5cc0f1bdd8511e')})
mess = db.doc.find_one({'_id': ObjectId('5d5779523f5cc0f1bdd8511f')})
slots = db.doc.find_one({'_id': ObjectId('5d5b51f233ba3bc7166344e3')})

typ = {}
version = "v1.2.5"


@client.event
async def on_ready():
    guild = client.get_guild(469591475999604746)
    channel = client.get_channel(612112677166252050)
    await channel.send(f"""<:bfyYes:613851579266760733> Bot started on **{version}**""")
    await client.change_presence(activity=discord.Activity(name=f"""{guild.member_count} members""", type=discord.ActivityType.watching))


@client.event
async def on_member_join(member):
    guild = client.get_guild(469591475999604746)  # Blob-ify
    guild1 = client.get_guild(591038750273044501)  # Pixel Blob Central FLAG!
    if member.guild == guild:
        await client.change_presence(activity=discord.Activity(name=f"""{guild.member_count} members""", type=discord.ActivityType.watching))
        channel = client.get_channel(469591475999604750)
        await channel.send(f"""<a:party:582383854262943745> Hey fellow **blob {member.mention}**, welcome to **Blob-ify**! You're the **{member.guild.member_count}th** blob to join our growing blob community! To get started, please check <#470303845495341057>. In order to request a blob, please check <#526232642425978892>. Have fun! <a:wumpusheart:582383394516631552>""")
    elif member.guild == guild1:
        channel = client.get_channel(591038750847533058)
        await channel.send(f"""<a:party:582383854262943745> Hey fellow **blob {member.mention}**, welcome to **{member.guild.name}**! You're the **{member.guild.member_count}th** blob to join our growing blob community! Have fun! <a:wumpusheart:582383394516631552>""")


@client.event
async def on_member_remove(member):
    guild = client.get_guild(469591475999604746)
    if member.guild == guild:
        await client.change_presence(activity=discord.Activity(name=f"""{guild.member_count} members""", type=discord.ActivityType.watching))


@client.event
async def on_message(message):
    guild = client.get_guild(469591475999604746)  # Blob-ify
    lower = message.content.lower()
    split = lower.split(" ")
    if message.author.id not in typ.keys():
        typ[message.author.id] = 0
    if str(message.author.id) not in status.keys():
        status[str(message.author.id)] = 0
    if str(message.author.id) not in bal.keys():
        bal[str(message.author.id)] = 0
    if message.author.guild != guild:
        typ[message.author.id] = -1
    if typ[message.author.id] == -1:
        if message.author.guild == guild:
            typ[message.author.id] = 0
    if lower == "cancel":
        if typ[message.author.id] > 0:
            await message.channel.send("<:bfyNo:613851611600781342> **The requested action has been canceled.**")
            typ[message.author.id] = 0
            rqtype[str(message.author.id)], rqdesc[str(message.author.id)], rqserv[str(message.author.id)] = "", "", ""
    elif message.author.id == 292953664492929025:
        if "w.exc" in message.content:
            mem = message.content.split(" ")
            user = str(client.get_user(int(mem[1])))
            if user not in bal.keys():
                bal[user] = 0
            await message.channel.send("<:bfyYes:613851579266760733> 2 <:blobpoint:577932728033476611> have been added to your account.")
            bal[user] += 2
            channel = client.get_channel(471878672677208084)
            await channel.send(f"""**Bank Update:** Bal of {user} now {bal[user]}""")
    else:
        if typ[message.author.id] <= 0:
            if lower == "w.help":
                embed = discord.Embed(title="Blob Bot Help", description="The full list of W1Z4RD's commands", color=0x0080c0)
                embed.add_field(name="w.request", value="Request a blob")
                embed.add_field(name="w.exchange", value="Exchange 2 BLOB POINTS for 2,500 BLOB COINS")
                embed.add_field(name="w.balance", value="Check your BLOB POINT balance")
                embed.add_field(name="w.request delete", value="Delete your current blob request")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/470304317748805652/581650589423763463/wiz.png")
                embed.set_footer(text=f"""Created by Tri#4823 ~ W1Z4RD {version}""")
                await message.channel.send(content=None, embed=embed)
            elif lower == "w.exchange":
                mem = str(message.author.id)
                truemem = str(message.author)
                if mem not in bal.keys():
                    bal[mem] = 0
                if bal[mem] > 1:
                    await message.channel.send("<:bfyYes:613851579266760733> <@266319920009183242> will complete the transaction within 24 hours.")
                    bal[mem] -= 2
                    channel = client.get_channel(471878672677208084)
                    await channel.send(f"""**Bank Update:** Bal of {truemem} now {bal[mem]}""")
                else:
                    await message.channel.send("<:bfyNo:613851611600781342> You do not have enough <:blobpoint:577932728033476611> to do so.")
            elif lower == "w.request":
                if slots["used"] < slots["max"] or guild.get_role(600678332320710666) in message.author.roles:
                    if status[str(message.author.id)] == 0:
                        embed = discord.Embed(title="W1Z Request Command", description="A full list of all blob types!", color=0x0080c0)
                        embed.set_image(url="https://cdn.discordapp.com/attachments/470304317748805652/624941100418859018/5309c984-4d97-40c1-bbeb-24f5045d5ddf.png")
                        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/470304317748805652/581650589423763463/wiz.png")
                        embed.set_footer(text=f"""Created by Tri#4823 ~ W1Z4RD {version}""")
                        await message.channel.send(content="__Please respond with the respective number, or `cancel`__", embed=embed)
                        typ[message.author.id] += 1
                    else:
                        await message.channel.send("<:bfyNo:613851611600781342> You currently have a request in the queue. Either wait until the request is done or delete your request to request again. You can also choose to edit your request.")
                else:
                    await message.channel.send("<:bfyNo:613851611600781342> The maximum amount of request slots has been reached. Either wait for a slot to open or boost the server to bypass this.")
            elif lower == "w.balance":
                await message.channel.send(f"""**Your Balance:** {bal[str(message.author.id)]} <:blobpoint:577932728033476611>""")
            elif lower == "w.bal":
                await message.channel.send(f"""**Your Balance:** {bal[str(message.author.id)]} <:blobpoint:577932728033476611>""")
            elif "w.say" == split[0]:
                admin = guild.get_role(471024426356310028)
                if admin in message.author.roles:
                    say = message.content.split(" ", 1)
                    await message.channel.send(f"""{say[1]}""")
                    await message.delete()
                else:
                    await message.channel.send("<:bfyNo:613851611600781342> You do not have the required permissions to use this command.")
            elif "w.add" == split[0]:
                admin = guild.get_role(471024426356310028)
                if admin in message.author.roles:
                    say = message.content.split(" ", 2)
                    user = client.get_user(int(say[1]))
                    if str(user.id) not in bal.keys():
                        bal[str(user.id)] = 0
                    bal[str(user.id)] += int(say[2])
                    await message.channel.send(f"""<:bfyYes:613851579266760733> **{say[2]}bp** has/have been added to {str(user)}'s balance""")
                    channel = client.get_channel(471878672677208084)
                    await channel.send(f"""**Bank Update:** Bal of {str(user)} now {bal[str(user.id)]}""")
                else:
                    await message.channel.send("<:bfyNo:613851611600781342> You do not have the required permissions to use this command.")
            elif "w.remove" == split[0]:
                admin = guild.get_role(471024426356310028)
                if admin in message.author.roles:
                    say = message.content.split(" ", 2)
                    user = client.get_user(int(say[1]))
                    if str(user.id) not in bal.keys():
                        bal[str(user.id)] = 0
                    bal[str(user.id)] -= int(say[2])
                    await message.channel.send(f"""<:bfyYes:613851579266760733> **{say[2]}bp** has/have been removed from {str(user)}'s balance""")
                    channel = client.get_channel(471878672677208084)
                    await channel.send(f"""**Bank Update:** Bal of {str(user)} now {bal[str(user.id)]}""")
                else:
                    await message.channel.send("<:bfyNo:613851611600781342> You do not have the required permissions to use this command.")
            elif "w.slots" == split[0]:
                admin = guild.get_role(471024426356310028)
                if admin in message.author.roles:
                    if "set" == split[1]:
                        slots["max"] = int(split[2])
                        await message.channel.send(f"""<:bfyYes:613851579266760733> Max slots now **{split[2]}**.""")
                    elif "check" == split[1]:
                        await message.channel.send(f"""There are **{slots["used"]} out of {slots["max"]} slots used.**""")
                    elif "forceremove" == split[1]:
                        if slots["used"] > 0:
                            slots["used"] -= 1
                            await message.channel.send(f"""<:bfyYes:613851579266760733> Used slots reduced by 1, now {slots["used"]}.""")
                        else:
                            await message.channel.send("<:bfyNo:613851611600781342> There are no requests in the queue or there are no slots used.")
                    elif "forceadd" == split[1]:
                        slots["used"] += 1
                        await message.channel.send(f"""<:bfyYes:613851579266760733> Forcefully used a slot. Used slots now {slots["used"]}.""")
                else:
                    await message.channel.send("<:bfyNo:613851611600781342> You do not have the required permissions to use this command.")
            elif lower == "w.emojiupdate":
                admin = guild.get_role(471024426356310028)
                if admin in message.author.roles:
                    channel = client.get_channel(578237505770618891)
                    async for message1 in channel.history():
                        await message1.delete()
                    for emoji in guild.emojis:
                        await channel.send(f"""{emoji} ~ `{emoji.name}`""")
                else:
                    await message.channel.send("<:bfyNo:613851611600781342> You do not have the required permissions to use this command.")
            elif "w.request" == split[0]:
                if "delete" == split[1]:
                    if status[str(message.author.id)] > 0:
                        await message.channel.send("Are you sure you would like to delete your request? Your <:blobpoint:577932728033476611> will be refunded. Please `confirm` or `cancel`.")
                        typ[message.author.id] = 5
                    else:
                        await message.channel.send("<:bfyNo:613851611600781342> You currently have no active requests to delete.")
                elif "claim" == split[1]:
                    print()
                elif "submit" == split[1]:
                    print()
                elif "check" == split[1]:
                    stat = status[str(message.author.id)]
                    if stat > 0:
                        embed = discord.Embed(title=f"""Your Request""", color=0x0080c0)
                        embed.add_field(name="Blob Type", value=rqtype[str(message.author.id)])
                        embed.add_field(name="Blob Description", value=rqdesc[str(message.author.id)])
                        embed.add_field(name="Server Blob?", value=rqserv[str(message.author.id)])
                        embed.set_thumbnail(
                            url="https://cdn.discordapp.com/attachments/470304317748805652/581650589423763463/wiz.png")
                        embed.set_footer(text=f"""Created by Tri#4823 ~ W1Z4RD {version}""")
                        if stat == 1:
                            await message.channel.send(content="Your request is **unclaimed**. You can edit it with the `edit` subommand.", embed=embed)
                        elif stat == 2:
                            await message.channel.send(content="Your request was claimed by artist [ARTIST]. The request is no longer able to be edited")
                    else:
                        await message.channel.send("<:bfyNo:613851611600781342> You do not have a request in the queue. Use the `w.request` command to create one.")
                elif "forcedelete" == split[1]:
                    admin = guild.get_role(471024426356310028)
                    if admin in message.author.roles:
                        user = client.get_user(int(split[2]))
                        if status[str(user.id)] > 0:
                            status[str(user.id)] = 0
                            slots["used"] -= 1
                            if rqtype[str(user.id)] == "Animated Blob":
                                bal[str(user.id)] += 6
                            if rqtype[str(user.id)] == "Normal Blob":
                                bal[str(user.id)] += 1
                            elif rqtype[str(user.id)] == "Bongo Cat":
                                bal[str(user.id)] += 7
                            elif rqtype[str(user.id)] == "Peep":
                                bal[str(user.id)] += 3
                            elif rqtype[str(user.id)] == "Animated Peep":
                                bal[str(user.id)] += 8
                            elif rqtype[str(user.id)] == "Full Blob Pack":
                                bal[str(user.id)] += 40
                            elif rqtype[str(user.id)] == "Custom Emoji":
                                bal[str(user.id)] += 10
                            elif rqtype[str(user.id)] == "Custom Emoji Pack":
                                bal[str(user.id)] += 80
                            await message.channel.send(f"""<:bfyYes:613851579266760733> You have forcefully deleted {str(user)}'s request. You may proceed to delete the message in the queue.""")
                        else:
                            await message.channel.send("<:bfyNo:613851611600781342> That user has no request in the queue.")
                    else:
                        await message.channel.send("<:bfyNo:613851611600781342> You do not have the required permissions to use this subcommand.")
        elif typ[message.author.id] == 1:
            if "1" in message.content:
                if bal[str(message.author.id)] >= 1:
                    await message.channel.send("__Great Choice! Now, please state what you would like your blob(s) to look like, or say `cancel`.__")
                    rqtype[str(message.author.id)] = "Normal Blob"
                    typ[message.author.id] += 1
                else:
                    await message.channel.send("<:bfyNo:613851611600781342> You do not have enough <:blobpoint:577932728033476611> to request this item. Pick a different item or `cancel`.")
            elif "2" in message.content:
                if bal[str(message.author.id)] >= 6:
                    await message.channel.send("__Great Choice! Now, please state what you would like your blob(s) to look like, or say `cancel`.__")
                    rqtype[str(message.author.id)] = "Animated Blob"
                    typ[message.author.id] += 1
                else:
                    await message.channel.send("<:bfyNo:613851611600781342> You do not have enough <:blobpoint:577932728033476611> to request this item. Pick a different item or `cancel`.")
            elif "3" in message.content:
                if bal[str(message.author.id)] >= 7:
                    await message.channel.send("__Great Choice! Now, please state what you would like your blob(s) to look like, or say `cancel`.__")
                    rqtype[str(message.author.id)] = "Bongo Cat"
                    typ[message.author.id] += 1
                else:
                    await message.channel.send("<:bfyNo:613851611600781342> You do not have enough <:blobpoint:577932728033476611> to request this item. Pick a different item or `cancel`.")
            elif "4" in message.content:
                if bal[str(message.author.id)] >= 3:
                    await message.channel.send("__Great Choice! Now, please state what you would like your blob(s) to look like, or say `cancel`.__")
                    rqtype[str(message.author.id)] = "Peep"
                    typ[message.author.id] += 1
                else:
                    await message.channel.send("<:bfyNo:613851611600781342> You do not have enough <:blobpoint:577932728033476611> to request this item. Pick a different item or `cancel`.")
            elif "5" in message.content:
                if bal[str(message.author.id)] >= 8:
                    await message.channel.send("__Great Choice! Now, please state what you would like your blob(s) to look like, or say `cancel`.__")
                    rqtype[str(message.author.id)] = "Animated Peep"
                    typ[message.author.id] += 1
                else:
                    await message.channel.send("<:bfyNo:613851611600781342> You do not have enough <:blobpoint:577932728033476611> to request this item. Pick a different item or `cancel`.")
            elif "6" in message.content:
                if bal[str(message.author.id)] >= 40:
                    await message.channel.send("__Great Choice! Now, please state what you would like your blob(s) to look like, or say `cancel`.__")
                    rqtype[str(message.author.id)] = "Full Blob Pack"
                    typ[message.author.id] += 1
                else:
                    await message.channel.send("<:bfyNo:613851611600781342> You do not have enough <:blobpoint:577932728033476611> to request this item. Pick a different item or `cancel`.")
            elif "7" in message.content:
                if bal[str(message.author.id)] >= 10:
                    await message.channel.send("__Great Choice! Now, please state what you would like your blob(s) to look like, or say `cancel`.__")
                    rqtype[str(message.author.id)] = "Custom Emoji"
                    typ[message.author.id] += 1
                else:
                    await message.channel.send("<:bfyNo:613851611600781342> You do not have enough <:blobpoint:577932728033476611> to request this item. Pick a different item or `cancel`.")
            elif "8" in message.content:
                if bal[str(message.author.id)] >= 80:
                    await message.channel.send("__Great Choice! Now, please state what you would like your blob(s) to look like, or say `cancel`.__")
                    rqtype[str(message.author.id)] = "Custom Emoji Pack"
                    typ[message.author.id] += 1
                else:
                    await message.channel.send("<:bfyNo:613851611600781342> You do not have enough <:blobpoint:577932728033476611> to request this item. Pick a different item or `cancel`.")
            else:
                await message.channel.send("<:bfyNo:613851611600781342> That was not a valid response. Send a number from 1 through 8.")
        elif typ[message.author.id] == 2:
            await message.channel.send("__Great! One last thing. Would you like this to be a server blob?__")
            await message.channel.send("Server blobs represent you in the server, and are made into emojis that you can use with Nitro.")
            await message.channel.send("However, only NORMAL BLOB requests can qualify. So what do you say, or `cancel`.")
            rqdesc[str(message.author.id)] = message.content
            typ[message.author.id] += 1
        elif typ[message.author.id] == 3:
            await message.channel.send("Cool! Now please confirm the following details before making your purchase.")
            await message.channel.send("The appropriate amount of <:blobpoint:577932728033476611> will be deducted from your account as listed in <#526232642425978892>.")
            embed = discord.Embed(title="Confirm Information", description="Either `confirm` or `cancel`", color=0x0080c0)
            embed.add_field(name="Blob Type", value=rqtype[str(message.author.id)])
            embed.add_field(name="Blob Description", value=rqdesc[str(message.author.id)])
            embed.add_field(name="Server Blob?", value=message.content)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/470304317748805652/581650589423763463/wiz.png")
            embed.set_footer(text=f"""Created by Tri#4823 ~ W1Z4RD {version}""")
            await message.channel.send(embed=embed)
            rqserv[str(message.author.id)] = message.content
            typ[message.author.id] += 1
        elif typ[message.author.id] == 4:
            if lower == "confirm":
                await message.channel.send("<:bfyYes:613851579266760733> The blob request has been added to the queue!")
                await message.channel.send("You will receive notifications as your blob is being made.")
                await message.channel.send("Send any image references to <@266319920009183242>.")
                embed = discord.Embed(title=f"""{message.author}""", color=0x0080c0)
                embed.add_field(name="Blob Type", value=rqtype[str(message.author.id)])
                embed.add_field(name="Blob Description", value=rqdesc[str(message.author.id)])
                embed.add_field(name="Server Blob?", value=rqserv[str(message.author.id)])
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/470304317748805652/581650589423763463/wiz.png")
                embed.set_footer(text=f"""Created by Tri#4823 ~ W1Z4RD {version}""")
                channel = client.get_channel(611768294315130891)
                await channel.send(content=f"""**Incoming Blob Request!** From {message.author.mention}""", embed=embed)
                typ[message.author.id] = 0
                status[str(message.author.id)] = 1
                slots["used"] += 1
                if rqtype[str(message.author.id)] == "Animated Blob":
                    bal[str(message.author.id)] -= 6
                elif rqtype[str(message.author.id)] == "Normal Blob":
                    bal[str(message.author.id)] -= 1
                elif rqtype[str(message.author.id)] == "Bongo Cat":
                    bal[str(message.author.id)] -= 7
                elif rqtype[str(message.author.id)] == "Peep":
                    bal[str(message.author.id)] -= 3
                elif rqtype[str(message.author.id)] == "Animated Peep":
                    bal[str(message.author.id)] -= 8
                elif rqtype[str(message.author.id)] == "Full Blob Pack":
                    bal[str(message.author.id)] -= 40
                elif rqtype[str(message.author.id)] == "Custom Emoji":
                    bal[str(message.author.id)] -= 10
                elif rqtype[str(message.author.id)] == "Custom Emoji Pack":
                    bal[str(message.author.id)] -= 80
            else:
                await message.channel.send("<:bfyNo:613851611600781342> That was not a valid response. Please `confirm` or `cancel`.")
        elif typ[message.author.id] == 5:
            if lower == "confirm":
                await message.channel.send("<:bfyYes:613851579266760733> <@266319920009183242> will proceed to delete your request and refund your <:blobpoint:577932728033476611>. At this point you may also start a new request.")
                status[str(message.author.id)] = 0
                typ[message.author.id] = 0
                slots["used"] -= 1
                if rqtype[str(message.author.id)] == "Animated Blob":
                    bal[str(message.author.id)] += 6
                elif rqtype[str(message.author.id)] == "Normal Blob":
                    bal[str(message.author.id)] += 1
                elif rqtype[str(message.author.id)] == "Bongo Cat":
                    bal[str(message.author.id)] += 7
                elif rqtype[str(message.author.id)] == "Peep":
                    bal[str(message.author.id)] += 3
                elif rqtype[str(message.author.id)] == "Animated Peep":
                    bal[str(message.author.id)] += 8
                elif rqtype[str(message.author.id)] == "Full Blob Pack":
                    bal[str(message.author.id)] += 40
                elif rqtype[str(message.author.id)] == "Custom Emoji":
                    bal[str(message.author.id)] += 10
                elif rqtype[str(message.author.id)] == "Custom Emoji Pack":
                    bal[str(message.author.id)] += 80
                channel = client.get_channel(471878672677208084)
                await channel.send(f"""{str(message.author)} has deleted their request.""")
            else:
                await message.channel.send("<:bfyNo:613851611600781342> That was not a valid response. Please `confirm` or `cancel`.")

    dicts = [bal, status, rqtype, rqdesc, rqserv, mess, slots]
    for d in dicts:
        db.doc.replace_one({'_id': d['_id']}, d, True)


@client.event
async def on_guild_emojis_update(guild0, before, after):
    channel = 0
    if guild0.id == 469591475999604746:
        channel = client.get_channel(570397486141669406)
    emoadd, emoaddname, emoremove, emoremovename, lis, lis2 = "", "", "", "", [], []
    for emoji in before:
        for emoji2 in after:
            lis.append(emoji2.name)
        if emoji.name not in lis:
            emoremove = emoji
            emoremovename = emoji.name
    for emoji in after:
        for emoji2 in before:
            lis2.append(emoji2.name)
        if emoji.name not in lis2:
            emoadd = emoji
            emoaddname = emoji.name
    if emoremove == "":  # If an emoji was added
        await channel.send(f"""<:w1:579473596041265152> **Added** {emoadd} `{emoaddname}`""")
    else:  # If an emoji was removed
        if emoadd == "":  # If an emoji was ONLY removed
            await channel.send(f"""<:w2:579473617134288898> **Removed** `{emoremovename}`""")
        else:  # If an emoji was renamed
            await channel.send(f"""<:w3:579473645706018827> {emoadd} **Renamed** `{emoremovename}` to `{emoaddname}`""")


client.run(os.getenv('TOKEN'))
