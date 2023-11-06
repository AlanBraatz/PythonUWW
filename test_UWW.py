# test_main.py
import main  # Import the main.py module

 
def test_hello_uww(capsys):
  main_output = "Hello UWWWW\n"
  main.main()
  captured = capsys.readouterr()
  assert captured.out == main_output

