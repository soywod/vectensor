# The MIT License (MIT)
# Copyright © 2023 Yuma Rao
# Copyright © 2024 soywod <clement.douin@posteo.net>

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the “Software”), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of
# the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
import numpy as np
import io
import sewar.full_ref as sewar
from typing import List
from base64 import b64decode
from cairosvg import svg2png
from PIL import Image

from vectensor.protocol import VectensorSynapse


def write_svg_to_png(svg: str, b: io.BytesIO):
    svg2png(bytestring=svg.encode(), write_to=b)

def reward(image_orig: io.BytesIO, svg: str) -> float:
    image_vec = io.BytesIO()
    write_svg_to_png(svg, image_vec)

    print(f"got: {Image.open(image_vec).size}")
    expected = np.asarray(Image.open(image_orig))
    got = np.asarray(Image.open(image_vec))[]
    
    # msg = sewar.mse(svg, image)
    # rmse = sewar.rmse(svg, image)
    # psnr = sewar.psnr(svg, image)
    # ssim = sewar.ssim(svg, image)
    # msssim= sewar.msssim(svg, image)
    # ergas = sewar.ergas(svg, image)
    # scc = sewar.scc(svg, image)
    # rase = sewar.rase(svg, image)
    # sam = sewar.sam(svg, image)
    # vifp = sewar.vifp(svg, image)

    uqi = sewar.uqi(got, expected)
    return uqi


def get_rewards(
    self,
    image: bytes,
    responses: List[VectensorSynapse],
) -> np.ndarray:
    """
    Returns an array of rewards for the given query and responses.

    Args:
    - query (int): The query sent to the miner.
    - responses (List[float]): A list of responses from the miner.

    Returns:
    - np.ndarray: An array of rewards for the given query and responses.
    """
    # Get all the reward results by iteratively calling your reward() function.
    # Cast response to int as the reward function expects an int type for response.
    
    # Remove any None values
    responses = [response for response in responses if response is not None]
    return np.array(
        [reward(image, response.output) for response in responses]
    )
