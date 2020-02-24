try:
    text = input('Enter something --> ')
except EOFError:
    print('Unexpected End of File')
except KeyboardInterrupt:
    print("Keyboard interruption")
else:
    print(f"You've just entered: {text}")