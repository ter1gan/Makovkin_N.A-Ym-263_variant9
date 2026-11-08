

def row_sums(matrix):

    result = []
    for row in matrix:
        result.append(sum(row))
    return result


def column_sums(matrix):

    if not matrix:
        return []
    columns = len(matrix[0])
    result = [0] * columns
    for row in matrix:
        for j in range(columns):
            result[j] += row[j]
    return result


def diagonal_pattern(size):

    pattern = []
    for row in range(size):
        new_row = []
        for column in range(size):
            if row == column:
                new_row.append(0)
            elif row < column:
                new_row.append(1)
            else:
                new_row.append(2)
        pattern.append(new_row)
    return pattern


def transform(matrix):

    result = []
    for row in matrix:
        new_row = []
        for value in row:
            if value % 3 == 0:
                new_row.append(3)
            else:
                new_row.append(value)
        result.append(new_row)
    return result