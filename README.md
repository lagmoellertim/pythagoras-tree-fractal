# Pythagoras Tree Fractal Generator

## Introduction
The Pythagoras Tree Fractal is a fractal that is made up of cubes and triangles. When it is generated with enough iterations, it looks like a tree, so that's where the name came from. You can read more over it on [wikipedia](https://en.wikipedia.org/wiki/Pythagoras_tree_(fractal)).

## Examples

![Image of Pythagoras Tree Fractal](https://github.com/lagmoellertim/pythagoras-tree-fractal/raw/master/examples/example_1.png)
![Image of Pythagoras Tree Fractal](https://github.com/lagmoellertim/pythagoras-tree-fractal/raw/master/examples/example_2.png)
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
You can specify the width, height, base_length, background_color, offset_x and offset_y as seen in the code documentation

### Generate a Tree

```python3
generator.generate()
```
You can choose the depth, background color, a style generation function, angle and mirror as seen in the code documentation

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

## Donations / Sponsors

I'm part of the official GitHub Sponsors program where you can support me on a monthly basis.

<a href="https://github.com/sponsors/lagmoellertim" target="_blank"><img src="https://github.com/lagmoellertim/shared-repo-files/raw/main/github-sponsors-button.png" alt="GitHub Sponsors" height="35px" ></a>

You can also contribute by buying me a coffee (this is a one-time donation).

<a href="https://ko-fi.com/lagmoellertim" target="_blank"><img src="https://github.com/lagmoellertim/shared-repo-files/raw/main/kofi-sponsors-button.png" alt="Ko-Fi Sponsors" height="35px" ></a>

Thank you for your support!

## License

[MIT License](https://github.com/lagmoellertim/cryption/blob/master/LICENSE)

Copyright © 2019-present, [Tim-Luca Lagmöller](https://en.lagmoellertim.de) & [Moritz Simonsmeier](https://github.com/simonchristiansen)

## Have fun :tada:
