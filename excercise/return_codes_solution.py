def get_alphabet(number):
    """
    Helper function to figure out alphabet of a particular number
    Remember:
        * ASCII for lower case 'a' = 97
        * chr(num) returns ASCII character for a number e.g. chr(65) ==> 'A'
    """
    return chr(number + 96)

#
# def all_codes(number):
#     """
#     :param: number - input integer
#     Return - list() of all codes possible for this number
#     TODO: complete this method and return a list with all possible codes for the input number
#     """
#     if number // 10 == 0:  # It means number if between 1 - 9, then we definitely know the answer.
#         return get_alphabet(number)
#     last_num = number % 10
#     the_rest = number // 10
#     if the_rest > 26:  # It means that it must be per digit, because the last lower letter, z is represented by 26.
#         return get_alphabet(the_rest)
#
#     pass


# NOTES: [YC] The reason we need to call all_codes(number // 100) is because we need to attach the letter that represented by the last two digits together to each one of the result of all_codes(number // 100).
#
# and this is not needed when this condition is not met: if remainder_100 <= 26 and number > 9, because the last two digits together does not directly represents one letter. That case will be covered by the output_10 below, because it will look at the last one digit and attach the letter represented by the last digit to all_result of the rest, until the floor division is zero, which means there's no more digits before the remainder.
def all_codes(number):
    if number == 0:
        return [""]

    # calculation for two right-most digits e.g. if number = 1123, this calculation is meant for 23
    remainder_100 = number % 100
    output_100 = list()
    if remainder_100 <= 26 and number > 9:

        # get all codes for the remaining number
        output_100 = all_codes(number // 100)
        alphabet = get_alphabet(remainder_100)

        for index, element in enumerate(output_100):
            output_100[index] = element + alphabet

    # calculation for right-most digit e.g. if number = 1123, this calculation is meant for 3 # TODO: [YC] I don't understand this part sentence? I think it's for the left-most digit
    remainder_10 = number % 10

    # get all codes for the remaining number
    output_10 = all_codes(number // 10)
    alphabet = get_alphabet(remainder_10)

    for index, element in enumerate(output_10):
        output_10[index] = element + alphabet

    output = list()
    output.extend(output_100)
    output.extend(output_10)

    return output



# def test_function(test_case):
#     number = test_case[0]
#     solution = test_case[1]
#
#     output = all_codes(number)
#
#     output.sort()
#     solution.sort()
#
#     if output == solution:
#         print("Pass")
#     else:
#         print("Fail")
#
# number = 123
# solution = ['abc', 'aw', 'lc']
# test_case = [number, solution]
# test_function(test_case)
#
# number = 145
# solution =  ['ade', 'ne']
# test_case = [number, solution]
# test_function(test_case)
#
# number = 1145
# solution =  ['aade', 'ane', 'kde']
# test_case = [number, solution]
# test_function(test_case)
#
# number = 4545
# solution = ['dede']
# test_case = [number, solution]
# test_function(test_case)