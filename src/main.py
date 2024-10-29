import discord
import urllib.request
from mcstatus import JavaServer


class Client(discord.Client):
    async def on_ready(self):
        print(f"The Bot is Running!!!")

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('السلام عليكم يا قروب الدعم') or message.content.startswith('السلام عليكم') or message.content.startswith('سلام عليكم'):
            await message.channel.send(f'وعليكم السلام {message.author}')

        if message.content.startswith('بوت مساعدة'):
            await message.channel.send(f'للحصول على اي بي سيرفر ماين كرافت اكتب اي بي ماينكرافت')

        if message.content.startswith('اي بي ماينكرافت') or message.content.startswith('ايبي ماينكرافت') or message.content.startswith('آي بي ماينكرافت') or message.content.startswith('آيبي ماينكرافت') or message.content.startswith('عنوان ماينكرافت'):
            mcip = urllib.request.urlopen('https://api.ipify.org').read().decode('utf8')
        
            try:
                server = JavaServer.lookup(mcip)
                status = server.status()
                await message.channel.send("السيرفر شغال وعنوان السيرفر هو " + mcip)
            except:
                await message.channel.send("السيرفر طافي")

        if message.content.startswith('بوت من انت') or message.content.startswith('بوت من أنت'):
            await message.channel.send(f'هلا {message.author} أنا بوت قروب الدعم مكتوب بلغة بايثون والكود حقي مفتوح المصدر وأنا هنا لمساعدتك أخي الكريم')

        if message.content.startswith('d3m source code'):
            await message.channel.send(f'https://github.com/5cfp/d3mbot')

        if message.content.startswith('تحكم داخلي'):
            await message.channel.send(f'يتم التحكم بالبوت من قبل المشغل')
            while(1):
                mess = input("Enter message:")
                if mess == "stopcon":
                    await message.channel.send(f'هلا انا البوت رجعت طبيعي')
                    return
                else:
                    await message.channel.send(mess)


intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)

#create token.txt file and put the token in the first line
try:
    with open('token.txt', 'r') as tokenfile:
        token = tokenfile.readline()
except:
    with open('src/token.txt', 'r') as tokenfile:
        token = tokenfile.readline()    
client.run(token.strip())