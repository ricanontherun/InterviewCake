"""

Calculate the product of the integers in a list EXCEPT for the ones
at each index.

https://www.interviewcake.com/question/python/product-of-other-numbers
"""


def get_product_list(numbers):
    products = [0 for x in numbers]
    list_length = len(numbers)

    # Check for empty numbers
    if list_length == 0:
        return products

    if list_length == 2:
        return list(reversed(numbers))

    # Calculate the product of the first element.
    product = 1
    for i in numbers[1:]:
        product *= i
    products[0] = product

    # The whole approach to this solution is that the product we seek
    # is the product of the products to the left and right of the element.
    # We keep track of the product we know about, the product of the elements
    # to the left of the current number. At each index we find the product of the
    # elements to the right of the index and multiply that with the current "left product"
    left_product = numbers[0]

    for i in range(1, list_length):
        next = i + 1

        # Once we hit the last element, the product is
        # the product of the elements to the left. Which is
        # what we've been tracking thus far.
        if next == list_length:
            products[i] = left_product
            break

        right_product = 1
        for key, value in enumerate(numbers[next:]):
            right_product *= value

        # at this point, we have the current left_product and the product for the
        # numbers to the right of the index i.
        products[i] = left_product * right_product
        left_product *= numbers[i]

    return products


def main():
    list = [5,3]

    product_list = get_product_list(list)

    print(product_list)


if __name__ == "__main__":
    main()
