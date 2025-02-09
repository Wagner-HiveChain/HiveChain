# hivechain_core.py

_config = None

def init_config(config: dict):
    """
    Initialize the library's configuration.
    Must be called once by the application before using other library functions.
    """
    global _config
    _config = config

def get_config():
    """
    Retrieve the current configuration.
    Raises an error if not initialized.
    """
    if _config is None:
        raise RuntimeError("Configuration not initialized. Please call init_config() first.")
    return _config
