import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 436734951 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
  alpha = 1 - p
  size = len(x)
  left = np.sqrt(size * (x**2).mean() / (49 * chi2.ppf(q=1 - alpha / 2, df=2 * size)))
  right = np.sqrt(size * (x**2).mean() / (49 * chi2.ppf(q=alpha / 2, df=2 * size)))
  return left, right
