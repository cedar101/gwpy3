def test_input_generator(*args):
    """Creates test input function that reads inputs from the passed arguments.
    This is used to override input to allow doctests to mimic user
    input

    Returns:
        function: this function is meant to moc out input and each time it is
                  called it will print the supplied prompt along with the "input"
                  supplied at the time the function was created.

    """
    input_iterator = (test_input for test_input in args)

    def test_input(prompt):
        """Gets input from outer input_iterator and prints the supplied
        prompt along with the test input.

        Args:
            prompt :  the prompt ot display to the user

        Returns:
            str:  the test input string
        """
        response = next(input_iterator)
        print(f"{prompt}{response}")
        return response

    return test_input