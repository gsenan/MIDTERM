def is_valid_url(url):
    # Check if the URL starts with http:// or https://
    if url.startswith("http://") or url.startswith("https://"):
        # Check if the URL contains a dot, indicating a domain name
        if "." in url:
            return True
        else:
            print("URL must contain a domain name.")
            return False
    else:
        print("URL must start with http:// or https://")
        return False

# Test the function
print(is_valid_url("https://www.example.com"))
print(is_valid_url("www.example.com"))
print(is_valid_url("https://example"))