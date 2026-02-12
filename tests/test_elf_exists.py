import unittest

import open_prime_rando_practice_mod


class TestStringMethods(unittest.TestCase):
    def test_exists_ntsc_full(self):
        p = open_prime_rando_practice_mod.get_elf_for(
            open_prime_rando_practice_mod.GameVersion.GC_NTSC,
            open_prime_rando_practice_mod.PracticeModMode.full,
        )

        self.assertTrue(p.is_file())
