# For converting ASCII into string

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Converting ASCII to string")
    parser.add_argument("-d", "--decode", help="Add ASCII chars to decode")
    args = parser.parse_args()
    ascii = args.decode
    # ascii = """114 114 114 111 99 107 110 114 110 48 49 49 51 114
    # """

    for c in ascii.split():
        print(chr(int(c)), end='')
