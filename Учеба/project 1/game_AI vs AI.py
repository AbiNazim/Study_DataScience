import numpy as np

def game_core_v3(number: int = 1) -> int:

    count = 0
    make_a_wish = np.random.randint(1, 101)
    
    while number != make_a_wish:
        count += 1
        if number > make_a_wish:
            make_a_wish += 4
        else:
            make_a_wish -= 5

    return count

def score_game(random_predict) -> int:

    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    

print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)