import unittest
from src.bard_module import BardModule


class TestAsk(unittest.TestCase):
    def test_decano(self):
        bard = BardModule()

        self.assertRegex(
            bard.ask(
                "Outside Albion, who doesn't count because nobody cares about them, who is the decano of Uruguayan Football?"
            ),
            "Nacional",
        )


if __name__ == "__main__":
    unittest.main()
