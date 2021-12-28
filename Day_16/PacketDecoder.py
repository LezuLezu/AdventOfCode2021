from io import StringIO
from math import prod

packetSum = 0

def getData(path):      #parse data
    data = "".join(
        [
        bin(int(x, 16))[2:].zfill(4)        # fill leading zeros
        for x in open(path).read().strip()
        ]
    )
    return data

def procesPackets(bits):
    global packetSum
    byte = bits.read(3)     # get byte from bits (input)
    # print(byte)
    packetSum += int(byte, 2)       # add decimal number of byte to packet sum
    # print(int(byte, 2))
    packetTypeID = bits.read(3)         # get packet id from bits
    # print(packetID)

    if packetTypeID == "100":   # type id 4 -> literal values of packets
            chunks = []
            group = ""
            while group != "0":         # go trough leading zeros
                group = bits.read(1)    # get first bit of packet to see if 0    
                # print(group)
                chunks.append(bits.read(4))     # add packet of 4 bits to chunks to calculate value
                # print(chunks)
            return int("".join(chunks), 2)      # return value of packets

    packets = []                        
    if bits.read(1) == "0":                 # lenght type ID 0 -> next 15 bits represent total lenght of bits
        length = int(bits.read(15), 2)      # calculate decimal number of first 15 bits to find total lenght
        target_length = bits.tell() + length    # target lenght is the amount of bits in input + the calculated lenght
        while bits.tell() != target_length:     # while the lengt of input is not equal to target keep appending packets
            packets.append(procesPackets(bits))
    else:                                   # lengt type ID 1 -> next 11 bits amount of subpackets in packet
        num_packets = int(bits.read(11), 2)     # calculate decimal number of first 11 bits to find amount of subpackets
        for _ in range(num_packets):            
            packets.append(procesPackets(bits))     # add subpackets to bits

    if packetTypeID == "000":   # type id 0 -> sum of packet
        return sum(packets)
        
    if packetTypeID == "001":   # type id 1 -> product of packet
        return prod(packets)

    if packetTypeID == "010":   # type id 2 -> minimun value of packet
         return min(packets)

    if packetTypeID == "011":   # type id 3 -> maximum value of packet
        return max(packets)
   
    if packetTypeID == "101":    # type id 5 -> greater than next packet 
        return int(packets[0] > packets[1])

    if packetTypeID == "110":   # type id 5 -> smaller than next packet
        return int(packets[0] < packets[1])

    if packetTypeID == "111":   # type id 6 -> equal to next packet
        return int(packets[0] == packets[1])

if __name__ == '__main__':

    data = getData("Day_16/data.txt") 
    expression = procesPackets(StringIO(data))

    print("Part one, packet sum:\t\t\t\t\t %s" %(packetSum))
    print("Part two, expression from hexadecimal encoded bits:\t %s" %(expression))

