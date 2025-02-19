import pytest
import allure


class Test_Triangle:
    @pytest.mark.parametrize(
        "side_a, side_b, side_c, expected_bug_text, expected_case_text",
        [
            
            ("3", "4", "5", None, "Кейс - Прямоугольный треугольник"),
            ("4", "5", "6", None, "Кейс - Остроугольный треугольник"),
            ("5", "5", "5", None, "Кейс - Равносторонний треугольник"),
            ("3", "4", "6", None, "Кейс - Тупоугольный треугольник"),

            ("3", "4", "5.5", "Баг - Форма неправильно работает с нецелыми числами.", None),
            ("3", "4", "", "Баг - Форма не валидирует поле C.", None),
            ("0", "0", "0", "Баг - Все нули - не равносторонний треугольник.", None),
            ("<SCRIPT>", "1", "1", "Баг - Вы нашли XSS.", None),
                   
            ("select *", "4", "0", None, "Кейс - Попробовали SQL-инъекцию"),
            ("", "4", "5", None, "Кейс - Не все поля заданы"),
            ("", "", "", None, "Кейс - Все поля пустые"),                    
            ("0", "4", "5", None, "Кейс - Не выполнились условия треугольника"),
            ("365146484", "487878564", "659595959", None, "Кейс - Попробовали большие числа"),
            ("<script>", "5", "5", None, "Кейс - Попробовали XSS"),
            ("2", "-2", "3", None, "Кейс - Это не треугольник"),
        ]
    )
    @allure.title("Тестирование страницы треугольников")
    def test_triangle_page(self, triangle_page, side_a, side_b, side_c, expected_bug_text, expected_case_text):
        page = triangle_page
        
        with allure.step(f"Вводим данные в поля сторон: {side_a}, {side_b}, {side_c}"):
            page.enter_sides(side_a, side_b, side_c)

        if expected_bug_text:
            with allure.step(f"Проверка наличия ожидаемого результата: {expected_bug_text}"):
                bug_elements = page.elements_are_visible(page.bug_logg, timeout=5)    
                assert bug_elements, f"Не найден ожидаемый баг с текстом: '{expected_bug_text}'"
        
        if expected_case_text:
            with allure.step(f"Проверка наличия ожидаемого результата: {expected_case_text}"):
                case_elements = page.elements_are_visible(page.case_logg, timeout=5)            
                assert case_elements, f"Не найден ожидаемый кейс с текстом: '{expected_case_text}'"
