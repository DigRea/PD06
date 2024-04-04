import pytest
from unittest.mock import patch
from io import StringIO
from use_functions import bankfunc
from victory import victory

# Этот тест проверяет функцию пополнения счета
def test_refill():
    with patch('builtins.input', side_effect=['1', '100', '4']):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            bankfunc()
            output = fake_out.getvalue().strip()
            assert "Текущая сумма:  100" in output

# Этот тест проверяет функцию покупки при недостаточном балансе
def test_purchase_with_insufficient_balance():
    with patch('builtins.input', side_effect=['2', '50', 'bread', '4']):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            bankfunc()
            output = fake_out.getvalue().strip()
            assert "Недостаточно средств!" in output

# Этот тест проверяет обработку неверного выбора пользователем пункта меню
def test_invalid_menu_choice():
    with patch('builtins.input', side_effect=['5', '4']):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            bankfunc()
            output = fake_out.getvalue().strip()
            assert "Неверный пункт меню" in output

# Этот тест проверяет корректность отображения истории покупок
def test_history():
    with patch('builtins.input', side_effect=['1', '100', '2', '50', 'bread', '3', '4']):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            bankfunc()
            output = fake_out.getvalue().strip()
            assert "('bread', 50)" in output
