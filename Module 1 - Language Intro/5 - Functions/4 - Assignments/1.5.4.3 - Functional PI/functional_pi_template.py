import math


def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """

   # 1. Initialization of variables
    a = 1.0
    b = 1.0 / math.sqrt(2)
    t = 1.0 / 4.0
    p = 1.0

    # 2. Iteration loop
    # We continue iterating until the difference between a and b is less than the target_error
    while abs(a - b) > target_error:
        # Calculate next values based on current values
        a_next = (a + b) / 2.0
        b_next = math.sqrt(a * b)
        t_next = t - p * (a - a_next)**2
        p_next = 2 * p
        
        # Update the variables for the next iteration
        a, b, t, p = a_next, b_next, t_next, p_next

    # 3. Calculate and return the final approximation of PI
    pi_approx = ((a + b)**2) / (4 * t)

    # change this so an actual value is returned
    return pi_approx




desired_error = 1E-10

approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
