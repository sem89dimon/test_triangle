import pytest
from selenium.webdriver.common.by import By


class Test_Triangle:
    @pytest.mark.parametrize(
        "side_a, side_b, side_c, expected_bug_text, expected_case_text",
        [
            # Корректные данные для разных кейсов
            ("3", "4", "5", None, "Кейс - Это прямоугольный треугольник."),
            ("4", "5", "6", None, "Кейс - Это остроугольный треугольник."),
            ("5", "5", "5", None, "Кейс - Это равносторонний треугольник."),
            ("3", "4", "6", None, "Кейс - Это тупоугольный треугольник."),

            # Поля с некорректными значениями
            ("0", "4", "5", None, "Баг - Сторона A не может быть равна 0."),
            ("3", "0", "5", None, "Баг - Сторона B не может быть равна 0."),
            ("3", "4", "0", None, "Баг - Сторона C не может быть равна 0."),
            ("0", "0", "0", None, "Баг - Все стороны не могут быть равны 0."),
            
            # Пустые поля (при проверке пустых значений, поле не должно быть отправлено или обработано)
            ("", "4", "5", None, "Кейс - Некорректные значения сторон."),
            ("3", "", "5", None, "Кейс - Некорректные значения сторон."),
            ("3", "4", "", None, "Кейс - Некорректные значения сторон."),
            
            # Ошибочные данные для остальных кейсов
            ("3", "4", "6", None, "Кейс - Некорректные значения сторон."),
            ("1", "1", "1", None, "Кейс - Некорректные значения сторон."),
            ("1", "5", "5", None, "Кейс - Некорректные значения сторон."),
            ("2", "2", "7", None, "Кейс - Некорректные значения сторон."),
        ]
    )
    def test_triangle_page(self, triangle_page, side_a, side_b, side_c, expected_bug_text, expected_case_text):
        page = triangle_page
        
        # Вводим данные в поля сторон
        page.enter_sides(side_a, side_b, side_c)

        
        # Проверка на баг
        if expected_bug_text:
            bug_elements = page.elements_are_visible((By.CSS_SELECTOR, ".bug_details .untraveled"), timeout=5)
            bug_found = False
            for bug in bug_elements:
                if expected_bug_text in bug.text:
                    bug_found = True
                    break
            assert bug_found, f"Не найден ожидаемый баг с текстом: '{expected_bug_text}'"
        
        # Проверка на кейс
        if expected_case_text:
            case_elements = page.elements_are_visible((By.CSS_SELECTOR, ".case_details .untraveled"), timeout=5)
            case_found = False
            for case in case_elements:
                if expected_case_text in case.text:
                    case_found = True
                    break
            assert case_found, f"Не найден ожидаемый кейс с текстом: '{expected_case_text}'"
