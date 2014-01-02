def minimal(n):
    numerals = (("M",1000),("CM",900),("D",500),("CD",400),("C",100),
                ("XC",90),("L",50),("XL",40),("X",10),("IX",9),("V",5),("IV",4),("I",1))
    answer = ""      
    for numeral, value in numerals:
        while n/value > 0:
            n -= value
            answer += numeral
    return answer


def convert(num):
    numerals = (('IV', "4"), ('IX', "9"), ('XL', "40"), ('XC', "90"), ('CD', "400"),('CM', "900"), 
                ('I', "1"), ('V', "5"), ('X', "10"), ('L', "50"), ('C', "100"), ('D', "500"), ('M', "1000"))
    for numeral, value in numerals:
        num = num.replace(numeral,value + ",")
    num = num[:-1]
    return sum(int(i) for i in num.split(","))

def main():
    f = open("roman.txt","r")
    data = f.read().split("\r\n")
    print sum(len(d) - len(minimal(convert(d))) for d in data)


if __name__ == '__main__':
    main()