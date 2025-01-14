from general.utils.collections import deep_update
from general.utils.settings import get_settings_from_environment

deep_update(globals(), get_settings_from_environment(ENVVAR_SETTINGS_PREFIX, BASE_DIR))  # type: ignore # noqa: F821
