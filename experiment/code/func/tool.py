import cmath
import sympy
import math


def xy_to_polar_theta(x, y):
    """
    根据直角坐标计算对应的`角度`
    """
    z = complex(x, y)
    (_, theta) = cmath.polar(z)
    return theta


class Vector_equation:
    """
    ## import

    PA: 已知的向量 (包括 `角度` 和 `方向`)
    theta_AB: 已知向量的 `角度` (`弧度`)
    theta_PB: 已知向量的 `角度` (`弧度`)

    ![](../pict/3.jpg)


    ### Method

    1. 以 P 点为原点
    2. AB 的参数方程
    3. PB 的参数方程
    4. 联立参数方程 => 求解出 B 点位置
    """
    def __init__(self, PA, theta_AB, theta_PB):
        self.PA = PA
        self.theta_AB = theta_AB
        self.theta_PB = theta_PB
        self.x = 0.0
        self.y = 0.0

        self.__solve()

    def __solve(self):

        # x,y 为 PB 与 AB 的交点
        x, y, t1, t2 = sympy.symbols('x, y, t1, t2')
        # AB 的参数方程 交于交点
        fun_AB_x = self.PA.x + t1 * math.cos(self.theta_AB) - x
        fun_AB_y = self.PA.y + t1 * math.sin(self.theta_AB) - y
        # 同理 PB
        fun_PB_x = t2 * math.cos(self.theta_PB) - x
        fun_PB_y = t2 * math.sin(self.theta_PB) - y
        result = sympy.solve([fun_AB_x, fun_AB_y, fun_PB_x, fun_PB_y],
                             [x, y, t1, t2])
        self.x = result[x]
        self.y = result[y]