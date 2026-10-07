"""Thin startup code; the CLI's behavior is tested through main()."""
from calculator.cli import main

# This only starts the tested main function; there is no extra logic to test.
if __name__ == "__main__":  # pragma: no cover
    main()
