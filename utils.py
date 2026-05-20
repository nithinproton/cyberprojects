def generate_test_cases(inputs, payload):

    test_cases = []

    for inp in inputs:

        data = {}

        for field in inputs:
            data[field] = "test"

        data[inp] = payload

        test_cases.append(data)

    return test_cases
