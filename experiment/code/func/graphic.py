from matplotlib.patches import Ellipse, Circle
import matplotlib.pyplot as plt


class Fig_position:
    """绘画机构位置简图"""
    def __init__(self, B_up, B_down, A, B, r):
        self.B_up = B_up
        self.B_down = B_down
        self.A = A
        self.B = B
        self.r = r
        fig = plt.figure()
        self.ax = fig.add_subplot(111)

    def __draw_O(self):
        x, y = 0, 0
        self.ax.plot(x, y, 'ro')

    def __draw_circles(self):
        cir = Circle(xy=(0.0, 0.0), radius=self.r, alpha=0.5)
        self.ax.add_patch(cir)

    def __draw_crank(self, A):
        self.ax.plot([0, A['x']], [0, A['y']], color="red")

    def __draw_link(self, A, B):
        self.ax.plot([A['x'], B['x']], [A['y'], B['y']], color="green")

    def __draw_slider(self):
        self.ax.plot([self.B_up['x'], self.B_down['x']],
                     [self.B_up['y'], self.B_down['y']],
                     color="red",
                     linestyle="--")

    def show(self, id_name):
        self.ax.set_title(id_name, fontsize=12, color='r')
        self.__draw_O()
        self.__draw_circles()
        self.__draw_crank(self.A)
        self.__draw_link(self.A, self.B)
        self.__draw_slider()

        plt.axis('scaled')
        #changes limits of x or y axis so that equal increments of x and y have the same length
        plt.axis('equal')
        plt.show()


"""尽可能复用代码吧, 增加一个接口就好了(本质就是化归), 保持外部简洁"""


def draw_position_figure(coord_param, A, B, r, id_name):
    temp_A = {'x': A.real, 'y': A.imag}
    temp_B = {'x': B.real, 'y': B.imag}
    temp_B_up = {'x': coord_param.B_up.real, 'y': coord_param.B_up.imag}
    temp_B_down = {'x': coord_param.B_down.real, 'y': coord_param.B_down.imag}
    fig = Fig_position(temp_B_up, temp_B_down, temp_A, temp_B, r)
    fig.show(id_name)


class Vect_Shape:
    def __init__(self, id_name):
        self.id_name = id_name

    def __draw_vec(self, ax, A, B):
        """绘画向量"""
        x = A['x']
        y = A['y']
        u = B['x'] - A['x']
        v = B['y'] - A['y']
        ax.quiver(x, y, u, v, angles='xy', scale_units='xy', scale=1)

    def __call_plt_show(self):
        plt.axis('scaled')
        #changes limits of x or y axis so that equal increments of x and y have the same length
        plt.axis('equal')
        plt.show()

    def show_vel(self, P, A, B, C2):
        self.fig = plt.figure()
        ax = self.fig.add_subplot(111)
        ax.set_title(self.id_name, fontsize=12, color='r')
        self.__draw_vec(ax, P, A)
        self.__draw_vec(ax, A, B)
        self.__draw_vec(ax, P, B)
        self.__draw_vec(ax, P, C2)
        plt.annotate("p",
                     xy=(P['x'], P['y']),
                     xytext=(2, 4),
                     textcoords='offset points')
        plt.annotate("a",
                     xy=(A['x'], A['y']),
                     xytext=(-2, -4),
                     textcoords='offset points')
        plt.annotate("b",
                     xy=(B['x'], B['y']),
                     xytext=(4, -2),
                     textcoords='offset points')
        plt.annotate("c2",
                     xy=(C2['x'], C2['y']),
                     xytext=(-4, -10),
                     textcoords='offset points')
        self.__call_plt_show()

    def show_acc(self, i, P, A, B, C2, D):
        self.fig = plt.figure()
        ax = self.fig.add_subplot(111)
        ax.set_title(self.id_name, fontsize=12, color='r')
        self.__draw_acc(ax, P, A)
        self.__draw_acc(ax, A, B)
        self.__draw_acc(ax, P, B)
        self.__draw_acc(ax, P, C2)
        self.__draw_acc(ax, A, D)
        self.__draw_acc(ax, D, B)
        plt.annotate("p",
                     xy=(P['x'], P['y']),
                     xytext=(2, 4),
                     textcoords='offset points')
        plt.annotate("a",
                     xy=(A['x'], A['y']),
                     xytext=(-2, -4),
                     textcoords='offset points')
        plt.annotate("b",
                     xy=(B['x'], B['y']),
                     xytext=(4, -2),
                     textcoords='offset points')
        plt.annotate("c2",
                     xy=(C2['x'], C2['y']),
                     xytext=(-4, -10),
                     textcoords='offset points')
        plt.annotate("d",
                     xy=(D['x'], D['y']),
                     xytext=(-4, -10),
                     textcoords='offset points')
        self.__call_plt_show()


def draw_velocity_figure(v_OA, v_OB, v_C2, id_name):
    P = {'x': 0, 'y': 0}
    A = {'x': v_OA.real, 'y': v_OA.imag}
    B = {'x': v_OB.real, 'y': v_OB.imag}
    C2 = {'x': v_C2.real, 'y': v_C2.imag}
    fig = Vect_Shape(id_name)
    fig.show_vel(P, A, B, C2)


def draw_acceleration_figure(a_OA, a_OB, a_OD, a_C2, id_name):
    P = {'x': 0, 'y': 0}
    A = {'x': a_OA.real, 'y': a_OA.imag}
    B = {'x': a_OB.real, 'y': a_OB.imag}
    C2 = {'x': a_C2.real, 'y': a_C2.imag}
    D = {'x': a_OD.real, 'y': a_OD.imag}
    fig = Vect_Shape(id_name)
    fig.show_acc(P, A, B, C2, D)