import yaml
import argparse
from pint import UnitRegistry

def read_yaml(file_path):
    with open(file_path, "r") as file:
        return yaml.safe_load(file)


def format_header_define(key, value):
    return f"#define {key} {value}"

def recurse_config_key(config, begin_key=""):
	for key, value in config.items():
		if isinstance(value, dict):
			recurse_config_key(value, f"{begin_key}_{key}")
		elif isinstance(value, list):
			for item in value:
				if isinstance(item, dict):
					recurse_config_key(item, f"{begin_key}_{key}")
		else:
			print(format_header_define(f"{begin_key}_{key}".upper(), value))

def main():
    parser = argparse.ArgumentParser(
        prog="bbsxtra-programmer",
        description="A tool to compile firmware for the Bafang BBS02/BBSHD ebike motor",
    )
    parser.add_argument("filename", help="Path to the yaml configuration file")
    args = parser.parse_args()
    config = read_yaml(args.filename)
    for level_type, levels in config["pedal_assist_levels"].items():
        for index, level in enumerate(levels["levels"]):
            # Header example ASSIST_LEVEL_STANDARD_0_FLAGS
            for level_key, level_value in level.items():
                print(format_header_define(f"ASSIST_LEVEL_{level_type}_{index}_{level_key}".upper(), level_value))
            print()
    del config["pedal_assist_levels"]
    recurse_config_key(config)


if __name__ == "__main__":
    main()
