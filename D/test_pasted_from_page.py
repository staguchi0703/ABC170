#
from resolve import resolve
####################################
####################################
# 以下にプラグインの内容をペーストする
#  
import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        print('------------')
        print(out)
        print('------------')
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """5
24 11 8 3 16"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
33 18 45 28 8 19 89 86 2 4"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
