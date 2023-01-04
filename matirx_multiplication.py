def validity(a,b):
    row_a = len(a)
    column_a = len(a[0])

    row_b = len(b)
    column_b = len(b[0])

    if column_a == row_b:
        print(f'Valid operation and order of new matrix: {row_a} X {column_b}')
        return True
    else:
        print('Not a valid operation')
        return False



def matrix_multiply(a,b):
    if validity(a,b):
        ans = []
        for i in range(len(a)):
            temp = []
            for j in range(len(b[0])):
                elem = 0
                for k in range(len(a[i])):
                    elem += a[i][k] * b[k][j]
                temp.append(elem)
            ans.append(temp)
        
        return ans


matrix_1 = [
    [9,5,2],
    [1,8,5],
    [3,1,6]
]

matrix_2 = [
    [3,2],
    [1,4],
    [5,3]
]

product = matrix_multiply(matrix_1,matrix_2)

print(f'product : {product}')