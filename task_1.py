import time


def find_coins_greedy(customer_change):
    start_time = time.time()

    coins = [50, 25, 10, 5, 2, 1]
    coins.sort(reverse=True)
    result = {}
    for coin in coins:
        if customer_change>=coin:
            count = customer_change//coin
            customer_change -=count*coin
            result[coin] = count
    
    end_time = time.time()
    process_time = (end_time - start_time)*1000

    print (f"Час виконання жадібного алгоритму: {process_time}")

    return result

print (find_coins_greedy(10000))

def find_min_coins(coins, change):
    start_time = time.time()

    coins = sorted(coins)
    # Ініціалізація масиву для збереження мінімальної кількості монет для кожної суми до change
    dp = [float('inf')] * (change + 1)
    dp[0] = 0  # Нульова сума потребує 0 монет
    
    # Масив для збереження кількості монет кожного номіналу для досягнення суми
    coin_count = [{} for _ in range(change + 1)]
    coin_count[0] = {coin: 0 for coin in coins}
    
    # Заповнення масиву dp та coin_count
    for coin in coins:
        for x in range(coin, change + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                # Оновлюємо кількість монет
                coin_count[x] = coin_count[x - coin].copy()
                coin_count[x][coin] += 1
    end_time = time.time()
    process_time = (end_time - start_time)*1000
    print(f"Час виконання динамічного програмування: {process_time}")
    
    if dp[change] == float('inf'):
        return {}  # Якщо сума не може бути сформована, повертаємо порожній словник
    else:
        result = {k: v for k, v in coin_count[change].items() if v > 0}
        return result


coins = [50, 25, 10, 5, 2, 1]
change = 10000
print(find_min_coins(coins, change))
