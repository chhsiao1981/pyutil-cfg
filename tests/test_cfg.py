# -*- coding: utf-8 -*-

import unittest
import logging

from pyutil_cfg import cfg


class TestCfg(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init_no_name_filename(self):
        logger, config = cfg.init()

        assert logger is logging.root
        assert config == {}

    def test_init_simpliest(self):
        logger, config = cfg.init('test_cfg', 'tests/data/test.ini')

        assert config['a'] == 'b'
        assert config['test_ini'] == 'test2'
        assert config['test_list'] == ['test0', 'test1', 2]
        assert config['test_dict'] == {'test_key': 'test_val', 'test_key2': 'test_val2'}
        assert config['test_list_dict'] == [
            {'A': 1, 'B': 'b'},
            {'A': 2, 'B': 'c'},
            {'A': 3, 'B': 'd'},
            {'A': 4, 'B': 'e'},
        ]

    def test_init(self):
        logger, config = cfg.init(
            'test_cfg',
            'tests/data/test.ini',
            extra_params={'test_params': 'test'},
            show_config=logging.DEBUG,
        )

        assert config['a'] == 'b'
        assert config['test_params'] == 'test'
        assert config['test_ini'] == 'test2'
        assert config['test_list'] == ['test0', 'test1', 2]
        assert config['test_dict'] == {'test_key': 'test_val', 'test_key2': 'test_val2'}
        assert config['test_list_dict'] == [
            {'A': 1, 'B': 'b'},
            {'A': 2, 'B': 'c'},
            {'A': 3, 'B': 'd'},
            {'A': 4, 'B': 'e'},
        ]

    def test_ini_toml(self):
        logger, config = cfg.init(
            'test_cfg',
            'tests/data/test.toml',
            extra_params={'test_params': 'test'},
            show_config=logging.DEBUG,
        )

        assert config['a'] == 'b'
        assert config['test_params'] == 'test'
        assert config['test_ini'] == 'test2'
        assert config['test_list'] == ['test0', 'test1', 2]
        assert config['test_dict'] == {'test_key': 'test_val', 'test_key2': 'test_val2'}
        assert config['test_list_dict'] == [
            {'A': 1, 'B': 'b'},
            {'A': 2, 'B': 'c'},
            {'A': 3, 'B': 'd'},
            {'A': 4, 'B': 'e'},
        ]

    def test_init_no_show_config_because_setting_info_in_config(self):
        logger, config = cfg.init(
            'test_cfg',
            'tests/data/test_no_show_config_because_setting_info_in_config.ini',
            extra_params={'test_params': 'test'},
            show_config=logging.DEBUG,
        )

        assert config['a'] == 'b'
        assert config['test_params'] == 'test'
        assert config['test_ini'] == 'test2'
        assert config['test_list'] == ['test0', 'test1', 2]
        assert config['test_dict'] == {'test_key': 'test_val', 'test_key2': 'test_val2'}
        assert config['test_list_dict'] == [
            {'A': 1, 'B': 'b'},
            {'A': 2, 'B': 'c'},
            {'A': 3, 'B': 'd'},
            {'A': 4, 'B': 'e'},
        ]

    def test_init_no_disale_existing_loggers(self):
        logger, config = cfg.init(
            'test_cfg',
            'tests/data/test_no_disable_existing_loggers.ini',
            extra_params={'test_params': 'test'},
        )

        assert config['a'] == 'b'
        assert config['test_params'] == 'test'
        assert config['test_ini'] == 'test2'
        assert config['test_list'] == ['test0', 'test1', 2]
        assert config['test_dict'] == {'test_key': 'test_val', 'test_key2': 'test_val2'}
        assert config['test_list_dict'] == [
            {'A': 1, 'B': 'b'},
            {'A': 2, 'B': 'c'},
            {'A': 3, 'B': 'd'},
            {'A': 4, 'B': 'e'},
        ]

    def test_init_none(self):
        logger, config = cfg.init(
            'test_cfg',
            'tests/data/test_none.ini',
            extra_params={'test_params': 'test'},
        )

        assert isinstance(config, dict)
        assert config['test_params'] == 'test'

    def test_init_no_logger(self):
        logger, config = cfg.init(
            'test_cfg',
            'tests/data/test_no_logger.ini',
            extra_params={'test_params': 'test'},
        )

        assert config['a'] == 'b'
        assert config['test_params'] == 'test'
        assert config['test_ini'] == 'test2'
        assert config['test_list'] == ['test0', 'test1', 2]
        assert config['test_dict'] == {'test_key': 'test_val', 'test_key2': 'test_val2'}

    def test_init_no_formatter(self):
        logger, config = cfg.init(
            'test_cfg',
            'tests/data/test_no_formatter.ini',
            extra_params={'test_params': 'test'},
        )

        assert config['a'] == 'b'
        assert config['test_params'] == 'test'
        assert config['test_ini'] == 'test2'
        assert config['test_list'] == ['test0', 'test1', 2]
        assert config['test_dict'] == {'test_key': 'test_val', 'test_key2': 'test_val2'}

    def test_init_not_is_extra_in_file_ok(self):
        logger, config = cfg.init(
            'test_cfg',
            'tests/data/test.ini',
            extra_params={'test_list_dict': 'test'},
            show_config=logging.DEBUG,
            is_extra_params_in_file_ok=False,
        )

        assert config['a'] == 'b'
        assert config['test_ini'] == 'test2'
        assert config['test_list'] == ['test0', 'test1', 2]
        assert config['test_dict'] == {'test_key': 'test_val', 'test_key2': 'test_val2'}
        assert config['test_list_dict'] == 'test'

    def test_init_with_default(self):
        logger, config = cfg.init(
            'test_cfg',
            'tests/data/test.ini',
            default_params={'test_default': 'test-default', 'a': 'c', 'test_ini': 'test'},
            extra_params={'test_list_dict': 'test'},
        )

        assert config['a'] == 'b'
        assert config['test_ini'] == 'test2'
        assert config['test_list'] == ['test0', 'test1', 2]
        assert config['test_dict'] == {'test_key': 'test_val', 'test_key2': 'test_val2'}
        assert config['test_list_dict'] == 'test'
        assert config['test_default'] == 'test-default'

    def test_init_with_default_not_is_extra_in_file_ok(self):
        logger, config = cfg.init(
            'test_cfg',
            'tests/data/test.ini',
            default_params={'test_default': 'test-default', 'a': 'c', 'test_list': ['test3']},
            extra_params={'test_list_dict': 'test'},
            is_extra_params_in_file_ok=False,
        )

        assert config['a'] == 'b'
        assert config['test_ini'] == 'test2'
        assert config['test_list'] == ['test0', 'test1', 2]
        assert config['test_dict'] == {'test_key': 'test_val', 'test_key2': 'test_val2'}
        assert config['test_list_dict'] == 'test'
        assert config['test_default'] == 'test-default'

    def test_init_with_default_is_skip_extra_params_in_file(self):
        logger, config = cfg.init(
            'test_cfg',
            'tests/data/test.ini',
            default_params={'test_default': 'test-default', 'a': 'c', 'test_list': ['test3']},
            extra_params={'test_list_dict': 'test', 'test_ini': 'test3', 'test_ini3': 'test3'},
            is_skip_extra_params_in_file=True,
        )

        assert config['a'] == 'b'
        assert config['test_ini'] == 'test2'
        assert config['test_list'] == ['test0', 'test1', 2]
        assert config['test_dict'] == {'test_key': 'test_val', 'test_key2': 'test_val2'}
        assert config['test_list_dict'] == [
            {'A': 1, 'B': 'b'},
            {'A': 2, 'B': 'c'},
            {'A': 3, 'B': 'd'},
            {'A': 4, 'B': 'e'},
        ]
        assert config['test_default'] == 'test-default'
        assert config['test_ini3'] == 'test3'

    def test_init_with_default_list_dict_and_different_types(self):
        logger, config = cfg.init(
            'test_cfg',
            'tests/data/test.ini',
            default_params={
                'test_default': 'test-default',
                'a': 'c',
                'test_list': 'test3',
                'test_list_dict': [1, 2, 3, 4],
            },
            extra_params={'test_list_dict': 'test', 'test_ini': 'test3', 'test_ini3': 'test3'},
            is_skip_extra_params_in_file=True,
        )

        assert config['a'] == 'b'
        assert config['test_ini'] == 'test2'
        assert config['test_list'] == ['test0', 'test1', 2]
        assert config['test_dict'] == {'test_key': 'test_val', 'test_key2': 'test_val2'}
        assert config['test_list_dict'] == [
            {'A': 1, 'B': 'b'},
            {'A': 2, 'B': 'c'},
            {'A': 3, 'B': 'd'},
            {'A': 4, 'B': 'e'},
        ]
        assert config['test_default'] == 'test-default'
        assert config['test_ini3'] == 'test3'

    def test_init_with_extra_list_dict_and_different_types(self):
        logger, config = cfg.init(
            'test_cfg',
            'tests/data/test.ini',
            default_params={
                'test_default': 'test-default',
                'a': 'c',
                'test_list': 'test3',
                'test_list_dict': [1, 2, 3, 4],
            },
            extra_params={'test_list_dict': [
                1,
                2,
                3,
                4,
                5,
            ], 'test_ini': 'test3', 'test_ini3': 'test3'},
            is_skip_extra_params_in_file=True,
            show_config=logging.INFO,
        )

        assert config['a'] == 'b'
        assert config['test_ini'] == 'test2'
        assert config['test_list'] == ['test0', 'test1', 2]
        assert config['test_dict'] == {'test_key': 'test_val', 'test_key2': 'test_val2'}
        assert config['test_list_dict'] == [
            {'A': 1, 'B': 'b'},
            {'A': 2, 'B': 'c'},
            {'A': 3, 'B': 'd'},
            {'A': 4, 'B': 'e'},
            5,
        ]
        assert config['test_default'] == 'test-default'
        assert config['test_ini3'] == 'test3'
