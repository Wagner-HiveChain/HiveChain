# hivechain_core.py
"""
Module: hivechain_core.py
Description:
  Manages the global configuration and shared state for HiveChain.
  By default, the configuration is made immutable to ensure consistency and avoid accidental modifications.
  However, an optional parameter allows disabling immutability if dynamic updates are required.
  
Keywords: singleton, global state, initialization, immutable.
"""

from types import MappingProxyType

_config = None

def init_config(config: dict, immutable: bool = True):
    """
    Initialize the library's configuration.
    Must be called once by the application before using other library functions.
    
    Args:
        config (dict): The configuration dictionary to be set as the global configuration.
        immutable (bool, optional): If True (default), the configuration will be made immutable.
                                    Set to False to allow modifications at runtime.
    """
    global _config
    if immutable:
        _config = MappingProxyType(config)
    else:
        _config = config

def get_config():
    """
    Retrieve the current configuration.
    
    Returns:
        dict: The global configuration.
    
    Raises:
        RuntimeError: If the configuration has not been initialized.
    """
    if _config is None:
        raise RuntimeError("Configuration not initialized. Please call init_config() first.")
    return _config
