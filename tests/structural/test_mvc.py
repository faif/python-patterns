import pytest

from patterns.structural.mvc import (
    ProductModel,
    ConsoleView,
    Controller,
    Router,
)


def test_productmodel_iteration_and_price_str():
    pm = ProductModel()
    items = list(pm)
    assert set(items) == {"milk", "eggs", "cheese"}

    info = pm.get("cheese")
    assert info["quantity"] == 10
    assert str(info["price"]) == "2.00"


def test_productmodel_get_raises_keyerror():
    pm = ProductModel()
    with pytest.raises(KeyError) as exc:
        pm.get("unknown_item")
    assert "not in the model's item list." in str(exc.value)


def test_consoleview_capitalizer_and_list_and_info(capsys):
    view = ConsoleView()
    # capitalizer
    assert view.capitalizer("heLLo") == "Hello"

    # show item list
    view.show_item_list("product", ["x", "y"])
    out = capsys.readouterr().out
    assert "PRODUCT LIST:" in out
    assert "x" in out and "y" in out

    # show item information formatting
    pm = ProductModel()
    controller = Controller(pm, view)
    controller.show_item_information("milk")
    out = capsys.readouterr().out
    assert "PRODUCT INFORMATION:" in out
    assert "Name: milk" in out
    assert "Price: 1.50" in out
    assert "Quantity: 10" in out


def test_show_item_information_missing_calls_item_not_found(capsys):
    view = ConsoleView()
    pm = ProductModel()
    controller = Controller(pm, view)

    controller.show_item_information("arepas")
    out = capsys.readouterr().out
    assert 'That product "arepas" does not exist in the records' in out


def test_router_register_resolve_and_unknown():
    router = Router()
    router.register("products", Controller, ProductModel, ConsoleView)
    controller = router.resolve("products")
    assert isinstance(controller, Controller)

    with pytest.raises(KeyError):
        router.resolve("no-such-path")
