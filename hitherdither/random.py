#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
bayer_dithering
-----------

"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import numpy as np
import math

def random_noise_dithering(image, palette, order=64):
    """Render the image using the random noise dithering pattern.

    Reference: http://caca.zoy.org/wiki/libcaca/study/1
               https://surma.dev/things/ditherpunk/

    :param :class:`PIL.Image` image: The image to apply the
        ordered dithering to.
    :param :class:`~hitherdither.colour.Palette` palette: The palette to use.
    :param int order: Standard deviation (spread or “width”) of the
        distribution. Must be non-negative.
    :return:  The random noise dithered PIL image of type "P"
        using the input palette.

    """

    ni = np.array(image, "uint8")
    noise = np.random.normal(0, order, ni.shape)
    new_image = ni + noise
    return palette.create_PIL_png_from_rgb_array(new_image)
   

def interleaved_gradient_noise(image, palette, order=128):
    """Render the image using the interleaved gradient noise pattern.

    Reference:
        https://bartwronski.com/2016/10/30/dithering-part-three-real-world-2d-quantization-dithering/

    :param :class:`PIL.Image` image: The image to apply the
        ordered dithering to.
    :param :class:`~hitherdither.colour.Palette` palette: The palette to use.
    :param int order:
    :return:  The random noise dithered PIL image of type "P"
        using the input palette.

    """

    ni = np.array(image, "uint8")
    noise = np.zeros(ni.shape[:2], "float")
    for x, y in np.ndindex(noise.shape):
        noise[x, y] = math.modf(52.9829189 * math.modf(0.06711056 * x + 0.00583715 * y)[0])[0] * 255 - order
    new_image = ni + np.repeat(np.expand_dims(noise, 2), 3, 2)
    return palette.create_PIL_png_from_rgb_array(new_image)
