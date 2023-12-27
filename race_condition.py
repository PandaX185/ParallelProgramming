import logging
import multiprocessing

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(processName)s - %(levelname)s - %(message)s')

def withdraw(balance):
    for _ in range(10000):
        balance.value = balance.value - 1


def deposit(balance):
    for _ in range(10000):
        balance.value = balance.value + 1


def perform_transactions():
    balance = multiprocessing.Value('i', 100)

    p1 = multiprocessing.Process(target=withdraw, args=(balance,))
    p2 = multiprocessing.Process(target=deposit, args=(balance,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    logging.info("Final balance = {}".format(balance.value))


if __name__ == "__main__":
    for _ in range(10):
        perform_transactions()