from services import Weather


def main():
    w = Weather()
    print(w.current_weather('Espoo'))


if __name__ == '__main__':
    main()