# Read any file including binarys and return them as a byte string
def read_file(location, chunk=4096):

    # Make new blank byte string
    byte = b""
    # Open file
    with open(location, "rb") as rb:
        # Read block size and cast to bite sting
        block = rb.read(chunk)
        # Reading a b"" means that the end of the file has been reached and the string should be returned
        if block == b"":
            return byte
        else:
            byte += block

# Write binary to the file
def write_file(location, byte):
    with open(location,"wb") as wb:
        wb.write(byte)

def send_file(location, client, protocol=11):
    data = read_file(location)
    packet = {"ID":11, "DATA":data}
    client.send(packet)