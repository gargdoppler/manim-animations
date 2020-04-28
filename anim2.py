from manimlib.imports import *
import numpy as np


class train_data(Scene):
    CONFIG = {"plane_kwargs": {
        "x_line_frequency": 4,
        "y_line_frequency": 4
    }
    }

    def construct(self):

        my_plane = NumberPlane(**self.plane_kwargs)
        my_plane.add(my_plane.get_axis_labels())

        PINK1 = Circle(radius=0.1, fill_color=PINK, fill_opacity=1, color=PINK)
        end_point1 = (-4, 0, 0)
        r1 = ApplyMethod(PINK1.shift, end_point1)

        PINK2 = Circle(radius=0.1, fill_color=PINK, fill_opacity=1, color=PINK)
        end_point2 = (-4, -1, 0)
        r2 = ApplyMethod(PINK2.shift, end_point2)

        PINK3 = Circle(radius=0.1, fill_color=PINK, fill_opacity=1, color=PINK)
        end_point3 = (-3.5, -2.5, 0)
        r3 = ApplyMethod(PINK3.shift, end_point3)

        PINK4 = Circle(radius=0.1, fill_color=PINK, fill_opacity=1, color=PINK)
        end_point4 = (-2.8, -0.8, 0)
        r4 = ApplyMethod(PINK4.shift, end_point4)

        PINK5 = Circle(radius=0.1, fill_color=PINK, fill_opacity=1, color=PINK)
        end_point5 = (-2, -2, 0)
        r5 = ApplyMethod(PINK5.shift, end_point5)

        PINK6 = Circle(radius=0.1, fill_color=PINK, fill_opacity=1, color=PINK)
        end_point6 = (-0.5, -2.5, 0)
        r6 = ApplyMethod(PINK6.shift, end_point6)

        PINK7 = Circle(radius=0.1, fill_color=PINK, fill_opacity=1, color=PINK)
        end_point7 = (1, -2, 0)
        r7 = ApplyMethod(PINK7.shift, end_point7)

        blue1 = Circle(radius=0.1, fill_color=GREEN,
                       fill_opacity=1, color=GREEN)
        end_point1 = (-1, 2, 0)
        b1 = ApplyMethod(blue1.shift, end_point1)

        blue2 = Circle(radius=0.1, fill_color=GREEN,
                       fill_opacity=1, color=GREEN)
        end_point2 = (1, 2, 0)
        b2 = ApplyMethod(blue2.shift, end_point2)

        blue3 = Circle(radius=0.1, fill_color=GREEN,
                       fill_opacity=1, color=GREEN)
        end_point3 = (3, 2, 0)
        b3 = ApplyMethod(blue3.shift, end_point3)

        blue4 = Circle(radius=0.1, fill_color=GREEN,
                       fill_opacity=1, color=GREEN)
        end_point4 = (5, 2, 0)
        b4 = ApplyMethod(blue4.shift, end_point4)

        blue5 = Circle(radius=0.1, fill_color=GREEN,
                       fill_opacity=1, color=GREEN)
        end_point5 = (2, 1, 0)
        b5 = ApplyMethod(blue5.shift, end_point5)

        blue6 = Circle(radius=0.1, fill_color=GREEN,
                       fill_opacity=1, color=GREEN)
        end_point6 = (4.5, 1, 0)
        b6 = ApplyMethod(blue6.shift, end_point6)

        blue7 = Circle(radius=0.1, fill_color=GREEN,
                       fill_opacity=1, color=GREEN)
        end_point7 = (4, 0, 0)
        b7 = ApplyMethod(blue7.shift, end_point7)

        # Decision Boundary:
        ep11 = (-4, 2, 0)
        ep12 = (4, -2, 0)
        db1 = Line(ep11, ep12, color=YELLOW)

        ep31 = (-3.4, 3.2, 0)
        ep32 = (4.6, -0.8, 0)
        db2 = Line(ep31, ep32, color=WHITE)

        ep41 = (-4.6, 0.8, 0)
        ep42 = (3.4, -3.2, 0)
        db3 = Line(ep41, ep42, color=WHITE)

        # ProbStat:
        y1 = TextMobject("y = 1")
        y1.scale(0.75)
        p1 = (4, 3, 0)
        y1.next_to(p1)
        y2 = TextMobject("y = -1")
        y2.scale(0.75)
        p2 = (-6, -2, 0)
        y2.next_to(p2)
        eq1 = TextMobject("$\\vec{w} \\cdot \\vec{x} - b = -1$")
        eq1.scale(0.6)
        p3 = (-1.5, -1, 0)
        eq1.rotate(-TAU/13.5516)
        eq1.next_to(p3)
        eq2 = TextMobject("$\\vec{w} \\cdot \\vec{x} - b = 0$")
        eq2.scale(0.6)
        p4 = (-0.9, 0.2, 0)
        eq2.rotate(-TAU/13.5516)
        eq2.next_to(p4)
        eq3 = TextMobject("$\\vec{w} \\cdot \\vec{x} - b = 1$")
        eq3.scale(0.6)
        p5 = (-0.3, 1.4, 0)
        eq3.rotate(-TAU/13.5516)
        eq3.next_to(p5)

        e1 = np.array([-1, 2, 0])
        f1 = np.array([0.5, 3, 0])
        pointer1 = CurvedArrow(e1, f1, angle=-TAU/8, color=GREEN)

        t1 = TextMobject("Support")
        a1 = (0.5, 3, 0)
        t1.next_to(a1)

        e2 = np.array([1, -2, 0])
        f2 = np.array([-1, -3.5, 0])
        pointer2 = CurvedArrow(e2, f2, angle=-TAU/8, color=PINK)

        t2 = TextMobject("Support")
        a2 = (-3, -3.5, 0)
        t2.next_to(a2)

        # self.play(ShowCreation(fl))
        # self.wait(1)
        # self.play(Transform(fl, sl))
        # self.add(tl)
        # self.wait(0.5)
        # self.play(Transform(fl, ffl))
        # self.play(Transform(tl,fffl))
        # self.wait(0.5)
        # self.play(FadeOut(fl))
        # self.play(FadeOut(tl))
        self.play(ShowCreation(my_plane))
        self.play(GrowFromCenter(PINK1), run_time=0.16)
        self.add(PINK2)
        self.add(PINK3)
        self.add(PINK4)
        self.add(PINK5)
        self.add(PINK6)
        self.add(PINK7)
        self.play(r1, r2, r3, r4, r5, r6, r7)
        self.play(ShowCreation(y2))
        self.play(GrowFromCenter(blue1), run_time=0.16)
        self.add(blue2)
        self.add(blue3)
        self.add(blue4)
        self.add(blue5)
        self.add(blue6)
        self.add(blue7)
        self.play(b1, b2, b3, b4, b5, b6, b7)
        self.play(ShowCreation(y1))
        self.play(ShowCreation(db1), ShowCreation(eq2))
        self.play(ShowCreation(pointer2), ShowCreation(t1),
                  ShowCreation(t2), ShowCreation(pointer1), ShowCreation(db2), ShowCreation(db3), ShowCreation(eq1), ShowCreation(eq3))
        self.wait(5)
