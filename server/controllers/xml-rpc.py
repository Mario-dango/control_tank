from xmlrpc.server import SimpleXMLRPCServer
from .robot import Robot

class XmlRpcServer:
    def __init__(self, robot: Robot):
        self.robot = robot
        self.server = None
    
    def start_server(self):
        self.server = SimpleXMLRPCServer(('localhost', 8000))
        self.server.register_instance(self.robot)
        self.server.serve_forever()
