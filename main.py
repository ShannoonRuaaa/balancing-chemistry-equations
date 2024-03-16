import numpy as np

def chemical_formula(formula):
    chemicals = []
    numbers = []
    prevIschar = False
    mulpiliter = 0
    for char in formula:
        if char.isdigit():
            mulpiliter = 10 * mulpiliter +int(char)
            formula = formula[1:]
        else:
            break
    for char in formula:
        if char.isalpha():
            prevIschar = True
            if char.isupper():
                chemicals.append(str(char))
                numbers.append(1)
            else:
                chemicals[-1] += str(char)
        else:
            if prevIschar:
                numbers[-1] = int(char)
            else:
                numbers[-1] = numbers[-1] * 10 + int(char)
    if mulpiliter == 0:
        return chemicals, numbers
    else:
        for i in range(len(chemicals)):
            numbers[i] = numbers[i] * mulpiliter
        return chemicals, numbers

def row_reduction(arr):
    l = len(arr)
    for i in range(l-1):
        # find largest piviot
        greatest_val = np.abs(arr[i][i])
        index = i
        for j in range(i,l):
             if np.abs(arr[j][i] )> greatest_val:
                index = j
                greatest_val = np.abs(arr[j][i])
        #exchanges pivots
        # if greatest_val == 0: return arr
        temp = arr[i]
        arr[i] = arr[index]
        arr[index] = temp
    #subtract each by muylt
        for j in range(i+1, l):
            arr[j] = np.subtract(np.multiply(arr[j], arr[i][i]), np.multiply(arr[i], arr[j][i]))


    for i in range(l-1, 0, -1):
        for j in range(i-1, -1, -1):
            if arr[i][i]!=0:
                arr[j] = np.subtract(np.multiply(arr[j], arr[i][i]), np.multiply(arr[i], arr[j][i]))

    for i in range(l):
        if arr[i][i]!=0:
            arr[i] = np.divide(arr[i], arr[i][i])
    return arr

def split_formula(formula):
    reactants = []
    products = []
    list = formula.split()
    isreactant = True
    for i in list:
        if i == "->":
            isreactant = False
        elif i == "+":
            continue
        elif isreactant:
            reactants.append(i)
        else:
            products.append(i)
    return reactants, products
def transpose(matrix):
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("Input must be a 2D list")

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    transposed_matrix = [[0 for _ in range(num_rows)] for _ in range(num_cols)]

    for i in range(num_rows):
        for j in range(num_cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix

def unique (combined_list):
    unique_list = []
    for item in combined_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

Chem = "Na + Cl2 -> NaCl"
# checmicals, numbers = chemical_formula(Chem)
reactants, product = split_formula(Chem)
left_equation = []
right_equation = []

total_elements =[]

for i in reactants:
    chemical, numbers = chemical_formula(i)
    total_elements+=chemical
    left_equation.append([chemical, numbers])
for i in product:
    chemical, numbers = chemical_formula(i)
    right_equation.append([chemical, numbers])

arr = [[1,2,3,4,5],[6,7,8,9,10]]

total_elements = unique(total_elements)


matrix = []
for t in range(len(left_equation)):
    Matrix = []
    index = 0
    for j in total_elements:
        if index < len(left_equation[t][0]):
            if left_equation[t][0][index] == j:
                Matrix.append(left_equation[t][1][index])
                index+=1
            else:
                Matrix.append(0)
        else: Matrix.append(0)
    matrix.append(Matrix)

for t in range(len(right_equation)):
    Matrix = []
    index = 0
    for j in total_elements:
        if right_equation[t][0][index] == j:
            Matrix.append(right_equation[t][1][index])
            index+=1
        else:
            Matrix.append(0)
    matrix.append(Matrix)

matrix = transpose(matrix)
matrix = row_reduction(matrix)
ans = []
for i in range(0,len(matrix[0])):
    if i < len(matrix):
        if matrix[i][-1]!=0:
            ans.append(-matrix[i][-1])
        else: ans.append(1)
    else: ans.append(1.0)
print(ans)
# print(total_elements)
# print (left_equation)
# print (right_equation)
