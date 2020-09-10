str = 'X-DSPAM-Confidence: 0.8475'

space = str.find(':')
print(space)

piece = str[space+2:]
print(piece)  # string
print(piece + 42.0)  # will fail

value = float(piece)
print(value)  # float
print(value + 42.0)  # 42.8475