import os

from dotenv import load_dotenv, dotenv_values

from .misc import yaml_coerce


def get_settings_from_environment(prefix, BASE_DIR):
	prefix_len = len(prefix)
	envs = {key[prefix_len:]: yaml_coerce(value) for key, value in os.environ.items() if key.startswith(prefix)}

	dot_env_file = dotenv_values(BASE_DIR / '.env')
	envs.update(dot_env_file)

	return envs
