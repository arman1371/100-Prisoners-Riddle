from random import shuffle


def get_random_boxes():
    inside_numbers = [number for number in range(100)]
    shuffle(inside_numbers)
    dict_box = dict()
    for outside_number in range(100):
        dict_box[outside_number] = inside_numbers[outside_number]
    return dict_box


def try_to_solve(select_method):
    boxes = get_random_boxes()
    for person in range(100):
        if not select_method(person, boxes):
            return 0
    return 1


def random_strategy(person, boxes):
    for outside_number in range(50):
        if boxes[outside_number] == person:
            return True
    return False


def loop_strategy(person, boxes):
    next_open = person
    for select_try in range(50):
        if boxes[next_open] == person:
            return True
        next_open = boxes[next_open]
    return False


if __name__ == '__main__':
    total_run = 10**3
    random_strategy_win_count = 0
    loop_strategy_win_count = 0
    for i in range(total_run):
        random_strategy_win_count += try_to_solve(random_strategy)
        loop_strategy_win_count += try_to_solve(loop_strategy)

    print(f'Random strategy win percent: {random_strategy_win_count/total_run}')
    print(f'Loop strategy win percent: {loop_strategy_win_count / total_run}')
