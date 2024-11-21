def setup():
    print('Please answer the following questions to complete the setup.')
    baka_username = input('Please enter your username in bakaláři: ')
    baka_password = input('Please input password for your account in bakaláři: ')
    gemini_api_key = input('Please enter your google gemini api key: ')
    discord_token = input('Please enter your discord bot token: ')

    if not baka_username or not baka_password or not gemini_api_key or not discord_token:
        print('You left some field unfilled >:( Please try again.')
        setup()
    else:
        with open('.env', 'w') as f:
            f.write(f'BAKA_USERNAME={baka_username}\n')
            f.write(f'BAKA_PASSWORD={baka_password}\n')
            f.write(f'GEMINI_API_KEY={gemini_api_key}\n')
            f.write(f'DISCORD_TOKEN={discord_token}\n')