import unittest
import solver


class TestSolver(unittest.TestCase):
    def test_inf_roots(self):
        self.assertEqual('3', solver.solve(0, 0, 0))

    def test_inf_roots1(self):
        self.assertEqual('0', solver.solve(0, 0, 3))

    def test_inf_roots2(self):
        self.assertEqual('1,-0.5', solver.solve(0, 2, 1))

    def test_inf_roots3(self):
        self.assertEqual('0', solver.solve(1, 2, 8))

    def test_inf_roots4(self):
        self.assertEqual('1,-1.0', solver.solve(1, 2, 1))

    def test_inf_roots5(self):
        self.assertEqual('2,-1.0,-4.0', solver.solve(1, 5, 4))




if __name__ == '__main__':
    unittest.main()
