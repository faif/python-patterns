try:
    from contextlib import redirect_stdout
except:
    pass

import io
import sys

import pytest

from patterns.behavioral.catalog import main as catalog_main
from patterns.behavioral.catalog import OUTPUT as catalog_output
from patterns.behavioral.chaining_method import main as chaining_method_main
from patterns.behavioral.chaining_method import OUTPUT as chaining_method_output
from patterns.behavioral.command import main as command_main
from patterns.behavioral.command import OUTPUT as command_output
from patterns.behavioral.iterator import main as iterator_main
from patterns.behavioral.iterator import OUTPUT as iterator_output
from patterns.behavioral.mediator import main as mediator_main
from patterns.behavioral.mediator import OUTPUT as mediator_output
from patterns.behavioral.observer import main as observer_main
from patterns.behavioral.observer import OUTPUT as observer_output
from patterns.behavioral.publish_subscribe import main as publish_subscribe_main
from patterns.behavioral.publish_subscribe import OUTPUT as publish_subscribe_output
from patterns.behavioral.specification import main as specification_main
from patterns.behavioral.specification import OUTPUT as specification_output
from patterns.behavioral.state import main as state_main
from patterns.behavioral.state import OUTPUT as state_output
from patterns.behavioral.strategy import main as strategy_main
from patterns.behavioral.strategy import OUTPUT as strategy_output
from patterns.behavioral.visitor import main as visitor_main
from patterns.behavioral.visitor import OUTPUT as visitor_output


@pytest.mark.skipif(sys.version_info < (3,4),
                    reason="requires python3.4 or higher")
@pytest.mark.parametrize("main,output", [
    (catalog_main, catalog_output),
    (chaining_method_main, chaining_method_output),
    (command_main, command_output),
    (iterator_main, iterator_output),
    (mediator_main, mediator_output),
    (observer_main, observer_output),
    (publish_subscribe_main, publish_subscribe_output),
    (specification_main, specification_output),
    (state_main, state_output),
    (strategy_main, strategy_output),
    (visitor_main, visitor_output),
])
def test_output(main, output):
    f = io.StringIO()
    with redirect_stdout(f):
        main()

    real_output = f.getvalue().strip()
    expected_output = output.strip()
    assert real_output == expected_output
