import os


def get_summary_rss(ps_output_file_path: str) -> str:
    with open(ps_output_file_path, 'r') as output_file:
        lines = output_file.readlines()[1:]

        total_memory = 0

        for line in lines:
            columns = line.split()
            total_memory += int(columns[5])

    units = ['Б', 'Кб', 'Мб', 'Гб', 'Тб']
    cur_unit_index = 0

    while total_memory >= 1024 and cur_unit_index < len(units):
        total_memory /= 1024
        cur_unit_index += 1

    return f'{total_memory:.2f} {units[cur_unit_index]}'


if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    path: str = os.path.join(BASE_DIR, 'output_file.txt')
    summary_rss: str = get_summary_rss(path)
    print(summary_rss)