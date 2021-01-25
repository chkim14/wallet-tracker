from optparse import OptionParser


def track_wallets(filepath):
    print(filepath)

if __name__ == '__main__':
    parser = OptionParser("This is a simple script to track ETH wallets")
    parser.add_option("-t",action="store_true",dest="track",help="Track wallet id's")
    parser.add_option("--filepath", action="store",type="string",dest="filepath")

    (options,args) = parser.parse_args()

    if options.track:
        track_wallets(options.filepath)
