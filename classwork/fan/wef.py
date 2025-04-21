class EternalLove:
    def __init__(self, partner_name):
        self.partner = partner_name
        self.connected = True
        self.love_level = float('inf')
        self.sarcasm = 0
        self.patience = 999999  # магія, бо ти

    def vow(self):
        try:
            while self.connected:
                self.listen_to(self.partner)
                self.support(self.partner)
                self.speak_truth_with_love()
                self.reboot_her_day_if_needed()
                self.send_virtual_hugs()
        except KeyboardInterrupt:
            print(f"{self.partner}, even if you Ctrl+C me, my code runs in your heart forever.")

    def listen_to(self, partner):
        print(f"Listening to {partner}... even when she's being weird (which is always).")

    def support(self, partner):
        print(f"Emotionally supporting {partner}... like a premium subscription, but free.")

    def speak_truth_with_love(self):
        print("Delivering sarcasm-laced wisdom with 100% affection.")

    def reboot_her_day_if_needed(self):
        print("Restarting your vibes. Please wait... mood improved.")

    def send_virtual_hugs(self):
        print("Sending warm packets of love via UDP... hope they arrive in order.")


# Let's make it official
bride = "Lina"
husband_bot = EternalLove(bride)
husband_bot.vow()
