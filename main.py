def product(x1 ,y1 ,x2 ,y2 ,x3 ,y3):
    # 计算叉乘
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)


def isInTriangle(x_t_1 ,y_t_1 ,x_t_2 ,y_t_2 ,x_t_3 ,y_t_3 ,x_o ,y_o):
    if product(x_t_1 ,y_t_1 ,x_t_2 ,y_t_2 ,x_t_3 ,y_t_3) < 0:
        # 保证是逆时针
        return isInTriangle(x_t_1 ,y_t_1 ,x_t_3 ,y_t_3 ,x_t_2 ,y_t_2 ,x_o ,y_o)
    if product(x_t_1 ,y_t_1 ,x_t_2 ,y_t_2 ,x_o ,y_o) > 0 and product(x_t_2 ,y_t_2 ,x_t_3 ,y_t_3 ,x_o ,y_o) > 0 and product(
            x_t_3 ,y_t_3 ,x_t_1 ,y_t_1 ,x_o ,y_o) > 0:
        return True
    return False

if __name__ == '__main__':
    x_s = 0.01
    y_s = 0.0

    x_a_1 = 0.0
    y_a_1 = 0.0

    x_a_2 = 0.1
    y_a_2 = 0.1 / np.sqrt(3)

    x_a_3 = 0.0
    y_a_3 = -0.2 / np.sqrt(3)


    print(isInTriangle(x_a_1,y_a_1,x_a_2,y_a_2,x_a_3,y_a_3,x_s,y_s))
