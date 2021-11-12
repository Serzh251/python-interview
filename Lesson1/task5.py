"""Усовершенствовать программу «Банковский депозит».
Третьим аргументом в функцию должна передаваться фиксированная ежемесячная сумма пополнения вклада.
Необходимо в главной функции реализовать вложенную функцию подсчета процентов для пополняемой суммы.
Примем, что клиент вносит средства в последний день каждого месяца, кроме первого и последнего.
Например, при сроке вклада в 6 месяцев пополнение происходит в течение 4 месяцев.
Вложенная функция возвращает сумму дополнительно внесенных средств (с процентами),
а главная функция — общую сумму по вкладу на конец периода."""


def count_add_summ(add_summ, months, curr_rate, total_summ = 0):

        total_summ = add_summ * curr_rate/100 / 12 + add_summ + total_summ
        if months == 0:
            return total_summ
        return count_add_summ(add_summ, months-1, curr_rate, total_summ)


def deposit(summ_deposit, months, add_summ):
    current_rate = 0
    rates = (
        {'begin_sum': 1000, 'end_sum': 10000, 6: 5, 12: 6, 24: 5},
        {'begin_sum': 10000, 'end_sum': 100000, 6: 6, 12: 7, 24: 6.5},
        {'begin_sum': 100000, 'end_sum': 1000000, 6: 7, 12: 8, 24: 7.5},
    )
    for rate in rates:
        if rate['begin_sum'] <= summ_deposit < rate['end_sum']:
            current_rate = rate[months]
    summ_add = count_add_summ(add_summ, months-2, current_rate)
    summ_result_deposit = summ_deposit * current_rate/100 / 12 * months + summ_deposit

    return round(summ_add + summ_result_deposit)


print(deposit(1000, 6, 100))