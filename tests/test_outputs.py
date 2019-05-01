try:
    from contextlib import redirect_stdout
except:
    pass

import io
import sys

import pytest

from patterns.behavioral.publish_subscribe import main as publish_subscribe_main
from patterns.behavioral.publish_subscribe import OUTPUT as publish_subscribe_output
from patterns.behavioral.specification import main as specification_main
from patterns.behavioral.specification import OUTPUT as specification_output
from patterns.behavioral.state import main as state_main
from patterns.behavioral.state import OUTPUT as state_output


@pytest.mark.skipif(sys.version_info < (3,4),
                    reason="requires python3.4 or higher")
@pytest.mark.parametrize("main,output", [
    (publish_subscribe_main, publish_subscribe_output),
    (specification_main, specification_output),
    (state_main, state_output),
])
def test_output(main, output):
    f = io.StringIO()
    with redirect_stdout(f):
        main()

    real_output = f.getvalue().strip()
    expected_output = output.strip()
    assert real_output == expected_output
