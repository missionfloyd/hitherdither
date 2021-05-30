#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import numpy as np

def random_noise_dithering(image, palette, order=128):
    """Render the image using the random noise dithering pattern.

    Reference: http://caca.zoy.org/wiki/libcaca/study/1
               https://surma.dev/things/ditherpunk/

    :param :class:`PIL.Image` image: The image to apply the
        ordered dithering to.
    :param :class:`~hitherdither.colour.Palette` palette: The palette to use.
    :param int order: Noise intensity
    :return:  The dithered PIL image of type "P" using the input palette.

    """

    ni = np.array(image)
    noise = np.random.normal(0, order, ni.shape)
    new_image = ni + noise
    return palette.create_PIL_png_from_rgb_array(new_image)

def interleaved_gradient_noise(image, palette, order=128):
    """Render the image using the interleaved gradient noise pattern.

    Reference:
        http://www.iryoku.com/next-generation-post-processing-in-call-of-duty-advanced-warfare

    :param :class:`PIL.Image` image: The image to apply the
        ordered dithering to.
    :param :class:`~hitherdither.colour.Palette` palette: The palette to use.
    :param int order: Noise intensity
    :return: The dithered PIL image of type "P" using the input palette.

    """

    ni = np.array(image)
    noise = np.zeros(ni.shape[:2], "float")
    for x, y in np.ndindex(noise.shape):
        noise[x, y] = (((52.9829189 * (0.06711056 * x + 0.00583715 * y) % 1) % 1) - 0.5) * order
    new_image = ni + np.repeat(np.expand_dims(noise, 2), 3, 2)
    return palette.create_PIL_png_from_rgb_array(new_image)
