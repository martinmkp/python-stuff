def activation(w_sum):
    """
    Activation function: Transforms the input to 1 or 0.
    """
    if w_sum >= 0.5:
        return 1
    else:
        return 0

def perceptron(x1, x2, y_hat, y):
    n = len(y)
    weights = [0.1, 0.1]
    learning_rate = 0.1
    state = 1

    print("Initial weights:", weights)
    print("Training the perceptron...")

    while state == 1:
        for i in range(n):
            w_sum = x1[i]*weights[0] + x2[i]*weights[1]
            y_hat[i] = activation(w_sum)

            if y_hat[i] != y[i]:
                weights[0] = weights[0] + learning_rate*(y[i] - y_hat[i])
                weights[1] = weights[1] + learning_rate*(y[i] - y_hat[i])

        if y_hat == y:
            state = 0

    print("Training is complete.")
    print("Actual values:", y)
    print("Predicted values:", y_hat)
    print("Final weights:", weights)

    return None

if __name__ == "__main__":
    y = [0, 1, 1, 1]
    y_hat = [-1, -1, -1, -1]
    x1 = [0, 0, 1, 1]
    x2 = [0, 1, 0, 1]
    print("The input data (y, x1, x2):", y, x1, x2)
    print()

    perceptron(x1, x2, y_hat, y)
