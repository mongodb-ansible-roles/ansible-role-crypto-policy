import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_crypto_policy(host):
    cmd = host.run("update-crypto-policies --show")
    assert cmd.stdout == "LEGACY\n"
