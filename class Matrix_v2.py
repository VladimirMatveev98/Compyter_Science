"""
# TODO:
--Реализовать сложение матриц;
--Реализовать вычитание матриц;
--Перемножение прямоугольных матриц (например, 2x3 * 3x2);
    -Возведение матрицы в степень???
--Вычисление определителя;
--Вычисление обратной матрицы???

--!!Удалять ненужные переменные после вычислений.Реализовать последним.
--Заменить данный раздел документацией с перечислением и описанием всех методов
"""

class Matrix:
    def __init__(self):
        self.mat = []


    def __str__(self):
        string = ''
        for i in self.mat:
            for j in i:
                string += str(j) + " "
            string += '\n'
        return string


    def __mul__(self,other):
        if type(other) == type(self):
            #Умножение на другую матрицу

        elif type(other) == type(1) or type(other) == type(1.1):
            #Умножение на число
            m_res = Matrix()
            list_res = []
            for i in self.mat:
                list_med = []
                for j in i:
                    list_med.append(j * other)
                list_res.append(list_med)
            m_res.insert(list_res)
            return m_res

        else:
            print("Не поддерживается умножение на тип ", type(other))
            return False



    def insert(self,list):
        self.mat = list




if __name__ == '__main__':

    test_1 = [[1, 2, 3],
              [2, 3, 4],
              [3, 4, 5]]

    test_2 = [[9, 8, 7],
              [8, 7, 6],
              [7, 6, 5]]

    m1 = Matrix()
    m2 = Matrix()

    m1.insert(test_1)
    m2.insert(test_2)

    print(m1)
    print(m2)

    m3 = m1 * m2
    print(m3)

    m4 = m1 * 5
    print(m4)

    m5 = m2 * "Hello world!"
    print(m5)
