import pytest

from patterns.behavioral.null_object import Customer, NullCustomer, CustomerRepository


@pytest.fixture
def repository():
    return CustomerRepository()


@pytest.fixture
def real_customer():
    return Customer("Ahmed", "ahmed@example.com")


@pytest.fixture
def null_customer():
    return NullCustomer()


# --- Customer Tests ---


def test_customer_is_not_null(real_customer):
    assert real_customer.is_null() is False


def test_customer_has_correct_name(real_customer):
    assert real_customer.name == "Ahmed"


def test_customer_has_correct_email(real_customer):
    assert real_customer.email == "ahmed@example.com"


def test_customer_send_notification(real_customer, capsys):
    real_customer.send_notification("Hello")
    captured = capsys.readouterr()
    assert "Sending 'Hello' to Ahmed at ahmed@example.com" in captured.out


# --- NullCustomer Tests ---


def test_null_customer_is_null(null_customer):
    assert null_customer.is_null() is True


def test_null_customer_has_default_name(null_customer):
    assert null_customer.name == "N/A"


def test_null_customer_has_default_email(null_customer):
    assert null_customer.email == "N/A"


def test_null_customer_send_notification_does_nothing(null_customer, capsys):
    null_customer.send_notification("Hello")
    captured = capsys.readouterr()
    assert captured.out == ""


# --- Repository Tests ---


def test_repository_returns_real_customer(repository):
    customer = repository.get_customer(1)
    assert customer.is_null() is False
    assert customer.name == "Ahmed"


def test_repository_returns_null_for_missing(repository):
    customer = repository.get_customer(999)
    assert customer.is_null() is True


def test_repository_null_customer_is_safe(repository):
    customer = repository.get_customer(999)
    customer.send_notification("Test")  # Should not raise any exception


def test_loop_over_mixed_customers(repository, capsys):
    for customer_id in [1, 2, 999]:
        repository.get_customer(customer_id).send_notification("Hi")
    captured = capsys.readouterr()
    assert "Ahmed" in captured.out
    assert "Sara" in captured.out
    assert captured.out.count("Sending") == 2  # Only 2 real customers