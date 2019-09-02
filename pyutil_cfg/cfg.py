# -*- coding: utf-8 -*-

from configparser import SafeConfigParser
import logging
import logging.config

import pyutil_json as json


def init(name, ini_filename, log_ini_filename='', params=None):
    logger = _init_logger(name, log_ini_filename, ini_filename)
    config = _init_ini_file(name, ini_filename, logger)
    config = _post_init_config(params, config, logger)

    logger.warning('pyutil_cfg: to return: logger: %s config: %s', logger, config)

    return logger, config


def _init_logger(name, log_ini_filename, ini_filename):
    logger = logging.getLogger(name)

    if not log_ini_filename:
        log_ini_filename = ini_filename

    if not log_ini_filename:
        return None

    logging.config.fileConfig(log_ini_filename, disable_existing_loggers=False)

    return logger


def _init_ini_file(name, ini_filename, logger):
    '''
    setup rx_med_analysis:main config
    '''
    section = name + ':main'

    config = _init_ini_file_core(ini_filename, section, logger)

    return config


def _init_ini_file_core(ini_filename, section, logger):
    '''
    get ini conf from section
    return: config: {key: val} val: json_loaded
    '''
    config_parser = SafeConfigParser()
    config_parser.read(ini_filename)
    options = config_parser.options(section)
    config = {option: _init_ini_file_parse_option(option, section, config_parser, logger) for option in options}

    return config


def _init_ini_file_parse_option(option, section, config_parser, logger):
    try:
        val = config_parser.get(section, option)
    except Exception as e:
        logger.exception('unable to get option: section: %s option: %s e: %s', section, option, e)
        val = ''
    return _init_ini_file_val_to_json(option, val)


def _init_ini_file_val_to_json(option, val):
    '''
    try to do json load on value
    '''

    if val.__class__.__name__ != 'str':
        return val

    orig_v = val
    try:
        val = json.loads(val)
    except:
        val = orig_v

    if option.endswith('_set'):
        val = set(val)

    return val


def _post_init_config(params, config, logger):
    '''
    add additional parameters into config
    '''
    logger.debug('params: %s', params)

    if not params:
        logger.debug('_post_init_config: done: config: %s', config)
        return config

    for (k, v) in params.items():
        if k in config:
            logger.warning('params will be overwrite: key: %s origin: %s new: %s', k, config[k], v)

    config.update(params)

    logger.debug('_post_init_config: done: config: %s', config)

    return config
