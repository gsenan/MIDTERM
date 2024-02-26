def count_pattern(text):
    count = 0
    words = text.split()
    for word in words:
        if word.startswith('b') and word.endswith('Bob'):
            count += 1
    return count

# Test the function with text
text = "Here is some text with b123Bob and b456Bob and just Bob and bBob"
print("The pattern appears", count_pattern(text), "times")