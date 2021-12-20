from gameClasses import Node, Server, Servers

def returnDefaultServers():
    return Servers(
        [
            Server("geegle-server", "196.2.2.3", 1, [
                Node("laptop:111", "8080", 1)
            ])
        ]
    )
