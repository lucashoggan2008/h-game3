import random
class Server:
    def __init__(self, name, ip, hackLvl, nodes):
        self.setDefaultVars()
        self.name = name
        self.ip = ip
        self.nodes = nodes
        self.hackLvl = hackLvl
    
    def setDefaultVars(self):
        self.working = True
        self.online = False
        self.moneyMulti = 1
        self.hackLvlMulti = 0.1
        self.root = False
        

   


    def enter(self):
        if self.working and self.root:
            self.online = True
        return self.online
    def exit(self):
        self.online = False
        return not self.online

    def gainRoot(self, hackLvl):
        if hackLvl >= self.hackLvl:
            self.root = True
        return self.root

    def stealMoney(self, hackLvl):
        if self.root and self.working and self.online:
            return (self.moneyMulti * random.random()) ** hackLvl
    
    def stealSkill(self, hackLvl):
        if self.root and self.working and self.online:
            return (self.hackLvlMulti * random.random()) ** hackLvl

    def stealNodeMoney(self, port, hackLvl):
        if self.root and self.working and self.online:
            for x in self.nodes:
                if x.port == port:
                    return x.stealMoney(hackLvl)

    def stealNodeSkill(self, port, hackLvl):
        if self.root and self.working and self.online:
            for x in self.nodes:
                if x.port == port:
                    return x.stealSkill(hackLvl)


class Node:
    def __init__(self, name, port, hackLvl):
        self.name = name
        self.port = port
        self.hackLvl = hackLvl

    def setDefaultVars(self):
        self.hacked = False
        self.moneyMulti = 5
    

    def stealMoney(self, hackLvl):
        if hackLvl >= self.hackLvl and not self.hacked:
            self.hacked = True
            return (self.moneyMulti * random.random() * 2) ** self.hackLvl

    def stealSkill(self, hackLvl):
        if hackLvl >= self.hackLvl and not self.hacked:
            self.hacked = True
            return (hackLvl * random.random()) ** self.hackLvl

    
class Servers:       
    def __init__(self, servers):
        self.servers = servers

    def findServerByIP(self, ip):
        for x in self.servers:
            if x.ip == ip:
                return x

    def gainServerRoot(self, ip, hackLvl):
        try:
            index = self.servers.index(self.findServerByIP(ip=ip))
        except ValueError:
            return False
        return self.servers[index].gainRoot(hackLvl)
    
    def exitServers(self):
        for x in self.servers:
            x.exit()

    def enterServer(self, ip):
        try:
            index = self.servers.index(self.findServerByIP(ip=ip))
        except ValueError:
            return False
        self.exitServers()
        return self.servers[index].enter()
    
    def stealNodeMoney(self, ip, port, hackLvl):
        try:
            index = self.servers.index(self.findServerByIP(ip=ip))
        except ValueError:
            return False
        return self.servers[index].stealNodeMoney(port=port, hackLvl=hackLvl)
    
    def stealNodeSkill(self, ip, port, hackLvl):
        try:
            index = self.servers.index(self.findServerByIP(ip=ip))
        except ValueError:
            return False
        return self.servers[index].stealNodeSkill(port=port, hackLvl=hackLvl)

    def getNodes(self, ip):
        try:
            index = self.servers.index(self.findServerByIP(ip=ip))
        except ValueError:
            return False
        return self.servers[index].nodes

    def stealServerMoney(self, ip, hackLvl):
        try:
            index = self.servers.index(self.findServerByIP(ip=ip))
        except ValueError:
            return False
        return self.servers[index].stealMoney(hackLvl)

    def stealServerSkill(self, ip, hackLvl):
        try:
            index = self.servers.index(self.findServerByIP(ip=ip))
        except ValueError:
            return False
        return self.servers[index].stealSkill(hackLvl)
        
    
        
        


    