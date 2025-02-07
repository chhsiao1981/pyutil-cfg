# pyutil-cfg

python utilility for configurations.

This package helps parsing `.toml` configurations and `json`-like configurations in `.ini`.


# Usage

    import pyutil_cfg as cfg

    logger, config = cfg.init(name, filename)


# File Formats

### `.toml`
For the `.toml` files, the format follows [TOML](https://toml.io/en/) specification.

You can check [production.tmpl.toml](https://github.com/chhsiao1981/pyutil-cfg/blob/main/production.tmpl.toml) for more details.

### `.ini`
For the `.ini` files, you can check [production.tmpl.ini](https://github.com/chhsiao1981/pyutil-cfg/blob/main/production.tmpl.ini) for more details.

Assume that you have the following `development.ini`:

    [demo]
    VAR_INT = 1
    VAR_BOOL = true
    VAR_DICT = {"A": 1, "B": "a"}
    VAR_LIST = [
        {"A": 2, "B": "b"},
        {"A": 3, "B": "c"},
        {"A": 4, "B": "d"}]

Then with the following code:

    import pyutil_cfg as cfg

    logger, config = cfg.init('demo', 'development.ini')

`logger` is a [logger](https://docs.python.org/3/library/logging.html) with `name = 'demo'`

`config` ia as follow:

    config = {
        "VAR_INT": 1,
        "VAR_BOOL": true,
        "VAR_DICT": {"A": 1, "B": "a"},
        "VAR_LIST": [
            {"A": 2, "B": "b"},
            {"A": 3, "B": "c"},
            {"A": 4, "B": "d"}
        ],
    }

# Advanced Usage

## Separated log configuration filename

    import pyutil_cfg as cfg


    logger, config = cfg.init(name, filename, log_name, log_filename)

## Additional customized config parameters (specified as dict)

    import pyutil_cfg as cfg

    extra_params = {}

    logger, config = cfg.init(name, filename, extra_params=extra_params)

## Ok if extra parameters are already in the configuration file (default: `True`)

It is usual that we would like to temporarily change the configuration settings through command-line variables.

Because usually we still want to continue the process even if the extra parmeters
are accidentally in the configuration file.
Only warning logs if this parameter is set as `False` and some extra parameters are already in configuration file.

    import pyutil_cfg as cfg

    logger, config = cfg.init(name, filename, is_extra_params_in_file_ok=True)

## Skip extra parameters if they are already in the configuration file.

Skip extram parameters if they are already in the configuration file.

    import pyutil_cfg as cfg

    logger, config = cfg.init(name, filename, is_skip_extra_params_in_file=True)

## Show configuration before returning.

Setup the log-level to show the computed configurations before return.
None as no-show.

Do not show the configuration before return.
```
import pyutil_cfg as cfg

logger, config = cfg.init(name, filename)
```

Show the configruration if the logger is set to `logging.DEBUG`
```
import pyutil_cfg as cfg

logger, config = cfg.init(name, filename, show_config=logging.DEBUG)
```

Show the configuration if the logger is set to `logging.INFO` or `logging.DEBUG`.
```
import pyutil_cfg as cfg

logger, config = cfg.init(name, filename, show_config=logging.INFO)
```

# Misc

* Reason not including .json: not a good file format for config.
* Reason not including .yaml: not the standard library.
