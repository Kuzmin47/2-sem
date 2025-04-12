class Server:
    __ip_counter = 1 

    def __init__(self):
        self.buffer = []  
        self.ip = Server.__ip_counter
        Server.__ip_counter += 1 
        
    def send_data(self, data):
        self.buffer.append(data)
        
    def get_data(self):
        packets = self.buffer.copy()
        self.buffer.clear()
        return packets

    def get_ip(self):
        return self.ip

class Router:
    def __init__(self):
        self.buffer = []  
        self.servers = {} 

    def link(self, server):
        self.servers[server.get_ip()] = server

    def unlink(self, server):
        if server.get_ip() in self.servers:
            del self.servers[server.get_ip()]

    def send_data(self):
        for data in self.buffer:
            if data.ip in self.servers:
                self.servers[data.ip].buffer.append(data)
        self.buffer.clear()

class Data:
    def __init__(self, data, ip):
        self.data = data 
        self.ip = ip