"""Determine if your browser is detectable by anti-bot services.
Some sites use scripts to detect Selenium and then block you."""
from seleniumbase import BaseCase

if __name__ == "__main__":
    from pytest import main
    main([__file__, "--uc", "--uc-cdp", "--incognito", "-s"])


class UndetectedTest(BaseCase):
    def verify_success(self):
        self.assert_text("OH YEAH, you passed!", "h1", timeout=12.5)
        self.post_message("Selenium wasn't detected!", duration=2.8)
        self._print("\n Success! Website did not detect Selenium! ")

    def fail_me(self):
        self.fail('Selenium was detected! Try using: "pytest --uc"')

    def test_browser_is_undetected(self):
        self.open("https://nowsecure.nl/#relax")
        try:
            self.verify_success()
        except Exception:
            if self.is_element_visible('input[value*="Verify"]'):
                self.click('input[value*="Verify"]')
            elif self.is_element_visible('iframe[title*="challenge"]'):
                self.switch_to_frame('iframe[title*="challenge"]')
                self.click("span.mark")
            else:
                self.fail_me()
            try:
                self.verify_success()
            except Exception:
                self.fail_me()
