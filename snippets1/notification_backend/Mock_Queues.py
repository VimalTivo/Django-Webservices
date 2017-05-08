import pika
import datetime
import time
from snippets1.notification_backend.formats import format1,headers_update,ids,source
from xml.dom import minidom
import random

class Handle_Connection:
    def __init__(self):
        self.credentials=pika.PlainCredentials('guest','guest')
        self.parameters = pika.ConnectionParameters('procsrv-mq-test-1100.zreem.com',55672, '/', self.credentials, socket_timeout=10000)
        self.connection = None

    def Connect(self):
        self.connection = pika.BlockingConnection(self.parameters)

    def channel(self):
        return self.connection.channel()

    def set_properties(self,id):
        delivery_mode=1
        content_type='text/plain; charset=utf-8'
        headers_update['Publication-Id']=str(random.randint(0,pow(10,6)))
        message_id=headers_update['Publication-Id']
        headers_update['Resource-Id']=id
        p = pika.BasicProperties(delivery_mode=delivery_mode,content_type=content_type,message_id=message_id,headers=headers_update)
        # return pika.BasicProperties(delivery_mode=delivery_mode,content_type=content_type,message_id=message_id,headers=headers_update)
        return p

    def Publish_Message(self,body,id):
        try:
            result=self.channel().basic_publish(exchange='Write-to-listnerqueue',routing_key='WTL',body=body,properties=self.set_properties(id))
            print(result)
            return result
        except Exception as e:
            print(e)
            print("False")
            return False

    def Disconnect(self):
        self.connection.close()

class Prepare_Test_Data:

    def get_time(self):
        c_time=datetime.datetime.isoformat(datetime.datetime.fromtimestamp(time.time()+15))
        e_time=datetime.datetime.isoformat(datetime.datetime.fromtimestamp(time.time()+30))
        airdatetime=c_time.split('.')[0]+'Z'
        endairdatetime=e_time.split('.')[0]+'Z'
        return [airdatetime,endairdatetime]

    def set_xmldata(self,id):
        xmldoc = minidom.parseString(format1)
        xmldoc.getElementsByTagName('id')[0].firstChild.data=id# id
        xmldoc.getElementsByTagName('r_airing')[0].firstChild.data=id#r_airing
        c = xmldoc.getElementsByTagName('source')[0].childNodes
        c[0].firstChild.nodeValue=source[str(id)][0]# sourceid
        c[1].firstChild.nodeValue=source[str(id)][1]# r_source
        c[2].firstChild.nodeValue=source[str(id)][2]# name
        t=self.get_time()
        xmldoc.getElementsByTagName('AirDateTime')[0].firstChild.data=t[0]
        xmldoc.getElementsByTagName('EndAirDateTime')[0].firstChild.data=t[1]
        return xmldoc.toxml()

def post_request():
    h = Handle_Connection()
    print('here1')
    h.Connect()
    p = Prepare_Test_Data()
    print('here2')
    id1=random.choice(ids)
    print('here3')
    success = h.Publish_Message(p.set_xmldata(id1),id1)
    print('here4')
    h.Disconnect()
    return success