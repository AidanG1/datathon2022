import convert_to_df
import random
import numpy as np
from collections import defaultdict


def markov_data(station: str, order):
    data = convert_to_df.convert_txt_to_df(station)["WDIR"].to_list()
    processed = [i//45 for i in data]
    data = processed
    model = create_markov(processed, order)

    #test the model
    ctr = 0
    sss=0
    for i in range(7000, len(data)-1):
        sss+=1
        sl = tuple(data[i-order:i])

        prediction = weighted_choice(sl, model)
        actual = data[i]
        #print(tuple(data[i-order:i]), ": predicted " ,prediction, ", actual ", actual)
        error = min(abs(prediction-actual), abs(8-(prediction-actual)))
        ctr += error**2
    #print("mse: " + str( ctr / (sss)))



def weighted_choice(sl, model):
    thresh = random.random()
    count=0
    if not sl in model:
        return random.randint(0,7)
        #return sl[-1]
    else:
        weights=model[sl]
        for k, v in weights.items():
            count+=v
            if count >= thresh:
                return k
        return weights.keys()[-1]


def create_markov(data: list, order):
    markov = {}
    for index in range(len(data)-order-1):
        dt_tuple = tuple(data[index:index+order])
        if dt_tuple not in markov:
            markov[dt_tuple] = defaultdict(int)

        markov[dt_tuple][data[index+order]] += 1;

    for key, value in markov.items():

        total = sum(value.values())
        for i in value:
            value[i]/=total
    #print(markov)
    return markov



# def run_markov(markov: dict, last_data: list):
#     results = []
#     for num in range(50):
#         tld = tuple(last_data)
#         if tld in markov:
#             probs = markov[tld]
#         else:
#             probs = {}
#             for i in range(10):
#                 probs[i] = i / 10
#         prob_sum = random.random()
#         for key, value in probs.items():
#             prob_sum -= value
#             if prob_sum < 0:
#                 results.append(key)
#                 last_data = last_data[1:]
#                 last_data.append(key)
#                 break
#     return results

# for j in range(1,40):
#     data = markov_data('VCAT2', j)
#print(run_markov(create_markov(data), data[-3:]))
