from data_reader import choose_odu, read_data


def main():
    f,exact_y = choose_odu()
    x0, xn, n, y0, epsilon = read_data()
    print(x0, xn, n, y0, epsilon)
if __name__ == "__main__":
    main()
