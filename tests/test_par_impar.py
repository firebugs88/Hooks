import unittest
import sys
from pathlib import Path

# Add parent directory to path to import the module
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from par_impar import comprobar_paridad, es_impar, es_par

class TestParImpar(unittest.TestCase):

    def test_comprobar_paridad(self):
        """Test comprobar_paridad function."""
        # TODO: Implement test for comprobar_paridad
        # Example: result = comprobar_paridad(test_input)
        # self.assertEqual(result, expected_output)
        pass

    def test_es_impar(self):
        """Test es_impar function."""
        # TODO: Implement test for es_impar
        # Example: result = es_impar(test_input)
        # self.assertEqual(result, expected_output)
        pass

    def test_es_par(self):
        """Test es_par function."""
        # TODO: Implement test for es_par
        # Example: result = es_par(test_input)
        # self.assertEqual(result, expected_output)
        pass

if __name__ == '__main__':
    unittest.main()
