import sys


def main():
    # print(sys.argv[1])
    # start = "local/study-files/nmdc-sty-11-34xj1150.yaml"
    start = sys.argv[1]
    next1 = start.split('/')[-1]
    next2 = next1.split('.')[0]
    result = next2.replace('-', ':', 1)
    print(result, end='')


if __name__ == "__main__":
    main()
