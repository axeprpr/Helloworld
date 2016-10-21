#coding:utf-8  
from pyftpdlib.authorizers import DummyAuthorizer  
from pyftpdlib.handlers import FTPHandler  
from pyftpdlib.servers import FTPServer  
import os
#新建一个用户组  
authorizer = DummyAuthorizer()  
authorizer.add_anonymous(os.path.abspath('.'))  
handler = FTPHandler  
handler.authorizer = authorizer  
#开启服务器  
server = FTPServer(("127.0.0.1", 21), handler)  
server.serve_forever()  
