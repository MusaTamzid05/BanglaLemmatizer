from bn_pos.pos import POS

def main():

    pos = POS()

    while True:
        print(pos.get_pos_of(input(">> ")))


if __name__ == "__main__":
    main()
