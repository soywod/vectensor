# The MIT License (MIT)
# Copyright © 2023 Opentensor Foundation

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

import sys
import torch
import unittest
import bittensor as bt

from neurons.validator import Validator
from neurons.miner import Miner

from vectensor.protocol import VectensorSynapse
from vectensor.validator.forward import forward
from vectensor.utils.uids import get_random_uids
from vectensor.validator.reward import get_rewards
from vectensor.base.validator import BaseValidatorNeuron


class VectensorValidatorNeuronTestCase(unittest.TestCase):
    """
    This class contains unit tests for the RewardEvent classes.

    The tests cover different scenarios where completions may or may not be successful and the reward events are checked that they don't contain missing values.
    The `reward` attribute of all RewardEvents is expected to be a float, and the `is_filter_model` attribute is expected to be a boolean.
    """

    def test_svg_to_png(self):
        svg = '<svg xmlns="http://www.w3.org/2000/svg" version="1.1"></svg>'
        png = validator.svg_to_png(svg)
        # TODO: Test a single step
        pass
