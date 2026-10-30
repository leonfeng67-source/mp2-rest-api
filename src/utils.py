import logging
import sys


def setup_logging(verbose: bool = False) -> None:
    """Configure root logging.

    NOTE: Replace this body with your MP1 setup_logging() so the
    behavior and format match exactly.
    """
    level = logging.DEBUG if verbose else logging.INFO
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(
        logging.Formatter(
            "%(asctime)s %(levelname)s %(name)s — %(message)s",
            datefmt="%H:%M:%S",
        )
    )
    root = logging.getLogger()
    root.handlers.clear()
    root.addHandler(handler)
    root.setLevel(level)
