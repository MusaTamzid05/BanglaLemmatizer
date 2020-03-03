from bn_processor.lemmatizer import BanglaLemmatizer

def main():

    lem = BanglaLemmatizer()

    while True:
        print(lem.lemmatize(input(">>")))



if __name__ == "__main__":
    main()
