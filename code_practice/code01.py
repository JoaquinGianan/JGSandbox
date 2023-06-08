# importing libraries to check the performance of the code.

# import cProfile
# import pstats


def pasar_a_romanos_01(numero):
    """ converting integers into roman numerals. Version 1."""
    numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romanos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    resultado = ""
    for i in range(len(numeros)):
        while numero >= numeros[i]:
            resultado += romanos[i]
            numero -= numeros[i]
    return resultado

ejemplo = 2721




def otra_de_romanos(numero):
    """ Conversion of integers into roman numerals. Version 2."""
    num = int(numero)
    rom = ""
    if num > 3999 or num < 1:
        return "Number must be an integer between 1 and 3999."
    mil = num // 1000
    cen  = (num - mil * 1000) // 100
    dec  = (num - mil * 1000 - cen * 100) // 10
    dig = (num - mil * 1000 - cen * 100 - dec * 10)
    if mil > 0:
        rom += "M" * mil
    if cen > 0:
        if cen == 9:
            rom += "CM"
        elif cen > 5:
            rom += "D" + "C" * (cen - 5)
        elif cen == 5:
            rom += "D"
        elif cen == 4:
            rom += "CD"
        else:
            rom += "C" * cen
    if dec > 0:
        if dec == 9:
            rom += "XC"
        elif dec > 5:
            rom += "L" + "X" * (dec - 5)
        elif dec == 5:
            rom += "L"
        elif dec == 4:
            rom += "XL"
        else:
            rom += "X" * dec
    if dig > 0:
        if dig == 9:
            rom += "IX"
        elif dig > 5:
            rom += "V" + "I" * (dig - 5)
        elif dig == 5:
            rom += "V"
        elif dig == 4:
            rom += "IV"
        else:
            rom += "I" * dig
    return rom



      

def otra_de_romanos_02(numero):
    """Another version of conversion of integers into roman numerals."""
    # create an array that contains the roman numerals for each digit
    r_n = [["", "M", "MM", "MMM", "", "", "", "", "", ""], ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]]
    num = int(numero)
    rom = ""
    if num > 3999 or num < 1:
        return "Number must be an integer between 1 and 3999."
    mil = num // 1000
    cen  = (num - mil * 1000) // 100
    dec  = (num - mil * 1000 - cen * 100) // 10
    dig = (num - mil * 1000 - cen * 100 - dec * 10)
    result = r_n[0][mil] + r_n[1][cen] + r_n[2][dec] + r_n[3][dig]
    return result
   
                                                                                                                                                                                              

    
# r_n = [["", "M", "MM", "MMM", "", "", "", "", "", ""], ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]]
# d_s = [[0,1,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,1]]
# # create a variable that will hold the result
# result = r_n[0][2] + r_n[1][3]
# print(result)

import timeit

# print(timeit.timeit('pasar_a_romanos_01(ejemplo)', number=10000, globals=globals()))
# print(timeit.timeit('otra_de_romanos(ejemplo)', number=10000, globals=globals()))
# print(timeit.timeit('otra_de_romanos_02(ejemplo)', number=10000, globals=globals()))













if __name__ == '__main__':
    print(pasar_a_romanos_01(ejemplo))
    print(otra_de_romanos(ejemplo))
    print(otra_de_romanos_02(ejemplo))   
    print(timeit.timeit('pasar_a_romanos_01(ejemplo)', number=10000, globals=globals()))
    print(timeit.timeit('otra_de_romanos(ejemplo)', number=10000, globals=globals()))
    print(timeit.timeit('otra_de_romanos_02(ejemplo)', number=10000, globals=globals()))