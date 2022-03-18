from PIL import Image, ImageColor
from PIL import ImageDraw
import numpy as np


class Fractal():
    def __init__(self):
        self.pmin, self.pmax, self.qmin, self.qmax = -2.5, 1.5, -2, 2
        self.ppoints, self.qpoints = 2048, 2048
        self.max_iter = 100
        self.infinity_border = 10

        self.image = Image.new("RGB", (self.ppoints, self.qpoints))
        self.draw = ImageDraw.Draw(self.image)

    def paint(self):
        for ip, p in enumerate(np.linspace(self.pmin, self.pmax, self.ppoints)):
            for iq, q in enumerate(np.linspace(self.qmin, self.qmax, self.qpoints)):
                c = p + 1j * q
                z = 0
                
                for k in range(self.max_iter):
                    z = z ** 2 + c
                    if abs(z) > self.infinity_border:
                        self.draw.point((ip, iq), fill=ImageColor.getrgb("white"))
                        break
        
        self.image.save("save.png", "PNG")


def main():
    start = Fractal()
    start.paint()
 
if __name__ == '__main__':
    main()