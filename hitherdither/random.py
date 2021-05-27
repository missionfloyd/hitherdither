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
