import webbrowser

choice = ''

activity_options = {"DEFAULT": ['habitica.com', 'tomato-timer.com', 'wunderlist.com'],
                    "accounting":['discover.com/', 'chase.com/', 'capitalone.com/',
                                  'online.citi.com', 'mint.com', 'amazon.com'],
                    "chill":['facebook.com', 'read.amazon.com/', 'youtube.com/channel/UC-27_Szq7BtHDoC0R2U0zxA'],
                    "code": ['automatetheboringstuff.com/','udemy.com', 'kaggle.com', 'github.com'],
                    "coding challenges": ['hackerrank.com/dashboard', 'projecteuler.net', 'codingame.com'],
                    "learn":['youtube.com/channel/UCsXVk37bltHxD1rDPwtNM8Q'],
                    "pick stocks": ['finviz.com', 'finance.yahoo.com/', 'stockflare.com', 'stockta.com'],
                    "web dev": ['siteground.com', 'burkit.life/', 'supsist.com/', 'wordpress.com'],
                    "work":['remote.blackrock.com', 'mail.google.com/mail/u/0/?shva=1#inbox'],
                    "write": ['evernote.com', 'writingexercises.co.uk/index.php']}

# Welcome & opening default pages
print('Привет, Алеля <3 \nOpening key productivity pages....')
for site in range(len(activity_options["DEFAULT"])):
    webbrowser.open('https://' + activity_options["DEFAULT"][site])

# Input validation block
while choice not in activity_options:
    print("You can select something to do from the following options:")
    for key in activity_options:
        if key == 'DEFAULT':
            continue
        print(key + " | ", end='')
    choice = str(input("\nWhat do you want to do? "))

# Opening pages relevant to specified desired activity
for site in range(len(activity_options[choice])):
        webbrowser.open('https://'+ activity_options[choice][site])
