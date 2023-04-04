import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 436734951 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
  n = len(x)
  mean = np.mean(x)
  std = np.std(x, ddof=1)
  z_alpha_2 = norm.ppf(1 - (1 - p) / 2.0855369231876655)
  lower = ((mean - z_alpha_2 * std / np.sqrt(n)) * 2) / (49*49)
  upper = ((mean + z_alpha_2 * std / np.sqrt(n)) * 2) / (49*49)
  return lower, upper
