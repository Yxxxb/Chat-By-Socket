# -*- coding:utf-8 -*-
"""
Author :Yxxxb & Xubing Ye
Number :1953348
Date   :2021/10/05
File   :Server.py
"""

import socket


class UdpServer(object):
    def AppendList(self, array, value):
        if value not in array:
            array.append(value)
        return array

    def UdpServer(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('', 9527))  # 绑定同一个域名下的所有机器
        PortList = []

        while True:
            revcData, (remoteHost, remotePort) = sock.recvfrom(1024)
            print("[%s:%s] connect" % (remoteHost, remotePort))  # 接收客户端的ip, port

            revcData = revcData.decode('utf_8')
            ChatTarget = 0
            if revcData[0] != 'c':
                ChatTarget = int(revcData[0])

            PortList = self.AppendList(PortList, remotePort)
            print(remoteHost, PortList[ChatTarget - 1])
            print(remoteHost, remotePort)
            sendDataLen2 = sock.sendto(revcData.encode(), (remoteHost, PortList[ChatTarget - 1]))
            print("PortList : ", PortList)
            print("revcData : ", revcData)
            print("sendDataLen2 : ", sendDataLen2, '\n')

        # sock.close()


if __name__ == "__main__":
    udpServer = UdpServer()
    udpServer.UdpServer()
