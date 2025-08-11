import json
import sys
import ast
from pathlib import Path

def extract_functions_and_classes(file_path):
    '''Extract function and class definitions from a Python file.'''
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tree = ast.parse(content)
        functions = []
        classes = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and not node.name.startswith('_'):
                functions.append(node.name)
            elif isinstance(node, ast.ClassDef):
                classes.append(node.name)
                
        return sorted(functions), sorted(classes)
    except Exception:
        return [], []

def generate_test_content(module_name, functions, classes):
    '''Generate test file content.'''
    test_content = f'''import unittest
import sys
from pathlib import Path

# Add parent directory to path to import the module
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
'''

    imports_to_add = functions + classes
    if not imports_to_add:
        import_line = f"import {module_name}"
    else:
        # Create a clean import line, handling potential line length if necessary
        import_line = f"from {module_name} import {', '.join(imports_to_add)}"

    test_content += f'''
{import_line}

class Test{module_name.title().replace('_', '')}(unittest.TestCase):
'''

    # Generate test methods for functions
    for func in functions:
        test_content += f'''
    def test_{func}(self):
        """Test {func} function."""
        # TODO: Implement test for {func}
        # Example: result = {func}(test_input)
        # self.assertEqual(result, expected_output)
        pass
'''

    # Generate test methods for classes
    for cls in classes:
        test_content += f'''
    def test_{cls.lower()}(self):
        """Test {cls} class."""
        # TODO: Implement test for {cls}
        # Example: instance = {cls}()
        # self.assertIsInstance(instance, {cls})
        pass
'''

    if not functions and not classes:
        test_content += '''
    def test_module_imports(self):
        """Test that the module can be imported without errors."""
        try:
            import ''' + module_name + '''
            self.assertTrue(True)
        except ImportError:
            self.fail("Failed to import module")
'''

    test_content += '''
if __name__ == '__main__':
    unittest.main()
'''
    
    return test_content

def process_python_file(file_path, log_file):
    '''Process a Python file directly and generate tests.'''
    try:
        file_path_obj = Path(file_path)
        
        # Skip test files themselves (only if they start with test_ or end with _test.py)
        if file_path_obj.name.startswith('test_') or file_path_obj.name.endswith('_test.py'):
            with log_file.open('a', encoding='utf-8') as f:
                f.write(f"Skipping test file: {file_path_obj.name}\n")
            return
            
        # Get the module name
        module_name = file_path_obj.stem
        
        # Create test file path
        test_dir = file_path_obj.parent / 'tests'
        test_dir.mkdir(exist_ok=True)
        test_file_path = test_dir / f'test_{module_name}.py'
        
        # Skip if test file already exists
        if test_file_path.exists():
            with log_file.open('a', encoding='utf-8') as f:
                f.write(f"Test file already exists: {test_file_path}\n")
            return
            
        # Extract functions and classes
        functions, classes = extract_functions_and_classes(file_path)
        
        with log_file.open('a', encoding='utf-8') as f:
            f.write(f"Found functions: {functions}, classes: {classes}\n")
        
        # Generate test content
        test_content = generate_test_content(module_name, functions, classes)
        
        # Write test file
        with test_file_path.open('w', encoding='utf-8') as f:
            f.write(test_content)
            
        with log_file.open('a', encoding='utf-8') as f:
            f.write(f"Successfully generated test file: {test_file_path}\n")
        
        print(f'Generated test file: {test_file_path}')
        
    except Exception as e:
        with log_file.open('a', encoding='utf-8') as f:
            f.write(f"Error in process_python_file: {str(e)}\n")
            import traceback
            f.write(f"Traceback: {traceback.format_exc()}\n")

def main():
    '''Main function that processes the hook input.'''
    try:
        # Create a log file for debugging
        log_file = Path(__file__).parent / 'hook_debug.log'
        
        # Log execution attempt
        with log_file.open('a', encoding='utf-8') as f:
            f.write(f"\n--- Hook execution attempt ---\n")
            f.write(f"Script: {__file__}\n")
            f.write(f"Args: {sys.argv}\n")
            
        # Try reading from stdin first
        input_data = ""
        try:
            input_data = sys.stdin.read().strip()
            with log_file.open('a', encoding='utf-8') as f:
                f.write(f"Stdin data: {repr(input_data)}\n")
        except:
            with log_file.open('a', encoding='utf-8') as f:
                f.write("No stdin data available\n")
        
        # If no stdin data, try to process command line args or create a simple test
        if not input_data:
            with log_file.open('a', encoding='utf-8') as f:
                f.write("No input data - creating test based on recent Python file creation\n")
            
            # Look for recently created .py files in the project directory
            project_dir = Path(__file__).parent.parent
            py_files = list(project_dir.glob("*.py"))
            
            if py_files:
                # Get the most recently modified .py file
                latest_file = max(py_files, key=lambda p: p.stat().st_mtime)
                
                with log_file.open('a', encoding='utf-8') as f:
                    f.write(f"Processing latest Python file: {latest_file}\n")
                
                # Process this file directly
                process_python_file(str(latest_file), log_file)
            return
            
        # Parse JSON input if available
        hook_data = json.loads(input_data)
        
        # Log parsed data
        with log_file.open('a', encoding='utf-8') as f:
            f.write(f"Parsed hook data: {json.dumps(hook_data, indent=2)}\n")
        
        # Get the file path from the tool use data
        tool_use = hook_data.get('tool_use', {})
        tool_name = tool_use.get('tool_name', '')
        
        if tool_name != 'Write':
            return
            
        parameters = tool_use.get('parameters', {})
        file_path = parameters.get('file_path', '')
        
        file_path_obj = Path(file_path)
        
        # Only process Python files
        if file_path_obj.suffix != '.py':
            return
            
        # Skip test files themselves (only if they start with test_ or end with _test.py)
        if file_path_obj.name.startswith('test_') or file_path_obj.name.endswith('_test.py'):
            return
            
        # Get the module name
        module_name = file_path_obj.stem
        
        # Create test file path
        test_dir = file_path_obj.parent / 'tests'
        test_dir.mkdir(exist_ok=True)
        test_file_path = test_dir / f'test_{module_name}.py'
        
        # Skip if test file already exists
        if test_file_path.exists():
            return
            
        # Extract functions and classes
        functions, classes = extract_functions_and_classes(file_path)
        
        # Generate test content
        test_content = generate_test_content(module_name, functions, classes)
        
        # Write test file
        with test_file_path.open('w', encoding='utf-8') as f:
            f.write(test_content)
            
        print(f'Generated test file: {test_file_path}')
        
        # Log success
        with log_file.open('a', encoding='utf-8') as f:
            f.write(f"Successfully generated test file: {test_file_path}\n")
        
    except Exception as e:
        # Log error details
        log_file = Path(__file__).parent / 'hook_debug.log'
        with log_file.open('a', encoding='utf-8') as f:
            f.write(f"Error: {str(e)}\n")
            import traceback
            f.write(f"Traceback: {traceback.format_exc()}\n")
        print(f'Error generating test: {e}', file=sys.stderr)

if __name__ == '__main__':
    main()
