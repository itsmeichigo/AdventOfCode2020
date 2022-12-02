from typing import Tuple

def decode_literal_number(binary) -> Tuple[int, int, int]:
    version = int(binary[:3], 2)
    index = 6
    bits = ""
    while index < len(binary):
        bits += binary[index+1:index+5]
        if binary[index] == "0":
            break
        index += 5
    return (version, index + 1, int(bits, 2))

def decode_subpacket(binary) -> Tuple[int, int]:
    print("found subpacket")
    total_versions = int(binary[:3], 2)
    packet_type = int(binary[3:6], 2)
    last_index = 0
    if packet_type != 4:
        if binary[6] == "0":
            total_subpacket_length = int(binary[7:22], 2)
            print(total_subpacket_length)
            current_index = 22
            while current_index < current_index + total_subpacket_length:
                if int(binary[current_index+3:current_index+6], 2) == 4:
                    print("0 - literal: ", binary[current_index:], current_index, total_versions)
                    version, last_index, _ = decode_literal_number(binary[current_index:])
                    print(last_index)
                    total_versions += version
                    current_index += last_index
                else:
                    versions, last_index = decode_subpacket(binary[current_index:])
                    total_versions += versions
                    current_index += last_index
            last_index = current_index + total_subpacket_length
        else:
            immediate_subpackets_count = int(binary[7:18], 2)
            current_index = 18
            subpackets_found = 0
            while subpackets_found < immediate_subpackets_count:
                if int(binary[current_index+3:current_index+6], 2) == 4:
                    print("1 - literal: ", binary[current_index:])
                    version, last_index, _ = decode_literal_number(binary[current_index:])
                    total_versions += version
                    current_index += last_index
                else:
                    versions, last_index = decode_subpacket(binary[current_index:])
                    total_versions += versions
                    current_index += last_index
                subpackets_found += 1
    return total_versions
        
def calculate_total_version(hex) -> int:
    binary = bin(int(hex, 16))[2:]
    print(binary)
    return decode_subpacket(binary)[0]

print(calculate_total_version("8A004A801A8002F478"))