def sct(inp_val):
    """
    The sct function takes a number input and calculates the product 
    of the sine, cosine and tangent of the input

    Args:
        in_val: Input angle in radians

    Returns:
        out_val: The product of the sin, cos and tan values of in_val
    """
    outp_val = np.sin(in_val) * np.cos(in_val) * np.tan(in_val)
    return out_val
