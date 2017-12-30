def helper(matrix, height, width, steps, pos, result) :
    if steps == 0:
        if valid(matrix):
            printRes(result);
    else:
        for i in range(pos, height + width + 2 - steps):
            reverse(matrix, height, width, i);
            result[i] = 1;
            helper(matrix, height, width, steps - 1, i + 1, result);
            result[i] = 0;
            reverse(matrix, height, width, i);

def reverse(matrix, height, width, pos):
    if pos < height:
        for i in range(0, width):
            matrix[pos][i] = 1 - matrix[pos][i];
    elif pos < height + width:
        for row in matrix:
            row[pos - height] = 1 - row[pos - height];
    else:
        if height <= width:
            for i in range(0, height):
                matrix[width - i - 1][i] = 1 - matrix[width - i - 1][i];
        else:
            for i in range(0, width):
                matrix[height - i - 1][i] = 1 - matrix[height - i - 1][i];


def valid(matrix):
    for row in matrix:
        for each in row:
            if each == 1:
                return False;
    return True;

def printRes(result):
    print("A solution");
    for each in result:
        print(str(each))
    print("Solution finished\n")

matrix = [
    [1,0,1,0,0],
    [1,0,1,1,1],
    [0,1,1,1,0],
    [0,0,0,1,0],
    [0,0,1,0,1],
    ];
steps = 6;
height = len(matrix)
width = len(matrix[0])

result = []
for i in range(0, height + width + 1):
    result.append(0);
    
helper(matrix, height, width, steps, 0, result);
print("program finished");
