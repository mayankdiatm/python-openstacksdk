# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import copy

import testtools
import uuid

from openstack.network.v2 import qos_minimum_bandwidth_rule

EXAMPLE = {
    'id': 'IDENTIFIER',
    'qos_policy_id': 'qos-policy-' + uuid.uuid4().hex,
    'min_kbps': 1500,
    'direction': 'egress',
}


class TestQoSMinimumBandwidthRule(testtools.TestCase):

    def test_basic(self):
        sot = qos_minimum_bandwidth_rule.QoSMinimumBandwidthRule()
        self.assertEqual('minimum_bandwidth_rule', sot.resource_key)
        self.assertEqual('minimum_bandwidth_rules', sot.resources_key)
        self.assertEqual(
            '/qos/policies/%(qos_policy_id)s/minimum_bandwidth_rules',
            sot.base_path)
        self.assertEqual('network', sot.service.service_type)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_retrieve)
        self.assertTrue(sot.allow_update)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_list)

    def test_make_it(self):
        sot = qos_minimum_bandwidth_rule.QoSMinimumBandwidthRule(EXAMPLE)
        self.assertEqual(EXAMPLE['id'], sot.id)
        self.assertEqual(EXAMPLE['qos_policy_id'], sot.qos_policy_id)
        self.assertEqual(EXAMPLE['min_kbps'], sot.min_kbps)
        self.assertEqual(EXAMPLE['direction'], sot.direction)

    def test_create_body(self):
        params = copy.deepcopy(EXAMPLE)
        body = (qos_minimum_bandwidth_rule.QoSMinimumBandwidthRule.
                _get_create_body(params))
        reference = copy.deepcopy(EXAMPLE)
        reference.pop('qos_policy_id')
        self.assertEqual(reference, body['minimum_bandwidth_rule'])
