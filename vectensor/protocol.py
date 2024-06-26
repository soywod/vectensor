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

import typing
import bittensor as bt


class VectensorSynapse(bt.Synapse):
    """
    The vectensor protocol representation which uses bt.Synapse as its base.
    This protocol helps in handling vectensor request and response communication
    between the miner and the validator.

    Attributes:
    - input: The image as base64 string sent by the validator.
    - output: The vectorized input, as raw XML SVG string.
    """
    
    # Required request input (image as base64 string), filled by sending dendrite caller.
    input: str
    
    # Optional request output (SVG as raw XML string), filled by receiving axon.
    output: typing.Optional[str] = None

    def deserialize(self) -> str:
        """
        Deserialize the miner response (output).

        Returns:
        - str: The deserialized response, which is the SVG as raw XML string.
        """
        return self.output
