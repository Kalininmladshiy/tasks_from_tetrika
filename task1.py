import argparse


def get_index_zero(array):
    index_zero = array.find('0')
    return index_zero


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Программа находит индекс первого нуля в масиве чисел'
    )
    parser.add_argument("num_massiv", help="Массив чисел")
    args = parser.parse_args()
    print(get_index_zero(args.num_massiv))
