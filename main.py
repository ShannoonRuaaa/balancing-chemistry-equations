import numpy as np
from fractions import Fraction
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

def rref(matrix):
    tol = 1e-10  # Tolerance for floating-point comparisons
    lead = 0
    rowCount, columnCount = matrix.shape
    rank = 0  # Initialize rank
    for r in range(rowCount):
        if lead >= columnCount:
            return rank
        i = r
        while abs(matrix[i, lead]) < tol:
            i += 1
            if i == rowCount:
                i = r
                lead += 1
                if columnCount == lead:
                    return rank
        matrix[[i, r]] = matrix[[r, i]]
        if abs(matrix[r, lead] - 0.0) > tol:
            matrix[r] /= matrix[r, lead]
        for i in range(rowCount):
            if i != r:
                matrix[i] -= matrix[i, lead] * matrix[r]
        lead += 1
        rank += 1  # Increment rank
    return rank

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


total_elements = unique(total_elements)


matrix = []
for t in range(len(left_equation)):
    Matrix = []
    index = 0
    for j in total_elements:
        if index < len(left_equation[t][0]):
            if left_equation[t][0][index] == j:
                Matrix.append(Fraction(left_equation[t][1][index], 1))
                index+=1
            else:
                Matrix.append(Fraction(0,1))
        else: Matrix.append(Fraction(0,1))
    matrix.append(Matrix)

for t in range(len(right_equation)):
    Matrix = []
    index = 0
    for j in total_elements:
        if index < len(right_equation[t][0]):
            if right_equation[t][0][index] == j:
                Matrix.append(Fraction(right_equation[t][1][index]))
                index+=1
            else:
                Matrix.append(Fraction(0,1))
        else: Matrix.append(Fraction(0,1))
    matrix.append(Matrix)
# print(matrix)
matrix = np.transpose(np.array(matrix))
rank= rref(matrix)
# print(matrix)
# print(rank)
ans = []
for i in range(0,rank):
    sub = [matrix[i][rank::]]
    ans.append(sub)
# ans.append(np.eye(len(matrix[0])-rank,dtype=Fraction))
I = np.eye(len(matrix[0])-rank, dtype=Fraction)
for i in range(len(matrix[0]) - rank):
    ans.append([I[i]])
frac = Fraction(1,2)

print(ans)
# print(total_elements)
# print (left_equation)
# print (right_equation)
