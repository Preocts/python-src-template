"""
Helper script, updates default values in setup.cfg

Since: 2021.06.20
Author: Preocts (Discord: Preocts#8196)
"""
import configparser
from typing import List

import setuptools


class TemplateSetup:
    """Helpful script to keep the setup.cfg updated"""

    SETUP_CONF = "./setup.cfg"

    def __init__(self) -> None:
        """Create instance and load SETUP_CONF"""
        self.config = self.load_config()

    def load_config(self) -> configparser.ConfigParser:
        """Returns the config as a ConfigParser object"""
        setup_config = configparser.ConfigParser()
        setup_config.read(self.SETUP_CONF)
        return setup_config

    def save_config(self) -> None:
        """Writes config to disk"""
        with open(self.SETUP_CONF, "w") as configfile:
            self.config.write(configfile)

    def update_metadata(self) -> None:
        """Run updates for [metadata]"""
        section = "metadata"
        option_list = [
            "name",
            "version",
            "description",
            "url",
            "author",
            "author_email",
        ]

        for option in option_list:
            value = self.user_prompt(option, self.config.get(section, option))
            self.config.set(section, option, value)

    def find_packages(self) -> List[str]:
        """Read the setup.cfg and return packages"""
        section = "options.packages.find"

        where = self.config.get(section, "where", fallback=".")
        exclude = self.multi_to_list(self.config.get(section, "exclude", fallback=""))
        include = self.multi_to_list(self.config.get(section, "include", fallback="*"))

        return setuptools.find_packages(where, exclude, include)

    def update_coverage(self) -> bool:
        """Updates (if exists) the coverage config to include package sources"""
        section = "coverage:run"
        package_list = self.find_packages()

        current = self.multi_to_list(
            self.config.get(section, "source_pkgs", fallback="")
        )

        new_list = sorted(package_list)

        self.config.set(section, "source_pkgs", "\n" + "\n".join(new_list))

        return current != new_list

    @staticmethod
    def user_prompt(option: str, current_value: str) -> str:
        """Prompt for input of option, default is current value"""
        in_ = input(
            f"Enter desired value for module {option} (default: {current_value}): "
        )
        return in_ if in_ else current_value

    @staticmethod
    def multi_to_list(instr: str) -> List[str]:
        """Convert multi-line config values to list"""
        return [line.strip() for line in instr.split("\n") if line]


if __name__ == "__main__":
    client = TemplateSetup()

    print("Python ./src template setup v1.0.0")
    print("Follow the prompts to update the template vaules.")
    print("Skip a prompt and use the default value by pressing enter.\n")

    client.update_metadata()

    print("\nChecking ./src folder for modules and updating [coverage:run]...")
    if client.update_coverage():
        print("Updates to [coverage:run] completed.")
    else:
        print("No changes for [coverage:run] needed.")

    client.save_config()
    print("\nSetup completed and values saved. You can run this again anytime.\n\n")
