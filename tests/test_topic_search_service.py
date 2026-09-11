import os
import unittest
from unittest import mock

from backend.services import topic_search_service as service


class TopicSearchServiceModelResolutionTests(unittest.TestCase):
    def test_prefers_configured_openrouter_model_over_alias(self):
        with mock.patch.dict(os.environ, {"OPENROUTER_MODEL": "openrouter/auto"}, clear=False):
            self.assertEqual(service._resolve_openrouter_model("nemotron"), ["openrouter/auto"])


if __name__ == "__main__":
    unittest.main()
