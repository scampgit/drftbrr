#!/usr/bin/python3

import subprocess

import requests
import datetime
from time import sleep

tkn = 'put herr tokEn'

class BotHndlr:

    def __init__(self, tkn):
        self.tkn = tkn
        self.api_url = "https://api.telegram.org/bot{}/".format(tkn)
#cntcts = {'byr':'409691240', 'scmp':'78413176'}
        
    def g_upd(self, offset=None, timeout=30):
        method = 'getUpdates'
        prms = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, prms)
    #print('from upd: ', resp)
        result_jsn = resp.json()['result']
        return result_jsn
    
    def send_msg(self, chat_id, text):
        prms = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
    # print('send 2 chateg: ', chat)
        resp = requests.post(self.api_url + method, prms)
        return resp

    def g_last_upd(self):
        g_result = self.g_upd()

        if len(g_result) > 0:
            last_upd = g_result[-1]
        else:
            last_upd = g_result[len(g_result)]

        return last_upd


greet_bot = BotHndlr(tkn)
greetings = ('heel', 'hi', 'greetings', 'sup', 'cYa!')
cmds = ('ls', 'ps', 'uname', 'df')
gud_user = ('X', 'Y')
usul_user = ('Z', us_name)
now = datetime.datetime.now()

def main():
    new_offset = None
    today = now.day
    hour = now.hour

    while True:
        greet_bot.g_upd(new_offset)

        last_upd = greet_bot.g_last_upd()

        last_upd_id = last_upd['update_id']
        last_chat_text = last_upd['message']['text']
        last_chat_id = last_upd['message']['chat']['id']
        last_chat_name = last_upd['message']['chat']['first_name']

        if last_chat_text.lower() in greetings and today == now.day and 6 <= hour < 12:
            greet_bot.send_msg(last_chat_id, 'Good Mrng {}'.format(last_chat_name))
            today += 1
            new_offset = last_upd_id +1
            continue

        elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour  < 17:
            greet_bot.send_msg(last_chat_id, 'Good Aftrnoon {}'.format(last_chat_name))
            today += 1
            new_offset = last_upd_id +1
            continue

        elif last_chat_text.lower() in greetings and today == now.day and 17 <= hour < 23:
            greet_bot.send_msg(last_chat_id, 'Good evnning {}'.format(last_chat_name))
            today += 1
            new_offset = last_upd_id +1
            continue
        
        if last_chat_text.lower() in cmds and last_chat_name.lower() in gud_user:
            #print('okay!')
            frm_sys = subprocess.getoutput('pwd')
            full_msg = 'okay! \n it is there now: \n\n' + frm_sys
            #greet_bot.send_msg(last_chat_id, 'okay! \n it is there now: \n\n'.format(last_chat_name))
            greet_bot.send_msg(last_chat_id, full_msg.format(last_chat_name))
            new_offset = last_upd_id +1
            continue

        elif last_chat_text.lower() in cmds and last_chat_name.lower() in usul_user:
            #print('sorrrrrryan')
            greet_bot.send_msg(last_chat_id, 'sorrrrryan4eg.. {}'.format(last_chat_name))
            new_offset = last_upd_id +1
            continue
        
        elif last_chat_text.lower() == 'bb':
            break

        else:
            #print('just bb')
            greet_bot.send_msg(last_chat_id, 'like miiiisunderstandng... {}'.format(last_chat_name))
            new_offset = last_upd_id +1
            continue

        #new_offset = last_upd_id +1

    greet_bot.send_msg(last_chat_id, 'me out, bb {}'.format(last_chat_name))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()


