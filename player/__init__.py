class Player:
    def __init__(self, name, servers, jobs):
        self.setDefaultVars()
        self.name = name
        self.servers = servers
        self.jobs = jobs    
    def setDefaultVars(self):
        self.money = 0
        self.hackLvl = 1 
        self.curSystemIp = "0.0.0.0"
        self.curSystemPort = None      
    def formatGetServers(self):
        formatedList = []
        for x in self.servers.servers:
            formatedList.append({
                "name":x.name,
                "ip":x.ip,
                "hackLvl":x.hackLvl,
                "working":x.working,
                "root":x.root
            })
        return formatedList  
    def gainServerRoot(self, ip):
        response = self.servers.gainServerRoot(ip, self.hackLvl)
        if response == True:
            self.exitServers()
            self.enterServer(ip)
        return response
    def exitServers(self):
        self.servers.exitServers()
        self.curSystemIp = "0.0.0.0"
        self.curSystemPort = None
    def enterServer(self, ip):
        response = self.servers.enterServer(ip)
        if response:
            self.curSystemIp = ip
        return response
    def stealNodeMoney(self, port):
        return self.servers.stealNodeMoney(self.curSystemIp, port, self.hackLvl)
    def stealNodeSkill(self, port):
        return self.servers.stealNodeSkill(self.curSystemIp, port, self.hackLvl)
    def stealServerSkill(self, ip):
        return self.servers.stealServerSkill(ip, self.hackLvl)
    def stealServerMoney(self, ip):
        return self.servers.stealServerMoney(ip, self.hackLvl)
    def formatGetNodes(self, ip):
        nodes = self.servers.getNodes(ip)
        tempList = []
        for x in nodes:
            tempList.append({
                "name":x.name,
                "port":x.port,
                "hackLvl":x.hackLvl,
                "hacked":x.hacked
            })
        return tempList
