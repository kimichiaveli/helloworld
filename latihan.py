# # SOAL DARI HACKERRANK

# n = int(input("masukkan angka: "));

# while n < 1 or n > 100:
#     n = int(input("masukkan angka: "));

# if (n%2 != 0 or (n >= 6 and n <= 20)):
#     print("weird");
# else:
#     print("not weird");

"""
SOAL DARI ALGOEXPERT
CARI URUTAN ANGKA (EX. 1,2,3,4) TERPANJANG DAN PRINT DERET AWAL DAN DERET AKHIRNYA DALAM BENTUK LIST
CONTOH INPUT : [0,1,2,3,4,5,6,7,10,11,12,15]
OUTPUTNYA : [0,7] >>> KARENA DERET TERPANJANG 0,1,2,3,4,5,6,7 DIMULAI DARI 0 SAMPAI 7
"""

soal = [30, 1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6, 16, 17, 19, 18, 29, 14, 20, 21]

def algo(x):
    for a in range(len(x)): # FOR LOOP UTK SORT, BISA PAKAI BUILT IN FUNCTION .SORT
        for b in range(a + 1, len(x)):
            if x[a] > x[b]:
                temp = x[a];
                x[a] = x[b];
                x[b] = temp;
    batas = [];
    xx = x[:]; # MANIPULASI LIST SUPAYA BISA MEMISAHKAN ANGKA YANG BERDERET
    xx.insert(0, x[0])
    xx.append(x[-1]);

    for a in range(len(x) + 1): # MENCARI INDEX UNTUK PEMISAHAN ANGKA YANG BERDERET
        if xx[a + 1] - xx[a] != 1:
            batas.append(a);
    awal = 0;
    deret = [];

    for j in batas: # PEMISAHAN ANGKA BERDERET DALAM BENTUK LIST
        deret.append(xx[awal+1:j+1]);
        awal = j

    d = {a:len(deret[a]) for a in range(len(deret))}; # MEMBUAT DICTIONARY UNTUK MENCARI DERET MANA YANG TERPANJANG
    max_value = max(d.values());
    max_keys = [];
    for i in d.keys():
        if d[i] == max_value:
            max_keys.append(i);
    
    print(x, ">> ini list angka yang sudah disort");
    print(deret, ">> ini list berisi deret angka dalam bentuk list");
    print(d, "ini dictionary dengan keys index deret dan value panjang deretnya");
    for i in max_keys: # JAWABAN
        print([deret[i][0], deret[i][-1]]);

algo(soal)

"""
Question 6
Level 2

Question:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
"""

# def formula(x):
#     import math
#     c = 50;
#     h = 30;
#     jawaban = "";
#     listx = x.split(",");
#     for d in listx:
#         z = str(round(math.sqrt(2 * c * int(d) / h)));
#         jawaban += z + ",";
#     print(jawaban[:-1]);

# formula("100,150,180");

# def formula1(x):
#     import math
#     c = 50;
#     h = 30;
#     jawaban = [];
#     listx = x.split(",");
#     for d in listx:
#         jawaban.append(str(round(math.sqrt(2 * c * int(d) / h))));
#     print(",".join(jawaban));

# formula1("100,150,180");

"""
Question 7
Level 2

Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

Hints:
Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.
"""

# def pq7(x):
#     listx = x.split(",");
#     listx = list(map(lambda a: int(a), listx));
#     value = [];
#     for rownum in range(listx[0]):
#         value.append([]);
#         for colnum in range(listx[1]):
#             value[rownum].append(rownum * colnum);
#     print(value);

# def pq7alt(x):
#     listx = [int(a) for a in x.split(",")]; # disini pake list comprehension untuk merubah value list awal dari str jadi int
#     value = [[0 for colnum in range(listx[1])] for rownum in range(listx[0])]; # disini pake list comprehension untuk membuat cetakan list yg akan dimasukan value sesuai formula
#     for rownum in range(listx[0]):
#         for colnum in range(listx[1]):
#             value[rownum][colnum] = rownum * colnum;
#     print(value);

# pq7("3,5");
# pq7alt("3,5");

"""
Question 8
Level 2

Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

# def pq8(x):
#     listx = x.split(",");
#     for a in range(len(listx)):
#         for b in range(a + 1, len(listx)):
#             if listx[a] > listx[b]:
#                 temp = listx[a];
#                 listx[a] = listx[b];
#                 listx[b] = temp;
#     print(",".join(listx));

# pq8("without,hello,bag,world");
