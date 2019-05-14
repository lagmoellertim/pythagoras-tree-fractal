# Pythagoras Tree Fractal Generator

## Introduction
The Pythagoras Tree Fractal is a fractal that is made up of cubes and triangles. When it is generated with enough iterations, it looks like a tree, so that's where the name came from. You can read more over it on [wikipedia](https://en.wikipedia.org/wiki/Pythagoras_tree_(fractal)).

## Example

![Image of Pythagoras Tree Fractal](https://github.com/lagmoellertim/pythagoras-tree-fractal/raw/master/example.png)

## Prerequisites

- Python >= 3.2
- pip
- Pillow
- numpy

## Installation

```sh
git clone https://github.com/lagmoellertim/pythagoras-tree-fractal.git

cd pythagoras-tree-fractal
```

## Usage

### Initialize the Generation Process

```python3
generator = TreeFractal()
```
You can specify the width, height, base_length and background_color, as seen in the code documentation

### Generate a Tree

```python3
generator.generate()
```
You can choose the depth, background color and a style generation function, as seen in the code documentation

### Custom style generation function

You can create your own style generation functions, based on this example function
```python3
def new_style_generator(depth, shape=None):
    if shape == "cube":
        return {"fill": (depth*10, 0, 0), "outline": (0, 0, 0)}
    elif shape == "triangle":
        return {"fill": (0, 0, 0), "outline": (depth*10, 0, 0)}

generator.generate(style_gen=new_style_generator)
```

### Save the image

```python3
generator.save(*filename*)
```

## Contributing

If you are missing a feature or have new idea, go for it! That is what open-source is for!

## Author

**Tim-Luca Lagmöller** ([@lagmoellertim](https://github.com/lagmoellertim))

**Moritz Simonsmeier** ([@simonchristiansen](https://github.com/simonchristiansen))

## Donate

You can also contribute by [buying me a coffee](https://www.buymeacoffee.com/lagmoellertim).

## License

[MIT License](https://github.com/lagmoellertim/cryption/blob/master/LICENSE)

Copyright © 2019-present, [Tim-Luca Lagmöller](https://en.lagmoellertim.de) & [Moritz Simonsmeier](https://github.com/simonchristiansen)

## Have fun :tada:
