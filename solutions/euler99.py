from math import log

def process_data():
    f = open("base_exp.txt", "r")
    data = f.read()
    data = data.replace("\r","")
    data = data.split("\n")
    data = [i.split(",") for i in data]
    return data


def main():
    highest = 0
    index = 0
    for i,n in enumerate(process_data):
        ans = int(n[1]) * log(int(n[0]))
        if ans > highest:
            highest = ans
            index = i
    print index + 1


if __name__ == '__main__':
    main()