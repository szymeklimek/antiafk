import json
import win32com.client as comclt
import win32gui
import time
from datetime import timedelta

DEFAULT_WAIT_TIME = 480
DEFAULT_LOGOUT_DELAY = 5
DEFAULT_LOGIN_DELAY = 10
DEFAULT_CONFIG_PATH = "./config.json"
WOW_WINDOW_NAME = "World of Warcraft"


class AntiAFK:
    def __init__(self, config_path: str = DEFAULT_CONFIG_PATH) -> None:
        self.config_path = config_path
        self.config = self._init_from_config()
        self.logout_delay = self.config.get("logout_delay", DEFAULT_LOGOUT_DELAY)
        self.login_delay = self.config.get("login_delay", DEFAULT_LOGIN_DELAY)
        self.wait_time = self.config.get("wait_time", DEFAULT_LOGIN_DELAY)
        self.win_client = comclt.Dispatch("WScript.Shell")
        self.counter = 0

    def _init_from_config(self) -> dict:
        try:
            with open(self.config_path, "r") as file:
                config = json.load(file)
        except FileNotFoundError:
            print("config.json not found, creating default...\n")
            config = self._create_default_config()
        return config

    def _create_default_config(self) -> str:
        config = {
            "wait_time": DEFAULT_WAIT_TIME,
            "logout_delay": DEFAULT_LOGOUT_DELAY,
            "login_delay": DEFAULT_LOGIN_DELAY,
        }
        with open(self.config_path, "w") as file:
            json.dump(config, file
            )
        return config

    def _write_command(self, input_str: str) -> None:
        for ch in input_str:
            self.win_client.SendKeys(ch)
            time.sleep(0.05)
        self.win_client.SendKeys("{ENTER}")

    def _wait_and_countdown(self, msg: str, wait_time: int) -> None:
        for i in range(wait_time, 0, -1):
            print(f"{msg}: {i}s...", end="\r", flush=True)
            time.sleep(1)

    def _focus_window(self, window_name: str = WOW_WINDOW_NAME) -> None:
        handle = win32gui.FindWindow(None, window_name)
        win32gui.SetForegroundWindow(handle)

    def run(self) -> None:
        while True:
            self._wait_and_countdown("Logging out in", self.logout_delay)
            self._focus_window()
            self._write_command("/logout")
            self._wait_and_countdown("Logged out, logging in in", self.login_delay)
            self.win_client.SendKeys("{ENTER}")
            self.counter += 1
            self._wait_and_countdown("Logged in, logging out in", self.wait_time)


def main():
    try:
        print("\nAntiAFK. Press ctrl + C to exit.\n")
        start_time = time.monotonic()
        client = AntiAFK()
        client.run()
    except KeyboardInterrupt:
        total_run_time = str(timedelta(seconds=time.monotonic()-start_time))[:-7]
        print("\n")
        print(f"Script ran for {total_run_time}.")
        print(f"Logged in and out {client.counter} times.\n")
        exit()


if __name__ == "__main__":
    main()
