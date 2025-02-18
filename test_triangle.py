import pytest


class Test_Triangle:
    @pytest.mark.parametrize(
        "side_a, side_b, side_c, expected_bug_text, expected_case_text",
        [
            
            ("3", "4", "5", None, "Кейс - Прямоугольный треугольник"),
            ("4", "5", "6", None, "Кейс - Остроугольный треугольник"),
            ("5", "5", "5", None, "Кейс - Равносторонний треугольник"),
            ("3", "4", "6", None, "Кейс - Тупоугольный треугольник"),

            
            ("3", "0", "5.5", None, "Баг - Форма неправильно работает с нецелыми числами."),
            ("select *", "4", "0", None, "Баг - Попробовали SQL-инъекцию"),
            ("0", "0", "0", None, "Баг - Все нули - не равносторонний треугольник."),
            ("<SCRIPT>", "1", "1", None, "Баг - Вы нашли XSS."),
            
            
            ("", "4", "5", None, "Кейс - Не все поля заданы"),
            ("", "", "", None, "Кейс - Все поля пустые"),
            ("3", "4", "", None, "Баг - Форма не валидирует поле C."),
            
            
            ("0", "4", "5", None, "Кейс - Не выполнились условия треугольника"),
            ("365146484", "487878564", "659595959", None, "Кейс - Попробовали большие числа"),
            ("<script>", "5", "5", None, "Кейс - Попробовали XSS"),
            ("2", "-2", "7", None, "Кейс - "),
        ]
    )
    def test_triangle_page(self, triangle_page, side_a, side_b, side_c, expected_bug_text, expected_case_text):
        page = triangle_page
        
        page.enter_sides(side_a, side_b, side_c)

        if expected_bug_text:
            bug_elements = page.elements_are_visible(page.bug_logg, timeout=5)
            
            assert bug_elements, f"Не найден ожидаемый баг с текстом: '{expected_bug_text}'"
        
        if expected_case_text:
            case_elements = page.elements_are_visible(page.case_logg, timeout=5)
           
            assert case_elements, f"Не найден ожидаемый кейс с текстом: '{expected_case_text}'"
