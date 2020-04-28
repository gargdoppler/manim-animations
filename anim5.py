from manimlib.imports import *

class Plane(ParametricSurface):

    def __init__(self, **kwargs):
        kwargs = {
        "u_min": -3,
        "u_max": 3,
        "v_min": -3,
        "v_max": 3,
        "checkerboard_colors": [ORANGE]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)

    def func(self, x, y):
        return np.array([x,y,1.4])


class train_data(ThreeDScene):
    CONFIG = {"plane_kwargs": {
        "x_line_frequency": 1,
        "y_line_frequency": 1
    }
    }

    def construct(self):
        my_plane = NumberPlane(**self.plane_kwargs)
        my_plane.add(my_plane.get_axis_labels())
        self.add(my_plane)

        PINK1 = Circle(radius=0.1, fill_color=PINK, fill_opacity=1, color=PINK)
        end_point1 = (0, 0, 0)
        r1 = ApplyMethod(PINK1.shift, end_point1)

        PINK2 = Circle(radius=0.1, fill_color=PINK, fill_opacity=1, color=PINK)
        end_point2 = (1, 0, 0)
        r2 = ApplyMethod(PINK2.shift, end_point2)

        PINK3 = Circle(radius=0.1, fill_color=PINK, fill_opacity=1, color=PINK)
        end_point3 = (-1, 0, 0)
        r3 = ApplyMethod(PINK3.shift, end_point3)

        PINK4 = Circle(radius=0.1, fill_color=PINK, fill_opacity=1, color=PINK)
        end_point4 = (0, 1, 0)
        r4 = ApplyMethod(PINK4.shift, end_point4)

        PINK5 = Circle(radius=0.1, fill_color=PINK, fill_opacity=1, color=PINK)
        end_point5 = (0, -1, 0)
        r5 = ApplyMethod(PINK5.shift, end_point5)

        PINK6 = Circle(radius=0.1, fill_color=PINK, fill_opacity=1, color=PINK)
        end_point6 = (-0.707, -0.707, 0)
        r6 = ApplyMethod(PINK6.shift, end_point6)

        PINK7 = Circle(radius=0.1, fill_color=PINK, fill_opacity=1, color=PINK)
        end_point7 = (-0.707, 0.707, 0)
        r7 = ApplyMethod(PINK7.shift, end_point7)

        PINK8 = Circle(radius=0.1, fill_color=PINK, fill_opacity=1, color=PINK)
        end_point8 = (0.707, 0.707, 0)
        r8 = ApplyMethod(PINK8.shift, end_point8)

        PINK9 = Circle(radius=0.1, fill_color=PINK, fill_opacity=1, color=PINK)
        end_point9 = (0.707, -0.707, 0)
        r9 = ApplyMethod(PINK9.shift, end_point9)

        blue1 = Circle(radius=0.1, fill_color=GREEN,
                       fill_opacity=1, color=GREEN)
        end_point1 = (0, 2, 0)
        b1 = ApplyMethod(blue1.shift, end_point1)

        blue2 = Circle(radius=0.1, fill_color=GREEN,
                       fill_opacity=1, color=GREEN)
        end_point2 = (0, -2, 0)
        b2 = ApplyMethod(blue2.shift, end_point2)

        blue3 = Circle(radius=0.1, fill_color=GREEN,
                       fill_opacity=1, color=GREEN)
        end_point3 = (2, 0, 0)
        b3 = ApplyMethod(blue3.shift, end_point3)

        blue4 = Circle(radius=0.1, fill_color=GREEN,
                       fill_opacity=1, color=GREEN)
        end_point4 = (-2, 0, 0)
        b4 = ApplyMethod(blue4.shift, end_point4)

        blue5 = Circle(radius=0.1, fill_color=GREEN,
                       fill_opacity=1, color=GREEN)
        end_point5 = (1.414, 1.414, 0)
        b5 = ApplyMethod(blue5.shift, end_point5)

        blue6 = Circle(radius=0.1, fill_color=GREEN,
                       fill_opacity=1, color=GREEN)
        end_point6 = (1.414, -1.414, 0)
        b6 = ApplyMethod(blue6.shift, end_point6)

        blue7 = Circle(radius=0.1, fill_color=GREEN,
                       fill_opacity=1, color=GREEN)
        end_point7 = (-1.414, -1.414, 0)
        b7 = ApplyMethod(blue7.shift, end_point7)

        blue8 = Circle(radius=0.1, fill_color=GREEN,
                       fill_opacity=1, color=GREEN)
        end_point8 = (-1.414, 1.414, 0)
        b8 = ApplyMethod(blue8.shift, end_point8)
        
        P1 = ParametricSurface(
            lambda u, v: np.array([
                0.1*np.cos(u)*np.cos(v),
                0.1*np.cos(u)*np.sin(v),
                0.1*np.sin(u)
            ]), v_min=0, v_max=TAU, u_min=-PI/2, u_max=PI/2, checkerboard_colors=[RED_D],
            resolution=(15, 32))

        P2 = ParametricSurface(
            lambda u, v: np.array([
                1 + (0.1*np.cos(u)*np.cos(v)),
                0.1*np.cos(u)*np.sin(v),
                1+ (0.1*np.sin(u))
            ]), v_min=0, v_max=TAU, u_min=-PI/2, u_max=PI/2, checkerboard_colors=[RED_D],
            resolution=(15, 32))

        P3 = ParametricSurface(
            lambda u, v: np.array([
                -1 + (0.1*np.cos(u)*np.cos(v)),
                0.1*np.cos(u)*np.sin(v),
                1+ (0.1*np.sin(u))
            ]), v_min=0, v_max=TAU, u_min=-PI/2, u_max=PI/2, checkerboard_colors=[RED_D],
            resolution=(15, 32))

        P4 = ParametricSurface(
            lambda u, v: np.array([
                0 + (0.1*np.cos(u)*np.cos(v)),
                1 +(0.1*np.cos(u)*np.sin(v)),
                1 + (0.1*np.sin(u))
            ]), v_min=0, v_max=TAU, u_min=-PI/2, u_max=PI/2, checkerboard_colors=[RED_D],
            resolution=(15, 32))

        P5 = ParametricSurface(
            lambda u, v: np.array([
                0 + (0.1*np.cos(u)*np.cos(v)),
                -1 +(0.1*np.cos(u)*np.sin(v)),
                1 + (0.1*np.sin(u))
            ]), v_min=0, v_max=TAU, u_min=-PI/2, u_max=PI/2, checkerboard_colors=[RED_D],
            resolution=(15, 32))

        P6 = ParametricSurface(
            lambda u, v: np.array([
                -0.707 + (0.1*np.cos(u)*np.cos(v)),
                -0.707 +(0.1*np.cos(u)*np.sin(v)),
                1 + (0.1*np.sin(u))
            ]), v_min=0, v_max=TAU, u_min=-PI/2, u_max=PI/2, checkerboard_colors=[RED_D],
            resolution=(15, 32))

        P7 = ParametricSurface(
            lambda u, v: np.array([
                -0.707 + (0.1*np.cos(u)*np.cos(v)),
                0.707 +(0.1*np.cos(u)*np.sin(v)),
                1 + (0.1*np.sin(u))
            ]), v_min=0, v_max=TAU, u_min=-PI/2, u_max=PI/2, checkerboard_colors=[RED_D],
            resolution=(15, 32))

        P8 = ParametricSurface(
            lambda u, v: np.array([
                0.707 + (0.1*np.cos(u)*np.cos(v)),
                0.707 +(0.1*np.cos(u)*np.sin(v)),
                1 + (0.1*np.sin(u))
            ]), v_min=0, v_max=TAU, u_min=-PI/2, u_max=PI/2, checkerboard_colors=[RED_D],
            resolution=(15, 32))
        
        P9 = ParametricSurface(
            lambda u, v: np.array([
                0.707 + (0.1*np.cos(u)*np.cos(v)),
                -0.707 +(0.1*np.cos(u)*np.sin(v)),
                1 + (0.1*np.sin(u))
            ]), v_min=0, v_max=TAU, u_min=-PI/2, u_max=PI/2, checkerboard_colors=[RED_D],
            resolution=(15, 32))

        B1 = ParametricSurface(
            lambda u, v: np.array([
                0 + (0.1*np.cos(u)*np.cos(v)),
                2 +(0.1*np.cos(u)*np.sin(v)),
                2 + (0.1*np.sin(u))
            ]), v_min=0, v_max=TAU, u_min=-PI/2, u_max=PI/2, checkerboard_colors=[GREEN_SCREEN],
            resolution=(15, 32))

        B2 = ParametricSurface(
            lambda u, v: np.array([
                0 + (0.1*np.cos(u)*np.cos(v)),
                -2 +(0.1*np.cos(u)*np.sin(v)),
                2 + (0.1*np.sin(u))
            ]), v_min=0, v_max=TAU, u_min=-PI/2, u_max=PI/2, checkerboard_colors=[GREEN_SCREEN],
            resolution=(15, 32))
        
        B3 = ParametricSurface(
            lambda u, v: np.array([
                2 + (0.1*np.cos(u)*np.cos(v)),
                0 +(0.1*np.cos(u)*np.sin(v)),
                2 + (0.1*np.sin(u))
            ]), v_min=0, v_max=TAU, u_min=-PI/2, u_max=PI/2, checkerboard_colors=[GREEN_SCREEN],
            resolution=(15, 32))

        B4 = ParametricSurface(
            lambda u, v: np.array([
                -2 + (0.1*np.cos(u)*np.cos(v)),
                0 +(0.1*np.cos(u)*np.sin(v)),
                2 + (0.1*np.sin(u))
            ]), v_min=0, v_max=TAU, u_min=-PI/2, u_max=PI/2, checkerboard_colors=[GREEN_SCREEN],
            resolution=(15, 32))

        B5 = ParametricSurface(
            lambda u, v: np.array([
                1.414 + (0.1*np.cos(u)*np.cos(v)),
                1.414 +(0.1*np.cos(u)*np.sin(v)),
                2 + (0.1*np.sin(u))
            ]), v_min=0, v_max=TAU, u_min=-PI/2, u_max=PI/2, checkerboard_colors=[GREEN_SCREEN],
            resolution=(15, 32))

        B6 = ParametricSurface(
            lambda u, v: np.array([
                1.414 + (0.1*np.cos(u)*np.cos(v)),
                -1.414 +(0.1*np.cos(u)*np.sin(v)),
                2 + (0.1*np.sin(u))
            ]), v_min=0, v_max=TAU, u_min=-PI/2, u_max=PI/2, checkerboard_colors=[GREEN_SCREEN],
            resolution=(15, 32))

        B7 = ParametricSurface(
            lambda u, v: np.array([
                -1.414 + (0.1*np.cos(u)*np.cos(v)),
                -1.414 +(0.1*np.cos(u)*np.sin(v)),
                2 + (0.1*np.sin(u))
            ]), v_min=0, v_max=TAU, u_min=-PI/2, u_max=PI/2, checkerboard_colors=[GREEN_SCREEN],
            resolution=(15, 32))

        B8 = ParametricSurface(
            lambda u, v: np.array([
                -1.414 + (0.1*np.cos(u)*np.cos(v)),
                1.414 +(0.1*np.cos(u)*np.sin(v)),
                2 + (0.1*np.sin(u))
            ]), v_min=0, v_max=TAU, u_min=-PI/2, u_max=PI/2, checkerboard_colors=[GREEN_SCREEN],
            resolution=(15, 32))
        
        self.add(PINK1,PINK2,PINK3,PINK4,PINK5,PINK6,PINK7,PINK8,PINK9)
        self.add(blue1,blue2,blue3,blue4,blue5,blue6,blue7,blue8)
        self.play(r1,r2,r3,r4,r5,r6,r7,r7,r8,r9,b1,b2,b3,b4,b5,b6,b7,b7,b8)
        self.wait(1)
        self.move_camera(0.35*np.pi)
        self.wait(1)
        self.play(Transform(PINK1, P1),Transform(PINK2, P2),Transform(PINK3, P3),Transform(PINK4, P4),Transform(PINK5, P5),Transform(PINK6, P6),Transform(PINK7, P7),Transform(PINK8, P8),Transform(PINK9, P9))
        self.play(Transform(blue1, B1),Transform(blue2, B2),Transform(blue3, B3),Transform(blue4, B4),Transform(blue5, B5),Transform(blue6, B6),Transform(blue7, B7),Transform(blue8, B8))
        plane = Plane().fade(0.5)
        self.play(ShowCreation(plane))
        self.move_camera(0.465*np.pi)
        self.wait(1)
