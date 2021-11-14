def reverse(m):
    if len(m) == 1:
        return m
    return m[-1] + reverse(m[0:-1:1])

output = reverse("aditya")
print(output)
if output == "aditya":
    print(True)
else:
    print(False)
