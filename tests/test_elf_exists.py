from contextlib import nullcontext
import unittest

import open_prime_rando_practice_mod


class TestStringMethods(unittest.TestCase):
    def test_exists(self):
        test_cases = [
            (
                open_prime_rando_practice_mod.GameVersion.GC_NTSC,
                open_prime_rando_practice_mod.PracticeModMode.full,
                True,
            ),
            (
                open_prime_rando_practice_mod.GameVersion.GC_NTSC,
                open_prime_rando_practice_mod.PracticeModMode.disabled,
                True,
            ),
            (
                open_prime_rando_practice_mod.GameVersion.GC_PAL,
                open_prime_rando_practice_mod.PracticeModMode.full,
                False,
            ),
            (
                open_prime_rando_practice_mod.GameVersion.GC_PAL,
                open_prime_rando_practice_mod.PracticeModMode.disabled,
                False,
            )
        ]

        for game_version, practice_mod_mode, expected in test_cases:
            with self.subTest(f"{game_version}, {practice_mod_mode}"):
                if expected:
                    ctx = nullcontext()
                else:
                    ctx = self.assertRaises(ValueError)
                
                with ctx:
                    p = open_prime_rando_practice_mod.get_elf_for(
                        game_version,
                        practice_mod_mode,
                    )
                
                if expected:
                    self.assertTrue(p.is_file())
