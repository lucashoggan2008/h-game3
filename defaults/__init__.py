from gameClasses import Node, Server, Servers

def returnDefaultServers():
    return Servers(
        [
            Server("geegle-server", "240.703.553.376", 8, [
                Node("phone:603", "1475", 11),
                Node("phone:783", "1152", 13),
                Node("phone:788", "1365", 9),
                Node("pc:257", "1943", 9),
                Node("phone:265", "1528", 8),
            ]),
            Server("gitdock-server", "309.667.367.261", 3, [
                Node("laptop:499", "1740", 3),
                Node("pc:300", "1937", 3),
                Node("phone:318", "1631", 3),
                Node("laptop:593", "1861", 8),
                Node("phone:268", "1225", 4),
            ]),
            Server("notflix-server", "579.321.664.173", 5, [
                Node("laptop:215", "1661", 7),
                Node("pc:582", "1693", 10),
                Node("laptop:140", "1566", 8),
                Node("phone:178", "1456", 5),
                Node("laptop:576", "1151", 6),
            ]),
            Server("johns-sercurity-server", "817.104.927.626", 1,  [
                Node("pc:255", "1784", 3),
                Node("laptop:384", "1706", 1),
                Node("pc:245", "1682", 5),
                Node("laptop:903", "1632", 1),
                Node("phone:651", "1262", 3),
            ]),
            Server("macrohard-server", "193.145.792.236", 7, [
                Node("pc:221", "1463", 7),
                Node("phone:952", "1461", 10),
                Node("laptop:580", "1745", 12),
                Node("phone:645", "1250", 9),
                Node("phone:869", "1377", 8),
            ])
        ]
    )
