import discord
prefix = "!"

class MyClient(discord.Client):
    async def on_ready(self):
        print('El indult a ', self.user, 'bot')

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == prefix + 'Szia': await message.channel.send('Szia')
        if message.content == prefix + 'Ping': await message.channel.send('Pong')
        if message.content== prefix +  'dm' : await message.author.send('A dm teszt sikeres volt')
        if message.content== prefix + "Invite": await message.author.send("https://discordapp.com/api/oauth2/authorize?client_id=608718486122004490&scope=bot&permissions=0")

client = MyClient()
client.run('NjE2OTQ4MjIzMDI1ODcyODk2.XWj_zg.wLs7eB-Nf5UoKj9b4OPGjfK5oYA')
