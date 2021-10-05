# -*- coding:utf-8 -*-
"""
Author :Yxxxb & Xubing Ye
Number :1953348
Date   :2021/10/05
File   :Client.py
"""

import socket
import threading
import tkinter as tk


class UdpClient(threading.Thread):
    def __init__(self, ClientName):
        threading.Thread.__init__(self, name=ClientName)
        self.clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.clientSock.sendto(str.encode(ClientName + ' Connected'), ('localhost', 9527))
        self.clientSock.recvfrom(1024)

        self.ClientName = ClientName
        self.text = ''
        self.window = ''
        self.EntryTxt = ''
        self.EntryName = ''

    def run(self):
        GetThread = threading.Thread(target=self.UdpClientGet)
        GetThread.setDaemon(True)
        GetThread.start()

        self.window = tk.Tk()
        self.window.title(self.ClientName)
        self.window.geometry('300x300')

        self.text = tk.Text(self.window, height=8)
        self.text.pack()
        self.EntryName = tk.Entry(self.window, show=None)
        self.EntryName.pack()
        self.EntryTxt = tk.Entry(self.window, show=None)
        self.EntryTxt.pack()
        bt = tk.Button(self.window, text='send', command=self.UdpClientSend)
        bt.pack()

        self.window.mainloop()

    def UdpClientSend(self):
        print(self.ClientName)
        sendTar = self.EntryName.get()
        sendStr = self.EntryTxt.get()
        sendDataLen = self.clientSock.sendto(str.encode(sendTar + sendStr), ('localhost', 9527))
        print("sendDataLen: ", sendDataLen)

    def UdpClientGet(self):
        while True:
            print('***')
            recvData = self.clientSock.recvfrom(1024)
            self.text.insert(tk.END, recvData)
            self.text.insert(tk.END, '\n')
            print("recvData: ", recvData)


if __name__ == "__main__":
    threads = []
    for i in range(2):
        clientname = 'c' + str(i + 1)
        t = UdpClient(ClientName=clientname)
        threads.append(t)
    for thr in threads:
        thr.start()
