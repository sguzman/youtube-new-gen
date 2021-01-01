import logging
import os
import typing


def get_env(env: str) -> str:
    logging.info(f'Retrieving {env}')
    env_val: str = os.environ[env]

    logging.info(f'Found value "{env_val}"')
    return env_val


def get_env_no_empty(env: str) -> str:
    logging.info(f'Retrieving {env}')
    env_val: str = os.environ[env]

    if len(env_val) == 0:
        logging.error(f'No value found for {env}')
        raise LookupError
    else:
        logging.info(f'Found value "{env_val}"')
        return env_val


def get_env_optional(env: str) -> typing.Optional[str]:
    logging.info(f'Retrieving {env}')
    env_val: str = os.environ[env]

    logging.info(f'Found value "{env_val}"')
    if len(env_val) == 0:
        return None
    else:
        return env_val
