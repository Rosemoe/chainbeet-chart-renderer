from parser import parse
from renderer import ChainbeetRenderer
import skia as sk

if __name__ == '__main__':
    chart = parse(open(f'assets/gengaozo.json', 'r').read())
    renderer = ChainbeetRenderer(chart, chart_name='G e n g a o z o [EXTRA 10]')
    image = renderer.render()
    image.save(open('gengaozo.png', 'wb'), sk.EncodedImageFormat.kPNG)
