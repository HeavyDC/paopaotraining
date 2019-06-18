from __future__ import print_function


from inputs import get_gamepad


def main():
    while 1:
        events = get_gamepad()
        for event in events:
            print(event.code)


if __name__ == "__main__":
    print("Test your inputs")
    main()