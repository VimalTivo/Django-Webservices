import time
from urllib.parse import quote, urlencode
import hashlib
import hmac
import base64
from snippets1.models import Snippet,Key_Secret
from django.core.exceptions import ObjectDoesNotExist
import re

Encode_dict = {',':'%2C','*':'%2A'}

class Oauth:

    def __init__(self,auth_headers,request_type,uri,parameters_string):
        self.h={}
        self.request_type=request_type
        self.uri = uri
        self.parameters_string=parameters_string
        for x in auth_headers.split(','):
            self.h[x.split('=')[0].strip()]=eval(x.split('=')[1])
        print("h",self.h)
        for k,v in self.h.items():
            if re.search('OAuth (.+)',k)!=None:
               self.h[re.search('OAuth (.+)',k).group(1)]=self.h[k]
               del self.h[k]
        #self.h['oauth_version']=self.h['OAuth oauth_version']
        #del self.h['OAuth oauth_version']

    def checktimestamp(self):
        if int(self.h['oauth_timestamp'])>int(time.time())+300:
            return False
        return True

    def checkconsumerkey(self):
        try:
            Key_Secret.objects.get(key=self.h['oauth_consumer_key'])
        except ObjectDoesNotExist:
                return False
        return True

    def checknonce(self):
        return True

    def first_chunk(self):
        return self.request_type

    def second_chunk(self):
        # print("second",quote('https://example.com/eloqua/action/create',safe=''))
        # return quote('https://example.com/eloqua/action/create',safe='')
        # print("second",quote('http://pre-cloud.rovicorp.com/data/2/2.4/lookup/airing/1548151083/synopses',safe=''))
        # return quote('http://pre-cloud.rovicorp.com/data/2/2.4/lookup/airing/1548151083/synopses',safe='')
        print("second_chunk",quote(self.uri,safe=''))
        return quote(self.uri,safe='')

    def third_chunk(self):
        # payload={'param1':'value1','param2':'value2','oauth_consumer_key':self.h['oauth_consumer_key'],'oauth_nonce':self.h['oauth_nonce'],'oauth_signature_method':self.h['oauth_signature_method'],'oauth_timestamp':self.h['oauth_timestamp'],'oauth_version':self.h['oauth_version']}
        # payload={'param1':'value1','param2':'value2','oauth_consumer_key':'test_client_id','oauth_nonce':1234567,'oauth_signature_method':'HMAC-SHA1','oauth_timestamp':1427308921,'oauth_version':1.0}
        payload={}
        for x in self.parameters_string.split('&'):
            payload[x.split('=')[0]]=self.Encode_SpecialChar_parameters(x.split('=')[1])
        for k,v in self.h.items():
            if k!='oauth_signature':
                payload[k]=v
        # payload={'in':'en-US%2Cen-%2A%2C%2A','oauth_consumer_key':'bdfc90661af492da88c5f606ac996262eff55ab3fb5990c542b69bfb23df66ea','oauth_nonce':81029248330733655571491318588,'oauth_signature_method':'HMAC-SHA1','oauth_timestamp':1491318588,'oauth_version':1.0}
        # payload={'param1':'value1','param2':'value2','oauth_consumer_key':'test_client_id','oauth_nonce':18198539448896772361491285593,'oauth_signature_method':'HMAC-SHA1','oauth_timestamp':1491285593,'oauth_version':1.0}
        third = ''
        print("payload:",payload)
        for key in sorted(payload.keys()):
            # if type(payload[key])==list:
            #     for v in payload[key]:
            #         third += key+'='+str(v)+'&'
            third += key+'='+str(payload[key])+'&'
        print("third:",third)
        return quote(third[:len(third)-1],safe='')

    def Encode_SpecialChar_parameters(self,st_value):
        for c in st_value:
            if (c in Encode_dict)==True:
                st_value=st_value.replace(c,Encode_dict[c])
        return st_value

    def Hash_Message(self):
        print('Message',self.first_chunk()+'&'+self.second_chunk()+'&'+self.third_chunk())
        return self.first_chunk()+'&'+self.second_chunk()+'&'+self.third_chunk()

    def Hash_Key(self):
        print("Hash_Key:",Key_Secret.objects.filter(key=self.h['oauth_consumer_key']).values('secret')[0]['secret']+'&')
        return Key_Secret.objects.filter(key=self.h['oauth_consumer_key']).values('secret')[0]['secret']+'&'
        # return '748ece20ad81aea37dfc868b39f6bd1b5d244b33c75435364ab300a7d419cc5a&'
        # return 'test_client_secret&'

    def make_digest(self,message,key):
        key = bytes(key, 'UTF-8')
        message = bytes(message, 'UTF-8')

        digester = hmac.new(key, message, hashlib.sha1)
        # signature1 = digester.hexdigest()
        signature1 = digester.digest()
        print(signature1)

        # signature2 = base64.urlsafe_b64encode(bytes(signature1, 'UTF-8'))
        signature2 = base64.urlsafe_b64encode(signature1)
        print(signature2)
        print(quote(str(signature2, 'UTF-8'),safe=''))
        return quote(str(signature2, 'UTF-8'),safe='')
        # return str(signature2, 'UTF-8')

    def optimize_signature(self,signature):
        return (signature.replace('_','%2F').replace('-','%2B'))==self.h['oauth_signature']
        # return signature
