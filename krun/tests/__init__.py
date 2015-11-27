from krun.tests.mocks import MockPlatform, MockMailer
from abc import ABCMeta
from krun.platform import detect_platform
import pytest


def subst_env_arg(lst, var):
    """Returns a copy of the list with elements starting with 'var=' changed to
    literally 'var='. Used in tests where an environment variable argument to
    env(1) contains a system-specific path."""

    find = var + "="
    new = []
    for i in lst:
        if i.startswith(find):
            i = find
        new.append(i)
    return new


class BaseKrunTest(object):
    """Abstract class defining common functionality for Krun tests."""

    __metaclass__ = ABCMeta

    @pytest.fixture
    def mock_platform(self):
        return MockPlatform(MockMailer())

    @pytest.fixture
    def platform(self):
        return detect_platform(MockMailer())

