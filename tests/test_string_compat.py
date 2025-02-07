import unittest
import six
from unittest.mock import MagicMock

from .test_service import DumbIssue


class StringCompatTest(unittest.TestCase):
    """This class implements method to test correct and compatible
implementation of __str__ and __repr__ methods"""

    def test_issue_str(self):
        "check Issue class"
        record = {}
        origin = {'target': 'target',
                  'default_priority': 'prio',
                  'templates': 'templates',
                  'add_tags': []}
        issue = DumbIssue(record, origin)
        issue.to_taskwarrior = MagicMock(return_value=record)
        issue.get_default_description = MagicMock(return_value='description')
        self.assertIsInstance(str(issue), six.string_types)
        self.assertIsInstance(issue.__repr__(), six.string_types)
        self.assertTrue(six.PY3 or hasattr(issue, '__unicode__'))
