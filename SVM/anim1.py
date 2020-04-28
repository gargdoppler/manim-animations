from manimlib.imports import *


class train_data(ThreeDScene):

    CONFIG = {"plane_kwargs": {
        "x_line_frequency": 1,
        "y_line_frequency": 1
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
        db1 = Line(ep11, ep12, color=WHITE)

        ep31 = (4, -3, 0)
        ep32 = (-5, 1, 0)
        db3 = Line(ep31, ep32, color=WHITE)

        ep41 = (-5, 2, 0)
        ep42 = (5, -1, 0)
        db4 = Line(ep41, ep42, color=WHITE)

        ep51 = (5, -2, 0)
        ep52 = (-4, 3, 0)
        db5 = Line(ep51, ep52, color=WHITE)

        # ProbStat:
        fl = TextMobject("But, you can do these as well..")
        # sl = TextMobject("He promises to give you a prize, if")
        # tl = TextMobject("you are able to perform a task.")
        # tl.next_to(sl, DOWN)
        # ffl = TextMobject("The task is to seperate balls of")
        # fffl = TextMobject("two sets of colors.")
        # fffl.next_to(ffl, DOWN)

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

        self.play(GrowFromCenter(blue1), run_time=0.16)
        self.add(blue2)
        self.add(blue3)
        self.add(blue4)
        self.add(blue5)
        self.add(blue6)
        self.add(blue7)
        self.play(b1, b2, b3, b4, b5, b6, b7)

        self.play(ShowCreation(db1))
        self.wait(1)

        self.play(FadeOut(PINK1), run_time=0.01)
        self.play(FadeOut(PINK2), run_time=0.01)
        self.play(FadeOut(PINK3), run_time=0.01)
        self.play(FadeOut(PINK4), run_time=0.01)
        self.play(FadeOut(PINK5), run_time=0.01)
        self.play(FadeOut(PINK6), run_time=0.01)
        self.play(FadeOut(PINK7), run_time=0.01)
        self.play(FadeOut(blue1), run_time=0.01)
        self.play(FadeOut(blue2), run_time=0.01)
        self.play(FadeOut(blue3), run_time=0.01)
        self.play(FadeOut(blue4), run_time=0.01)
        self.play(FadeOut(blue5), run_time=0.01)
        self.play(FadeOut(blue6), run_time=0.01)
        self.play(FadeOut(blue7), run_time=0.01)
        self.play(FadeOut(db1), run_time=0.01)
        self.play(FadeOut(my_plane), run_time=0.01)
        self.play(ShowCreation(fl), run_time=2)
        self.wait(0.5)
        self.play(FadeOut(fl))
        self.play(ShowCreation(my_plane))
        self.add(PINK1)
        self.add(PINK2)
        self.add(PINK3)
        self.add(PINK4)
        self.add(PINK5)
        self.add(PINK6)
        self.add(PINK7)

        self.add(blue1)
        self.add(blue2)
        self.add(blue3)
        self.add(blue4)
        self.add(blue5)
        self.add(blue6)
        self.add(blue7)

        self.play(ShowCreation(db1))
        self.play(ShowCreation(db3))
        self.play(ShowCreation(db4))
        self.play(ShowCreation(db5))
        self.wait(2)
