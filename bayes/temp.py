# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

#prob_alza : P(H)
#prob_sintoma_dado_alza : P(E/H)
#prob_sintoma_dado_no_alza : P(E/~H)
#prob_no_alza : P(~H)
#prob_alza_dado_sintoma : P(H/E) 

def calc_bayes(prior_A, prob_B_dado_A, prob_B):
    return (prior_A * prob_B_dado_A) / prob_B

if __name__ == '__main__':
    prob_alza = 71/125
    prob_sintoma_dado_alza = 64/71
    prob_sintoma_dado_no_alza = 49/54
    prob_no_alza = 1 - prob_alza
 
    prob_sintoma = (prob_sintoma_dado_alza * prob_alza) + (prob_sintoma_dado_no_alza * prob_no_alza)

    prob_alza_dado_sintoma = calc_bayes(prob_alza, prob_sintoma_dado_alza, prob_sintoma)

print("**********************************************************")
print("")
print(f" Probabilidad de alza accion P(H/E): {prob_alza_dado_sintoma}")
print("")
print("**********************************************************")   