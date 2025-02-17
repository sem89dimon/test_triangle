import pytest
from page import Triangle_Page


class Test_Triangle:
    # def test_triangle(self, driver):
    #     page = Triangle_Page(driver)
    #     page.open()
    #     page.enter_sides()

    @pytest.mark.parametrize(
        "side_a, side_b, side_c, expected_result",
        [
            ("3", "4", "5", "Это прямоугольный треугольник."),  # Пример успешного теста
            ("4", "5", "6", "Это остроугольный треугольник."),
            ("0", "4", "5", "Incorrect"),  # Пример неудачного теста
            ("3", "4", "6", "Incorrect"),
            # Добавьте остальные тесты здесь
        ],
    )
    def test_triangle_page(self,driver, side_a, side_b, side_c, expected_result):
        page = Triangle_Page(driver)
        page.open()
        page.enter_sides(side_a, side_b, side_c)

        info = self.element_is_visible(self.info, timeout=5).text
        print(info)
        assert expected_result == info
