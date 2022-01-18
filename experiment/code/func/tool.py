import cmath


def xy_to_polar_theta(x, y):
    """
    根据直角坐标计算对应的`角度`
    """
    z = complex(x, y)
    (_, theta) = cmath.polar(z)
    return theta