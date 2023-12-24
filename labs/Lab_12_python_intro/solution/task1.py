
def count_routes(board_rows, board_columns):
    routes = [[0] * board_columns for _ in range(board_rows)]
    routes[0][0] = 1

    for i in range(board_rows):
        for j in range(board_columns):
            if (i >= 2 and j >= 1) or (i >= 1 and j >= 2):
                routes[i][j] = routes[i - 2][j - 1] + routes[i - 1][j - 2]

    return routes[board_rows - 1][board_columns - 1]

if __name__ == '__main__': # точка запуска решения
    board_rows, board_columns = map(int, input().split())  # ввод данных строк и столбцов шахматной доски
    result = count_routes(board_rows, board_columns) # вызов функции для подсчета количества маршрутов на доске
    print(result)  # вывод результата
