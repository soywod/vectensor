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

from base64 import b64encode
import bittensor as bt

from vectensor.protocol import VectensorSynapse
from vectensor.validator import generate
from vectensor.validator.reward import get_rewards
from vectensor.utils.uids import get_random_uids


async def forward(self):
    miner_uids = vectensor.utils.uids.get_random_uids(self, k=min(self.config.neuron.sample_size, self.metagraph.n.item()))
    image = await generate.image()

    # The dendrite client queries the network.
    responses = await self.dendrite(
        axons=[self.metagraph.axons[uid] for uid in miner_uids],
        synapse=VectensorSynapse(input=b64encode(image)),
        deserialize=False,
    )
    bt.logging.info(f"Received responses: {responses}")

    rewards = get_rewards(self, image=image, responses=responses)
    bt.logging.info(f"Scored responses: {rewards}")

    self.update_scores(rewards, miner_uids)
