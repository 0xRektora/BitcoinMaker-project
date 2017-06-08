import BitmakerBot

MyBot = BitmakerBot.BotMaker()
while True:
    try:
        MyBot.Start()
    except Exception as e:
        print("[-]Exception catch : " + e)
        print("\nRe launching the app.")
        continue
