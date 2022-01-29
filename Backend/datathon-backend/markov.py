import convert_to_df
import random
import numpy as np


def markov_data(station: str):
    data = convert_to_df.convert_txt_to_df(station).WSPD.to_list()
    data = [i for i in data if i != np.NaN]
    data.reverse()
    max_speed = float(max(data))
    for point in data:
        if point != np.NaN:
            point = round(10 * point / max_speed)
    return data


def create_markov(data: list):
    markov_dict = {}
    dt = data[:3]
    for index, point in enumerate(data[3:]):
        dt_tuple = tuple(dt)
        if dt_tuple in markov_dict:
            markov_dict[dt_tuple].append(point)
        else:
            markov_dict[dt_tuple] = [point]
        dt = dt[1:]
        dt.append(point)

    for value in markov_dict.values():
        values = {}
        for item in value:
            values[item] = value.count(item)/len(value)
            markov_dict[value] = values

    return markov_dict


def run_markov(markov: dict, last_data: list):
    results = []
    for num in range(50):
        tld = tuple(last_data)
        if tld in markov:
            probs = markov[tld]
        else:
            probs = {}
            for i in range(10):
                probs[i] = i / 10
        prob_sum = random.random()
        for key, value in probs.items():
            prob_sum -= value
            if prob_sum < 0:
                results.append(key)
                last_data = last_data[1:]
                last_data.append(key)
                break
    return results


data = markov_data('kbqx')
print(run_markov(create_markov(data), data[-3:]))
