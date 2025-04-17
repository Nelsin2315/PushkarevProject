import sys


def get_mean_size(ls_output: str) -> float:

    memory = 0
    count = 0

    for str in ls_output:
        if str.startswith('-'):
            columns = str.split()
            memory += int(columns[4])
            count += 1

    return memory / count if count > 0 else 0

if __name__ == '__main__':
    data: str = sys.stdin.readlines()[1:]
    mean_size: float = get_mean_size(data)
    print(mean_size)