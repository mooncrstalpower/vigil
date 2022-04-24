import discord
token = 'OTY3MDYyMDczOTI4NDY2NTAy.YmK0vQ.Do1V3UK-B7qQ-mSsb26o_oyAong' #봇 토큰
client = discord.Client()


@client.event
async def on_ready():

    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다')
    game = discord.Game('비질 명령어: !삭제 , 말보다는 , 퓨즈 , 룩 , 몽타뉴 , 카베이라 , 발키리 , 애쉬 , 도깨비 , 군주님') #봇 ~하는중 입력
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "말보다는": 
        await message.channel.send (f"행동이지")
    if message.content == "퓨즈": 
        await message.channel.send (f"https://i.ytimg.com/vi/XplzilWzUog/maxresdefault.jpg")
    if message.content == "룩": 
        await message.channel.send (f"https://i.pinimg.com/736x/50/f3/90/50f3908b62c39c2aae0fa27d0fe64c69.jpg")
    if message.content == "몽타뉴": 
        await message.channel.send (f"https://i3.ruliweb.com/img/19/08/04/16c5b4cebc74a5412.jpg")
    if message.content == "카베이라": 
        await message.channel.send (f"https://i.ytimg.com/vi/hMx9YqX3n3M/hqdefault.jpg")
    if message.content == "발키리": 
        await message.channel.send (f"https://opgg-com-image.akamaized.net/attach/images/20201004042714.1390629.jpg")
    if message.content == "애쉬": 
        await message.channel.send (f"https://ac2-p2.namu.la/20211113s2/3225b0bb864707b4a01883af68510a9e47c4d7d22787abb31259ea418a7751f2.jpg")
    if message.content == "도깨비": 
        await message.channel.send (f"https://cdn.discordapp.com/attachments/967048643867738155/967273058903666769/174074ef8954b8183.mp4")
    if message.content == "군주님": 
        await message.channel.send (f"https://post-phinf.pstatic.net/MjAxODA0MjZfMjk2/MDAxNTI0Njc1NzkwMjY4.0Pa_pzQb6t7n8joccWWtzWKN6vM0QQPKFOky7XcQHuQg.vIqzTghybT07M_pe74vnvh1cXTNo6d7cyYEM3aKIxg8g.JPEG/CwXSlgzXUAEdawe.jpg?type=w1200 https://www.youtube.com/watch?v=ipenAIzb_18") #봇이 '안녕하세요'라고 대답
    if message.content == "!비질 명령어": 
        await message.channel.send (f"!삭제 , 말보다는 , 퓨즈 , 룩 , 몽타뉴 , 카베이라 , 발키리 , 애쉬 , 도깨비 , 군주님")

    if message.content.startswith("!삭제"):
        number = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=number)
        await message.channel.send(f"{number}개의 채팅을 삭제했다 말보다는 행동이지.")


client.run(token)