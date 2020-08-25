# # FIZZ BUZZ

# def fizzbuzz(num):
#     for i in range(1, num+1):
#         number = i;
#         text = ""
#         if i % 3 == 0:
#             number = "";
#             text += "Fizz";
#         if i % 5 == 0:
#             number = "";
#             text += "Buzz";
#         print(str(number) + text);

# fizzbuzz(20);

# def fizzbuzz(num):
#     for i in range(1,num+1):
#         # if (i % 21 == 0):
#         #     print('fizzbuzz');
#         if (i % 7 == 0):
#             print(i, ' ');
#         elif (i % 3 == 0):
#             print(i, ' ');
#         else:
#             print(i, 'fizzbuzz');

# fizzbuzz(22);

# def fizzbuzz(num):
#     for i in range(1,num+1):
#         # if (i % 21 == 0):
#         #     print('fizzbuzz');
#         var = ' ' if (i % 7 == 0) or (i % 3 == 0) else 'fizzbuzz'
#         print(i, var);
#         # else:
#         #     print(i, 'fizzbuzz');

# fizzbuzz(22);

# # ALGORITMA DIUBAH JADI PRINT FIZZBUZZ KELIPATAN 3 OR 7, SELAIN ITU PRINT KOSONG

# def fizzbuzz(num):
#     for i in range(1,num+1):
#         if (i % 7 == 0):
#             print(i, ' ');
#         elif (i % 3 == 0):
#             print(i, ' ');
#         else:
#             print(i, 'fizzbuzz');

# fizzbuzz(22);

# # DIRINGKAS JADI 4 LINE

# def fizzbuzz(num):
#     for i in range(1,num+1):
#         if (i % 7 == 0 or i % 3 == 0):
#             print(i, ' ');
#         else:
#             print(i, 'fizzbuzz');

# fizzbuzz(22);

# # DIRINGKAS JADI 2 LINE

# def fizzbuzz(num):
#     for i in range(1,num+1):
#         var = ' ' if (i % 7 == 0) or (i % 3 == 0) else 'fizzbuzz'
#         print(i, var);

# fizzbuzz(22);

# # FIBONACI (mereturn fungsi didalam fungsi itu sendiri, dengan catatan jika x > 900an akan menghasilkan error "maximum recursion depth exceeded")

# def Fibonacci(x):
#     n = x+1
#     if n<0: 
#         print("Incorrect input") 
#     # First Fibonacci number is 0 
#     elif n==1: 
#         return 0
#     # Second Fibonacci number is 1 
#     elif n==2: 
#         return 1
#     else: 
#         return Fibonacci(x-1)+Fibonacci(x-2);
# print(Fibonacci(6))

# # REVERSE LIST IN PLACE

# listku = [1, 2, 3, 4, 5, 6, 7, 8, 9];
# def rev(x):
#     if type(x) != list:
#         print('salah tipe data');
#     else:
#         jawaban = [];
#         for a in range(len(x)-1, -1, -1):
#             jawaban.append(x[a])
#     return jawaban
# print(rev(listku));

# # REVERSE LIST SETENGAH AJA

# listku = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; # PENGEN DIRETURN JADI [5, 4, 3, 2, 1, 10, 9, 8, 7, 6]

# def rev(x):
#     jawaban = [];
#     for a in range(int(len(x)/2)-1, -1, -1):
#         jawaban.append(x[a]);
#     for a in range(len(x)-1, int(len(x)/2)-1, -1):
#         jawaban.append(x[a]);
#     x = jawaban
#     return x
# print(rev(listku))

# # REVERSE LIST SETENGAH AJA DIGANJILIN

# listku = [1, 2, 3, 4, 5, 6, 7, 8, 9]; # PENGEN DIRETURN JADI [5, 4, 3, 2, 1, 10, 9, 8, 7, 6]

# def rev(x):
#     import math
#     jawaban = [];
#     for a in range(math.ceil(len(x)/2)-1, -1, -1):
#         jawaban.append(x[a]);
#     for a in range(len(x)-1, math.ceil(len(x)/2)-1, -1):
#         jawaban.append(x[a]);
#     x = jawaban
#     return x
# print(rev(listku))

# # BUBBLE SORT

# x = [6000, 34, 203, 3, 746, 200, 984, 198, 764, 9, 1];

# def bubblesort(list):
#     for i in range(len(list), 0, -1):
#         for j in range(0, i-1):
#             if (list[j] > list[j + 1]):
#                 temp = list[j];
#                 list[j] = list[j + 1];
#                 list[j + 1] = temp;
#     return list;

# print(bubblesort(x))

# MEAN MEDIAN MODE

data = [1, 2, 3, 2, 5, 2, 7, 2];

# # ITUNG MEAN

# def itungmean(x):
#     sum = 0;
#     for a in x:
#         sum += a;
#     return sum / len(x)

# # ITUNG STDEV

# def itungstdev(x):
#     import math
#     sum = 0;
#     for i in x:
#         sum = sum + (pow((i - itungmean(x)), 2));
#     return math.sqrt(sum / (len(x) - 1))

# # ITUNG MEDIAN

# def itungmedian(x):
#     for a in range(len(x)-1):
#         for b in range(a + 1, len(x)):
#             if x[a] > x[b]:
#                 elea = x[a];
#                 eleb = x[b];
#                 x[a] = eleb;
#                 x[b] = elea;
#     if (len(x) % 2 == 0):
#         med = (x[int(len(x)/2)] + x[int(len(x)/2 - 1)]) / 2;
#     else:
#         med = x[int(len(x)/2)];
#     return med

# # ITUNG QUARTIL

# def itungq1(x):
#     for a in range(len(x)-1):
#         for b in range(a + 1, len(x)):
#             if x[a] > x[b]:
#                 elea = x[a];
#                 eleb = x[b];
#                 x[a] = eleb;
#                 x[b] = elea;
#     if (len(x) % 4 == 0):
#         med = (x[int(len(x)/4)] + x[int(len(x)/4 - 1)]) / 2;
#     else:
#         med = x[int(len(x)/4)];
#     return med

# def itungq3(x):
#     for a in range(len(x)-1):
#         for b in range(a + 1, len(x)):
#             if x[a] > x[b]:
#                 elea = x[a];
#                 eleb = x[b];
#                 x[a] = eleb;
#                 x[b] = elea;
#     if (len(x) % 4 == 0):
#         med = (x[int(len(x) * 3 / 4)] + x[int(len(x) * 3 / 4 - 1)]) / 2;
#     else:
#         med = x[int(len(x) * 3 / 4)];
#     return med

# def itungmode(mylist):
#     x = list(map(lambda f: str(f), mylist));
#     for a in range(len(x)-1):
#         for b in range(len(x)-1):
#             print(len(list(filter(lambda f: x[a] in f, x))), 'ini loop a ke', a)
#             print(len(list(filter(lambda f: x[b] in f, x))), 'ini loop b ke', b)
#             if (len(list(filter(lambda f: x[a] in f, x)))) > (len(list(filter(lambda f: x[b] in f, x)))):
#                 print(x[a])
#                 print(a)
#                 mod = x[a];
#     return mod

# data.sort()
# print(data)
# print(itungq3(data));

data = [1, 1, 2, 1, 3, 2, 4, 2, 1, 5, 2];
# setmode = []
# for a in range(len(data)-1):
#     for b in data:
#         if (data.count(data[a]) < data.count(b)):
#             setmode = [(data[b])]
#         if (data.count(data[a]) == data.count(b)):
#             setmode.append(data[b])
# print(set(setmode))
# print(setmode)

counter = [];
for i in range(0, len(data)):
    counter.append(data.count(data[i]));
listmode = dict(zip(data, counter));
# a = zip(data, counter)
# print(list(a))
# print(type(a))
# print(listmode)
jawab = {d for (d, c) in listmode.items() if c == max(counter)};
print(jawab)

# PUNYA MAS INDRA

def modes(x):
    himpunan = list(set(x))
    dictionary = {}

    for i in himpunan:
        dictionary[i] = 0

    for i in x:
        dictionary[i] += 1

    max_count = max(dictionary.values())

    modes = []
    for i in himpunan:
        if dictionary[i] == max_count:
            modes.append(i)
    
    return modes

x = [1,7,2,3,2,5,2,7,2]
print(modes(x))
