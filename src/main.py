import discord

class Client(discord.Client):
    async def on_ready(self):
        print(f"The Bot is running and logged on as {self.user}")

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('السلام عليكم يا قروب الدعم'):
            await message.channel.send(f'وعليكم السلام {message.author}')

        if message.content.startswith('بوت مساعدة'):
            await message.channel.send(f'انقلع')

        if message.content.startswith('اي بي ماينكرافت') or message.content.startswith('ايبي ماينكرافت') or message.content.startswith('آي بي ماينكرافت') or message.content.startswith('آيبي ماينكرافت') or message.content.startswith('عنوان ماينكرافت'):
            await message.channel.send(f'NOT Implemented :(')

        if message.content.startswith('بوت من انت') or message.content.startswith('بوت من أنت'):
            await message.channel.send(f'هلا {message.author} أنا بوت قروب الدعم مكتوب بلغة بايثون والكود حقي مفتوح المصدر وأنا هنا لمساعدتك أخي الكريم')

        if message.content.startswith('d3m source code'):
            await message.channel.send(f'https://github.com/5cfp/d3mbot')




intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)

#create token.txt file and put the token in the first line
with open('src/token.txt', 'r') as tokenfile:
    token = tokenfile.readline()
client.run(token.strip())