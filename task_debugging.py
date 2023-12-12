import logging

logging.basicConfig(level=logging.INFO, filename='text.txt')

logger = logging.getLogger(__name__)

# вводим количество сайтов
n = int(input('N:'))
assert n > 0
logger.info("Количество введенных сайтов")


# находим максимальную цену и минимальную цену айфона
x = int(input('Цена за айфон:'))
assert x > 0
logger.info("Цена с первого сайта")

sale_min = x
sale_max = x

for i in range(n - 1):
    x = int(input('Цена за айфон:'))
    assert x > 0
    logger.info("Цена со следующего сайта")

    if x > sale_max:
        sale_max = x
    if x < sale_min:
        sale_min = x

print('Максимальная цена айфона: ', sale_max,
      'Минимальная цена айфона: ', sale_min)