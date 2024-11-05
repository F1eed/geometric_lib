import unittest
import circle
import rectangle
import square
import triangle


class MyTestCase(unittest.TestCase):
    # тесты, где параметр равен нулю
    def test_circle_area_parametr_zero(self):
        self.assertEqual(circle.area(0), 0)
    def test_circle_perimeter_parametr_zero(self):
        self.assertEqual(circle.perimeter(0), 0)
    def test_rectangle_area_second_parametr_zero(self):
        self.assertEqual(rectangle.area(5, 0), 0)
    def test_rectangle_area_first_parametr_zero(self):
        self.assertEqual(rectangle.area(0, 5), 0)
    def test_rectangle_perimeter_first_parametr_zero(self):
        self.assertEqual(rectangle.perimeter(0, 5), 10)
    def test_rectangle_perimeter_second_parametr_zero(self):
        self.assertEqual(rectangle.perimeter(5, 0), 10)
    def test_square_area_parametr_zero(self):
        self.assertEqual(square.area(0), 0)
    def test_square_perimeter_parametr_zero(self):
        self.assertEqual(square.perimeter(0), 0)
    def test_triangle_area_second_parametr_zero(self):
        self.assertEqual(triangle.area(10, 0), 0)
    def test_triangle_area_first_parametr_zero(self):
        self.assertEqual(triangle.area(0, 10), 0)
    def test_triangle_perimeter_first_parametr_zero(self):
        self.assertEqual(triangle.perimeter(0, 10, 29), 39)
    def test_triangle_perimeter_first_and_second_parametrs_zero(self):
        self.assertEqual(triangle.perimeter(0, 0, 29), 29)
    def test_triangle_perimeter_all_parametrs_zero(self):
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)

    # обработка на неправильный тип в аргументах
    def test_circle_area_invalid_types_string(self):
        with self.assertRaises(TypeError):
            circle.area("5")
    def test_circle_perimeter_invalid_types_string(self):
        with self.assertRaises(TypeError):
            circle.perimeter("5")
    def test_rectangle_perimeter_first_parametr_invalid_types_string(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter("5", 0)
    def test_rectangle_perimeter_second_parametr_invalid_types_string(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter(0, "5")
    def test_rectangle_perimeter_all_parametrs_invalid_types_string(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter("5", "5")
    def test_rectangle_area_first_parametr_invalid_types_string(self):
        with self.assertRaises(TypeError):
            rectangle.area("5", 0)
    def test_rectangle_area_second_parametr_invalid_types_string(self):
        with self.assertRaises(TypeError):
            rectangle.area(5, "5")
    def test_rectangle_area_all_parametrs_invalid_types_string(self):
        with self.assertRaises(TypeError):
            rectangle.area("5", "5")
    def test_square_area_invalid_types_string(self):
        with self.assertRaises(TypeError):
            square.area("5")
    def test_square_perimeter_invalid_types_string(self):
        with self.assertRaises(TypeError):
            square.perimeter("5")
    def test_triangle_area_first_parametr_invalid_types_string(self):
        with self.assertRaises(TypeError):
            triangle.area("5", 0)
    def test_triangle_area_second_parametr_invalid_types_string(self):
        with self.assertRaises(TypeError):
            triangle.area(0, "5")
    def test_triangle_area_all_parametrs_invalid_types_string(self):
        with self.assertRaises(TypeError):
            triangle.area("5", "5")
    def test_triangle_perimeter_first_parametr_invalid_types_string(self):
        with self.assertRaises(TypeError):
            triangle.perimeter("5", 0, 0)
    def test_triangle_perimeter_second_parametr_invalid_types_string(self):
        with self.assertRaises(TypeError):
            triangle.perimeter(0, "5", 0)
    def test_triangle_perimeter_all_parametrs_invalid_types_string(self):
        with self.assertRaises(TypeError):
            triangle.perimeter("5", "5", "5")
    def test_triangle_perimeter_first_and_second_parametrs_invalid_types_string(self):
        with self.assertRaises(TypeError):
            triangle.perimeter("5", "5", 0)
    def test_triangle_perimeter_second_and_third_parametrs_invalid_types_string(self):
        with self.assertRaises(TypeError):
            triangle.perimeter(0, "5", "5")
    def test_triangle_perimeter_third_parametr_invalid_types_string(self):
        with self.assertRaises(TypeError):
            triangle.perimeter(0, 0, "5")
    def test_triangle_perimeter_first_and_third_parametrs_invalid_types_string(self):
        with self.assertRaises(TypeError):
            triangle.perimeter("5", 0, "5")
    def test_circle_area_invalid_types_list(self):
        with self.assertRaises(TypeError):
            circle.area([5])
    def test_circle_perimeter_invalid_types_list(self):
        with self.assertRaises(TypeError):
            circle.perimeter([5])
    def test_rectangle_perimeter_first_parametr_invalid_types_list(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter([5], 0)
    def test_rectangle_perimeter_second_parametr_invalid_types_list(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter(0, [5])
    def test_rectangle_perimeter_all_parametrs_invalid_types_list(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter([5], [5])
    def test_rectangle_area_first_parametr_invalid_types_list(self):
        with self.assertRaises(TypeError):
            rectangle.area([5], 0)
    def test_rectangle_area_second_parametr_invalid_types_list(self):
        with self.assertRaises(TypeError):
            rectangle.area(5, [5])
    def test_rectangle_area_all_parametrs_invalid_types_list(self):
        with self.assertRaises(TypeError):
            rectangle.area([5], [5])
    def test_square_area_invalid_types_list(self):
        with self.assertRaises(TypeError):
            square.area([5])
    def test_square_perimeter_invalid_types_list(self):
        with self.assertRaises(TypeError):
            square.perimeter([5])
    def test_triangle_area_first_parametr_invalid_types_list(self):
        with self.assertRaises(TypeError):
            triangle.area([5], 0)
    def test_triangle_area_second_parametr_invalid_types_list(self):
        with self.assertRaises(TypeError):
            triangle.area(0, [5])
    def test_triangle_area_all_parametrs_invalid_types_list(self):
        with self.assertRaises(TypeError):
            triangle.area([5], [5])
    def test_triangle_perimeter_first_parametr_invalid_types_list(self):
        with self.assertRaises(TypeError):
            triangle.perimeter([5], 0, 0)
    def test_triangle_perimeter_second_parametr_invalid_types_list(self):
        with self.assertRaises(TypeError):
            triangle.perimeter(0, [5], 0)
    def test_triangle_perimeter_all_parametrs_invalid_types_list(self):
        with self.assertRaises(TypeError):
            triangle.perimeter([5], [5], [5])
    def test_triangle_perimeter_first_and_second_parametrs_invalid_types_list(self):
        with self.assertRaises(TypeError):
            triangle.perimeter([5], [5], 0)
    def test_triangle_perimeter_second_and_third_parametrs_invalid_types_list(self):
        with self.assertRaises(TypeError):
            triangle.perimeter(0, [5], [5])
    def test_triangle_perimeter_third_parametr_invalid_types_list(self):
        with self.assertRaises(TypeError):
            triangle.perimeter(0, 0, [5])
    def test_triangle_perimeter_first_and_third_parametrs_invalid_types_list(self):
        with self.assertRaises(TypeError):
            triangle.perimeter([5], 0, [5])

    #тесты не негативные числа
    def test_circle_area_negative_numbers(self):
        with self.assertRaises(ValueError):
            circle.area(-5)
    def test_circle_perimeter_negative_numbers(self):
        with self.assertRaises(ValueError):
            circle.perimeter(-5)
    def test_rectangle_perimeter_first_argument_negative_numbers(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(-5, 0)
    def test_rectangle_perimeter_both_arguments_negative_numbers(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(-5, -5)
    def test_rectangle_perimeter_second_argument_negative_numbers(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(0, -5)
    def test_rectangle_area_first_argument_negative_numbers(self):
        with self.assertRaises(ValueError):
            rectangle.area(-5,0)
    def test_rectangle_area_both_arguments_negative_numbers(self):
        with self.assertRaises(ValueError):
            rectangle.area(-5,-5)
    def test_rectangle_area_second_argument_negative_numbers(self):
        with self.assertRaises(ValueError):
            rectangle.area(0, -5)
    def test_square_area_negative_numbers(self):
        with self.assertRaises(ValueError):
            square.area(-5)
    def test_square_perimeter_negative_numbers(self):
        with self.assertRaises(ValueError):
            square.perimeter(-5)
    def test_triangle_perimeter_all_arguments_negative_numbers(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(-5, -5, -5)
    def test_triangle_perimeter_first_and_second_arguments_negative_numbers(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(-5, -5, 0)
    def test_triangle_perimeter_first_argument_negative_numbers(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(-5, 0, 0)
    def test_triangle_perimeter_first_and_third_arguments_negative_numbers(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(-5, 0, -5)
    def test_triangle_perimeter_third_argument_negative_numbers(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(0, 0, -5)
    def test_triangle_perimeter_second_and_third_arguments_negative_numbers(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(0, -5, -5)
    def test_triangle_perimeter_second_argument_negative_numbers(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(0, -5, 0)



if __name__ == '__main__':
    unittest.main()
