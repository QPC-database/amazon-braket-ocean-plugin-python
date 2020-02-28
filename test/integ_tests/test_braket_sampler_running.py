# Copyright 2019-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

import minorminer
from braket.ocean_plugin import BraketSampler, BraketSamplerArns
from conftest import to_base_ten
from dwave.embedding import embed_bqm, unembed_sampleset


def test_factoring_minorminer(aws_session, s3_destination_folder, factoring_bqm, integer_to_factor):
    sampler = BraketSampler(
        s3_destination_folder, device_arn=BraketSamplerArns.DWAVE, aws_session=aws_session
    )
    _, target_edgelist, target_adjacency = sampler.structure
    embedding = minorminer.find_embedding(factoring_bqm.quadratic, target_edgelist)
    bqm_embedded = embed_bqm(factoring_bqm, embedding, target_adjacency, 3.0)
    unembeded_response = sampler.sample(bqm_embedded, shots=1000, resultFormat="histogram")
    response = unembed_sampleset(unembeded_response, embedding, source_bqm=factoring_bqm)
    sample, energy = next(response.data(["sample", "energy"]))
    a, b = to_base_ten(sample)
    assert a * b == integer_to_factor
