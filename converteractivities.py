import numpy as np

text2intConverter = {
    "zero":     0,
    "one":      1,
    "two":      2,
    "three":    3,
    "four":     4,
    "five":     5,
    "six":      6,
    "seven":    7,
    "eight":    8,
    "nine":     9,
    "ten":      10,
    "eleven":   11,
    "twelve":   12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen":  15,
    "sixteen":  16,
    "seventeen": 17,
    "eighteen":  18,
    "nineteen":  19,
    "twenty":   20,
    "thirty":   30,
    "forty":   40,
    "fifty":    50,
    "sixty":    60,
    "seventy":  70,
    "eighty":   80,
    "ninety":   90,
    "one hundred": 100
}

def converter_func(d: dict, s: str):
    if s == "one hundred":
        return 100
    slist = s.split()
    summation = []
    for w in slist:
        if w in d:
            num = d[w]
            summation.append(num)
        else:
            print(w, "is not part of the dictionary")

    returnvalue = sum(summation)
    return returnvalue



if __name__ == '__main__':
    gradeslist = (
    [90, 60, "one", "twenty three", "ninety nine", "one hundred"],
    ["forty seven", "sixty eight", "eighty two", "seventy seven", "zero", 1, "three"],
    ["thirty nine", "eleven", "twelve", "thirteen", "nineteen", "one hundred", 99],
    ["fifty five", 33, "twenty", 0, "seventy one", "seventy", "ninety", 44, 99, 27]
    )
    
    
    m = 1
    for grade in gradeslist:

        h = list(enumerate(grade)) # enumerate returns a tuple of (index, element)

        for i in range(len(h)):
            if isinstance(h[i][1], str) == True:
                grade[i] = (converter_func(text2intConverter, h[i][1]))
        print("This is grade", m)
        grade.sort
        print(grade)
        grade.sort(reverse = True)
        print(grade)
        grade.pop(len(grade)-1)
        print(grade)
        average = np.mean(grade)
        if average >= 60.00:
            print("The average is:",average,"PASSED\n")
        else:
            print("The average is:",average,"FAILED\n")

        m +=1

    