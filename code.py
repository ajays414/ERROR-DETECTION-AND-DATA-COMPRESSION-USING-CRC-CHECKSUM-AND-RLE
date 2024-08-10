def crc_error_correction(bits, divisor):
    dividend = bits + "0" * (len(divisor) - 1)  # Append zeros for division

    # Perform CRC division
    for i in range(len(dividend) - len(divisor) + 1):
        if dividend[i] == "1":
            for j in range(len(divisor)):
                dividend = dividend[:i+j] + str(int(dividend[i+j]) ^ int(divisor[j])) + dividend[i+j+1:]

    # Extract error correction bits
    error_correction = dividend[-(len(divisor)-1):]
    corrected_crc = bits[:-(len(error_correction))] + error_correction
    return corrected_crc

def calculate_checksum(bits):
    checksum = 0
    for bit in bits:
        checksum += int(bit)
        checksum = checksum & 1  # Perform 1-bit addition using bitwise AND
    corrected_checksum = bits[:-1] + str(int(bits[-1]) ^ 1)
    return corrected_checksum

def run_length_encode(data):
    encoded_data = ""
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i-1]:
            count += 1
        else:
            encoded_data += str(count) + data[i-1]
            count = 1
    encoded_data += str(count) + data[-1]
    return encoded_data
def run_length_encode(data):
    encoded_data = ""
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i-1]:
            count += 1
        else:
            encoded_data += str(count) + data[i-1]
            count = 1
    encoded_data += str(count) + data[-1]
    return encoded_data

def run_length_decode(data):
    decoded_data = ""
    i = 0
    while i < len(data):
        count = int(data[i])
        symbol = data[i+1]
        decoded_data += symbol * count
        i += 2
    return decoded_data

# Get input from the user
bits = input("Enter the bit sequence: ")
divisor = input("Enter the divisor for CRC: ")

# Calculate the chunk size
n = len(bits) // 2
# Split the message into two separate bit sequences
first_sequence = bits[:n]
second_sequence = bits[n:]

# Perform CRC error correction on the first sequence
corrected_crc = crc_error_correction(first_sequence, divisor)

# Calculate the checksum on the second sequence
checksum = calculate_checksum(second_sequence)

# Correct the overall bits
corrected_bits = corrected_crc + checksum

# Apply RLE compression to the corrected bits
compressed_data = run_length_encode(corrected_bits)

# Decompress the compressed data using RLE
decompressed_data = run_length_decode(compressed_data)

# Print the results
print("Corrected CRC:", corrected_crc)
print("Corrected Checksum:", checksum)
print("Overall Corrected Bits:", corrected_bits)
print("Compressed Data:", compressed_data)
print("Decompressed Data:", decompressed_data)
