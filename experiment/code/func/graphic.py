from matplotlib.patches import Ellipse, Circle
import matplotlib.pyplot as plt


class Fig_position:
    """绘画机构位置简图"""
    def __init__(self, cood_param, A, B, r):
        self.cood_param = cood_param
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
        self.ax.plot([self.cood_param.B_up['x'], self.cood_param.B_down['x']],
                     [self.cood_param.B_up['y'], self.cood_param.B_down['y']],
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