import unittest

from billing import calculate_invoice_total


class TestInvoiceTotal(unittest.TestCase):
    def test_normal_invoice(self):
        items = [{"name": "Keyboard", "price": 50.00, "quantity": 2}]
        self.assertEqual(calculate_invoice_total(items, 10), 90.00)

    def test_zero_discount(self):
        items = [{"name": "Mouse", "price": 25.00, "quantity": 3}]
        self.assertEqual(calculate_invoice_total(items, 0), 75.00)

    def test_multiple_items(self):
        items = [
            {"name": "Keyboard", "price": 50.00, "quantity": 2},
            {"name": "Mouse", "price": 25.00, "quantity": 1},
            {"name": "Monitor", "price": 200.00, "quantity": 1},
        ]
        self.assertEqual(calculate_invoice_total(items, 10), 292.50)


if __name__ == "__main__":
    unittest.main()
