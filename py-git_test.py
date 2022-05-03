from unittest.mock import patch
from unittest.mock import MagicMock
import unittest
class TestGitClass(unittest.TestCase):

    def setUp(self):
        self.gc = GitClass()

    def test_simple(self):
        candidate = 1
        input = 2
        result = self.gc.compare(candidate, input)
        expected = "release"
        self.assertEquals(result, expected)

    def test_simple_with_feature(self):
        candidate = 20
        input = 1
        result = self.gc.compare(candidate, input)
        expected = "feature"
        self.assertEquals(result, expected)

    def test_simple_with_mock(self):
        self.gc.find_latest_release_branch = MagicMock(return_value="a simple mock branch")
        candidate = 1
        input = 2
        result = self.gc.compare(candidate, input)
        expected = "somebranch"
        self.assertEquals(result, expected)

    @patch("__main__.GitClass.find_latest_release_branch")
    def test_simple_with_patch(self, mock):
        mock.return_value = "a patched mock branch name"
        candidate = 1
        input = 2
        result = self.gc.compare(candidate, input)
        expected = "somebranch"
        self.assertEquals(result, expected)        

class GitClass():
    def find_latest_release_branch(self, input ):
        if "release" in input:
            return "release"
        else:
            return "feature"

    def compare(self,candidate, input):
        res = None
        if candidate < input:
            res = self.find_latest_release_branch("release")
        else:
            res = self.find_latest_release_branch("")
        return res

if __name__ == '__main__':
    unittest.main()