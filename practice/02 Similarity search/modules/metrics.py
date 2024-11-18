import numpy as np


def ED_distance(ts1: np.ndarray, ts2: np.ndarray) -> float:
    """
    Calculate the Euclidean distance

    Parameters
    ----------
    ts1: the first time series
    ts2: the second time series

    Returns
    -------
    ed_dist: euclidean distance between ts1 and ts2
    """
    
    ed_dist = 0
    ed_dist = np.sqrt(np.sum((ts1 - ts2) ** 2))

    return ed_dist


def norm_ED_distance(ts1: np.ndarray, ts2: np.ndarray) -> float:
    """
    Calculate the normalized Euclidean distance

    Parameters
    ----------
    ts1: the first time series
    ts2: the second time series

    Returns
    -------
    norm_ed_dist: normalized Euclidean distance between ts1 and ts2s
    """

    norm_ed_dist = 0

    # INSERT YOUR CODE
    n = len(ts1)
    
    # Calculate means and standard deviations
    mu_T1, sigma_T1 = calculate_mean_std(ts1)
    mu_T2, sigma_T2 = calculate_mean_std(ts2)
    
    # Calculate scalar product
    scalar_product = np.dot(ts1, ts2)
    
    # Calculate normalized Euclidean distance
    norm_ed_dist = np.sqrt(
        abs(2 * n * (1 - (scalar_product - n * mu_T1 * mu_T2) / (n * sigma_T1 * sigma_T2)))
    )

    return norm_ed_dist


def DTW_distance(ts1: np.ndarray, ts2: np.ndarray, r: float = 1) -> float:
    """
    Calculate DTW distance

    Parameters
    ----------
    ts1: first time series
    ts2: second time series
    r: warping window size
    
    Returns
    -------
    dtw_dist: DTW distance between ts1 and ts2
    """

    dtw_dist = 0

    n, m = len(ts1), len(ts2)
    dtw_matrix = np.full((n + 1, m + 1), np.inf)
    dtw_matrix[0, 0] = 0

    # if r is None:
    #     r_abs = max(n, m)  # Полоса включает всю матрицу
    # else:
    #     r_abs = r * max(n, m)  # Определяем абсолютное значение полосы

    # Заполняем матрицу DTW с учетом полосы
    dtw_matrix = np.full((n + 1, m + 1), np.inf)
    dtw_matrix[0, 0] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
          
          if r > 0:
            print(r)
            if not (int(np.ceil(j -r)) <= i <= int(np.ceil(j + r))):
              continue
          cost = (euclidean_distance(ts1[i - 1], ts2[j - 1])) ** 2
          dtw_matrix[i, j] = cost + min(dtw_matrix[i - 1, j],    # Вверх
                                          dtw_matrix[i, j - 1],    # Влево
                                          dtw_matrix[i - 1, j - 1] # По диагонали
                                        )

    # Финальное расстояние находится в правом нижнем углу
    print(dtw_matrix)
    dtw_dist = dtw_matrix[n, m]
    return dtw_dist


def euclidean_distance(a, b):
    
  return (a - b) 
  #return np.sqrt((a - b) ** 2)

def calculate_mean_std(series: np.ndarray):
    """
    Calculate mean and standard deviation of a time series.
    
    Parameters
    ----------
    series : np.ndarray
        Time series (1D array).
    
    Returns
    -------
    mean : float
        Mean of the time series.
    std : float
        Standard deviation of the time series.
    """
    n = len(series)
    mean = np.mean(series)  # Alternatively: np.sum(series) / n
    std = np.sqrt(np.sum(series**2) / n - mean**2)
    return mean, std
