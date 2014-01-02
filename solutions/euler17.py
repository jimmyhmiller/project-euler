#!/usr/bin/env python

def main():
    ones = ["one","two","three","four","five","six","seven","eight","nine"]
    teens = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    tens = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"] 
    hundreds = ["hundred"]
    ands = ["and"]
    thousands = ["thousand"]


    total = 0


    teens_n = sum(1 for x in range(10,1001) if str(x)[-2] == "1" and str(x)[-1] == "1")
    ones_n = sum(1 for x in range(1,1000) if str(x)[-1] == "1") - teens_n + 100
    tens_n = sum(1 for x in range(10,1001) if str(x)[-2] == "2")
    hundreds_n = sum(1 for x in range(100,1000))
    ands_n = sum(1 for x in range(100,1000) if str(x)[1:] != "00")
    thousands_n = 1

    teens_w = sum(len(w) * teens_n for w in teens)
    ones_w = sum(len(w) * ones_n for w in ones)
    tens_n = sum(len(w) * tens_n for w in tens)
    hundreds_w = sum(len(w) * hundreds_n for w in hundreds)
    ands_w = sum(len(w) * ands_n for w in ands)
    thousands_w = sum(len(w) * thousands_n for w in thousands)


    print teens_w + ones_w + tens_n + hundreds_w + ands_w + thousands_w + len("one")



if __name__ == '__main__':
    main()