"""
Unit tests for coffee_shop.py

Run with:
    pytest
"""

import os
import sys

# Allow tests to import coffee_shop.py from the project root
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from coffee_shop import Coffee, Order


# ---------------------------------------------------------------------------
# Coffee
# ---------------------------------------------------------------------------

def test_coffee_stores_name_and_price():
    coffee = Coffee("Latte", 3.50)
    assert coffee.name == "Latte"
    assert coffee.price == 3.50


# ---------------------------------------------------------------------------
# Order.add_order
# ---------------------------------------------------------------------------

def test_add_order_appends_item():
    order = Order()
    coffee = Coffee("Espresso", 2.50)

    order.add_order(coffee)

    assert order.items == [coffee]


def test_add_order_multiple_items():
    order = Order()
    espresso = Coffee("Espresso", 2.50)
    latte = Coffee("Latte", 3.50)

    order.add_order(espresso)
    order.add_order(latte)

    assert order.items == [espresso, latte]


# ---------------------------------------------------------------------------
# Order.total
# ---------------------------------------------------------------------------

def test_total_is_zero_for_empty_order():
    order = Order()
    assert order.total() == 0


def test_total_sums_item_prices():
    order = Order()
    order.add_order(Coffee("Espresso", 2.50))
    order.add_order(Coffee("Mocha", 4.00))

    assert order.total() == pytest.approx(6.50)


# ---------------------------------------------------------------------------
# Order.show_order
# ---------------------------------------------------------------------------

def test_show_order_empty_cart_prints_message(capsys):
    order = Order()
    order.show_order()

    captured = capsys.readouterr()
    assert "empty" in captured.out.lower()


def test_show_order_lists_items_and_total(capsys):
    order = Order()
    order.add_order(Coffee("Espresso", 2.50))

    order.show_order()
    captured = capsys.readouterr()

    assert "Espresso" in captured.out
    assert "2.50" in captured.out
    assert "Total" in captured.out


# ---------------------------------------------------------------------------
# Order.checkout
# ---------------------------------------------------------------------------

def test_checkout_empty_cart_prints_message(capsys):
    order = Order()
    order.checkout()

    captured = capsys.readouterr()
    assert "empty" in captured.out.lower()


def test_checkout_confirmed_clears_cart(monkeypatch, capsys):
    order = Order()
    order.add_order(Coffee("Espresso", 2.50))

    monkeypatch.setattr("builtins.input", lambda _: "yes")
    order.checkout()

    captured = capsys.readouterr()
    assert "completed" in captured.out.lower()
    assert order.items == []


def test_checkout_cancelled_keeps_cart(monkeypatch, capsys):
    order = Order()
    order.add_order(Coffee("Espresso", 2.50))

    monkeypatch.setattr("builtins.input", lambda _: "no")
    order.checkout()

    captured = capsys.readouterr()
    assert "cancelled" in captured.out.lower()
    assert len(order.items) == 1
