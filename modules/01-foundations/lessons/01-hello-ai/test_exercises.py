"""
Simple test file for students to verify their solutions work correctly.
Run with: python test_exercises.py
"""

def test_hello_world():
    """Test for Exercise 1"""
    print("Testing Exercise 1...")
    # Students can add their hello world test here
    print("✓ Manual test needed - did it print 'Hello, World!'?")

def test_hello_input():
    """Test for Exercise 2"""
    print("\nTesting Exercise 2...")
    print("✓ Manual test needed - did it ask for name and greet personally?")

def test_debugging():
    """Test for Exercise 3"""
    print("\nTesting Exercise 3...")
    print("✓ Manual test needed - does it correctly show the color in the output?")

def test_introduction():
    """Test for Mini-Project"""
    print("\nTesting Mini-Project...")
    print("✓ Manual test needed - does it collect all info and format nicely?")

if __name__ == "__main__":
    print("Running lesson 1 tests...\n")
    test_hello_world()
    test_hello_input()
    test_debugging()
    test_introduction()
    print("\nAll tests require manual verification for this lesson!")