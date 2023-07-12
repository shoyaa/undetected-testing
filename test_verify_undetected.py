"""Determine if your browser is detectable by anti-bot services.
Some sites use scripts to detect Selenium and then block you."""
from seleniumbase import BaseCase

if __name__ == "__main__":
    from pytest import main
    main([__file__, "--uc", "--uc-cdp", "--incognito", "-s"])


class UndetectedTest(BaseCase):
    def verify_success(self):
        self.assert_text("OH YEAH, you passed!", "h1", timeout=6.25)
        self.post_message("Selenium wasn't detected!", duration=2.8)
        self._print("\n Success! Website did not detect Selenium! ")

    def fail_me(self):
        self.fail('Selenium was detected! Try using: "pytest --uc"')

    def test_browser_is_undetected(self):
        self.open("https://nowsecure.nl/#relax")
        try:
            self.verify_success()
        except Exception:
            self.clear_all_cookies()
            self.get_new_driver(devtools=True)
            self.open("https://nowsecure.nl/#relax")
            try:
                self.verify_success()
            except Exception:
                self.fail_me()
