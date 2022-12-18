
# Converting binary to string
# Using BinarytoDecimal(binary)+chr()
# Defining BinarytoDecimal() function
def BinaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Binary to String Converter")
    parser.add_argument("-d", "--decode", help="Decode binary data to string")
    args = parser.parse_args()
    # Driver's code
    # initializing binary data
    bin_data = args.decode
    # print binary data
    print("The binary value is:", bin_data)
    # initializing a empty string for
    # storing the string data
    str_data = " "
    # slicing the input and converting it
    # in decimal and then converting it in string
    for i in range(0, len(bin_data), 7):
        # slicing the bin_data from index range [0, 6]
        # and storing it as integer in temp_data
        temp_data = int(bin_data[i : i + 7])
        # passing temp_data in BinarytoDecimal() function
        # to get decimal value of corresponding temp_data
        decimal_data = BinaryToDecimal(temp_data)
        # Decoding the decimal value returned by
        # BinarytoDecimal() function, using chr()
        # function which return the string corresponding
        # character for given ASCII value, and store it
        # in str_data
        str_data = str_data + chr(decimal_data)
    # printing the result
    print("The Binary value after string conversion is:", str_data)
