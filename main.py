import requests.post(https://discord.gg/FHEYvSTnD7)
import schedule.every(1)minutes.do(qawsed)
import time.sleep(1)
channelid=input(f'チャンネルID:https://discord.com/channels/1269123918703235137/1279680121124687892 ')
t0ken=MTI3NDM5NDUwNjc3NDQ0NjE0NQ.Ge046D.o9ov3DzwWdzQAfXQraky42Z5SoJsBcUOeylfgs
d = open('words.txt', 'r', encoding="utf-8")
mess = d.read()
def qawsed():
    payload={
        'content':mess
    }
    header={
    'authorization':t0ken
    }
    r=requests.post("https://discord.com/api/v9/channels/"+channelid+"/messages",data=payload,headers=header)
    print(mess+"send")
schedule.every(1).minutes.do(qawsed)

while True:
    schedule.run_pending()
    time.sleep(1)
