# This will initilise the packet protocol structure and handle imports
# IMPORT ALL PROTOCOLS

"""
-----------------------------------------------------------------
|Packet ID   | Description                          | Direction |
-----------------------------------------------------------------
|00          | Network connection and handshake     | Send/Recv |
|01          | Profile management                   | Send/Recv |
|02          | Loggin in                            | Send/Recv |
|03          | Account Setup                        | Send/Recv |
|xx          |                                      |           |
|09          | General Error handeling and reporting| Send/Recv |
|------------|--------------------------------------|-----------|
|10          | World Chunks                         | Send/Recv |
|11          | Code samples                         | Send/Recv |
|12          | Chunk update Send                    | Send/     |
|13          | Chunk Error handeling                | Send/Recv |
|---------------------------------------------------|-----------|
|20          | IDE data settings ect.               | Send/     |
-----------------------------------------------------------------
"""



# Function peramiter order. (User Class, Packet Data, LoggerFunction, SettingsFunction)
def none_function(user, data, log, settings):
    return None


packet_functions = {
     0:none_function,
     1:none_function,
     2:none_function,
     3:none_function,
     9:none_function,

    10:none_function,
    11:none_function,
    12:none_function,
    13:none_function,

    20:none_function,
}