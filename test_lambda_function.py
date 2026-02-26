import unittest

from lambda_function import lambda_handler


class LambdaHandlerTests(unittest.TestCase):
    def test_handler_with_name(self):
        result = lambda_handler({"name": "Lmbda"}, None)
        self.assertEqual(result["statusCode"], 200)
        self.assertEqual(result["body"]["message"], "Hello, Lmbda!")

    def test_handler_without_name(self):
        result = lambda_handler({}, None)
        self.assertEqual(result["statusCode"], 200)
        self.assertEqual(result["body"]["message"], "Hello, World!")


if __name__ == "__main__":
    unittest.main()
