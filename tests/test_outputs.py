try:
    from contextlib import redirect_stdout
except:
    pass

import io
import sys

import pytest

from behavioral.visitor import main as visitor_main
from behavioral.visitor import OUTPUT as visitor_output
from behavioral.strategy import main as strategy_main
from behavioral.strategy import OUTPUT as strategy_output

@pytest.mark.skipif(sys.version_info < (3,4),
                    reason="requires python3.4 or higher")
@pytest.mark.parametrize("main,output", [
    (visitor_main, visitor_output),
    (strategy_main, strategy_output),
])
def test_output(main, output):
    f = io.StringIO()
    with redirect_stdout(f):
        main()

    real_output = f.getvalue().strip()
    expected_output = output.strip()
    assert real_output == expected_output
