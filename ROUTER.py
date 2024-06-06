import random

ServerResponseArray = [] 
ServerData = ["scratchcat", "apple", "kojiwolf", "koji", "loki", "lemon", "lemons", "lemonade", "pillow", "blanket", "basket", "lemon cream", "socket", "lemon juice", "orange", "orange juice"]

def socket_request(*args):
    global ServerResponseArray
    x = random.randint(100000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999)
    ServerResponseArray = []
    
    for index in args:
        if isinstance(index, int) and 0 <= index < len(ServerData):
            ServerResponseArray.append(ServerData[index])
    
    resp = ",".join(ServerResponseArray)
    fstring = f"{{({resp}),(SOCKET:1,SOCKET-REQUEST-ID:0x{x})}}"
    return fstring


def socket_index(input):
    x = random.randint(100000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999)
    resp = ServerData.index(input)
    fstring = f"{{{{{resp}}},(SOCKET:1,SOCKET-REQUEST-ID:0x{x})}}"
    return fstring 