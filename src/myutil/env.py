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
        err_msg: str = f'No value found for {env}'
        logging.error(err_msg)
        raise LookupError(err_msg)
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


def get_db_user() -> str:
    return get_env_no_empty('POSTGRES_USERNAME')


def get_db_pass() -> str:
    return get_env_no_empty('POSTGRES_PASSWORD')


def get_db_name() -> str:
    return get_env_no_empty('POSTGRES_DB')


def get_db_host() -> str:
    return get_env_no_empty('POSTGRES_HOST')


def get_db_port() -> str:
    return get_env_no_empty('POSTGRES_PORT')


def get_db_table() -> str:
    return get_env_no_empty('POSTGRES_TABLE')
