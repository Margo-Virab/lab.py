#1.Գրել ծրագիր, որը վերադարձնում է տրված տողը՝ “cat” այսպես՝ [“Cat”, “cAt”, “caT”], բոլոր հնարավոր տարբերակներով։ 

#2.Գրել ծրագիր, որը կհամեմատի տրված երկու տողերը և կվերադարձնի 0, եթե երկուսն էլ նույն տողն են, հակառակ դեպքում կվերադարձնի երկու տողերի տարբերությունը: Եթե տողերը հավասար չեն, կվերադարձնի -1:
#Օրինակ՝
#str1 = “unicorn”, str2 = “unicorn”, Output: 0
#str1 = “string”, str2 = “strong”, Output: i
#str1 = “cat”, str2 = “kitten”, Output: -1

str1 = input('Enter string1: ')
str2=input('Enter string2: ')
if len(str1)!=len(str2) :
    print(-1)
elif len(set(str1)-set(str2))!=0: print(list(set(str1)-set(str2)))
else: print(0)


                                                                                                                                                                                                                                                    

#4.Իրականացնել strMove(string, number, bool) ֆունկցիան, ստանում է տող, թիվ և բուլյան արժեք։ Եթե վերջինս True է, տողը տեղաշարժվում է աջ տրված թվի չափով, եթե False՝ ձախ։
#Օրինակ՝
#string = “Hello”, number = 2, bool = True, Output: loHel

a=[1, 3, 5, 6]
t=0
s=list(range(a[0], (t+1)))
if t in a: print(a.index(t))
else: 
    if t in s: print(s.index(t))
    else: print('%d not in list' % (t))


#5.Տրված է սորտավորված լիստ և մեկ կամայական թիվ։ Գրել ֆունկցիա, որը կվերադարձնի այդ թվի ինդեքսը լիստում, եթե այն առկա է, հակառակ դեպքում այն ինդեքսը, որտեղ որ կլիներ այդ թիվը, եթե պարունակվեր լիստում։
#Օրինակ՝
#nums = [1, 3, 5, 6], target = 5, Output: 2
#nums = [1, 3, 5, 6], target = 2, Output: 1

a=[1, 3, 5, 6]
t=int(input('Enter mumber: '))

s=list(range(a[0], (t+1)))
if t in a: print(a.index(t))
else: 
    if t in s: print(s.index(t))
    else: print('%d not in list' % (t))


#6.Գրել ծրագիր, որը կստանա երկու թիվ՝ m(rows) և n(columns), և կգեներացնի երկչափ զանգված(մատրից)։ i-րդ տողի j-րդ սյունակի էլեմենտը պետք է լինի i*j։ Փորձեք խնդիրը լուծել՝ օգտագործելով list comprehension:
m_row = int(input("Input number of rows: "))
n_col = int(input("Input number of columns: "))
matrix = [[0 for col in range(n_col)] for row in range(m_row)]

for row in range(m_row):
    for col in range(n_col):
        matrix[row][col]= row*col

print(matrix)

#7.Գրել ծրագիր, որը ստուգում է՝ տրված գաղտնաբառը վավեր է, թե ոչ։ Գաղտնաբառը վավեր է, եթե պարունակում է.
#Առնվազն մեկ մեծատառ
#Առնվազն մեկ թվանշան
#Առնվազն մեկ նշան այս ցուցակից՝ [$#@]
#Ամենաքիչը 6 նիշ
#Ամենաշատը 16 նիշ
