import numpy as np
from  sklearn.metrics import mean_squared_error

def theils_stats(actual: np.ndarray, simulated: np.ndarray, show:bool=False) -> dict:
    """
    Calculates Theil's Inequality Proportions (Um, Us, Uc)

    Args:
        actual (np.ndarray): array-like of real-world observations (len: 113)
        simulated (np.ndarray): array-like of PySD outputs (len: 113)

    Returns:
        A dictionary containing:
            - Um: Bias Proportion/Systemic Error - The model over/underestimates the actual values (Ideal: close to 0)
            - Us: Variance Proportion/Intensity Error - The actual spikes are much larger or smaller than the simulated values (Ideal: close to 0)
            - Uc: Covariation Proportion/Timing Error - The spikes' timing matches/mismatches the actual values(Ideal: close to 1)
            - MSE: Total Mean Squared Error
    """
    # Convert to numpy arrays
    A = np.array(actual)
    S = np.array(simulated)
    
    # 1. Calculate overall Mean Squared Error (MSE)
    mse = mean_squared_error(A, S)
    
    # 2. Calculate Means and Standard Deviations
    mean_A, mean_S = np.mean(A), np.mean(S)
    std_A, std_S = np.std(A), np.std(S)
    
    # 3. Calculate Correlation Coefficient (r)
    # handles edge cases where std might be 0
    if std_A == 0 or std_S == 0:
        r = 0
    else:
        r = np.corrcoef(A, S)[0, 1]
    
    # 4. Decompose MSE into Theil's components
    bias_comp = (mean_S - mean_A) ** 2
    var_comp = (std_S - std_A) ** 2
    cov_comp = 2 * (1 - r) * std_S * std_A
    
    # 5. Calculate Proportions (Divided by total MSE)
    Um = bias_comp / mse
    Us = var_comp / mse
    Uc = cov_comp / mse
    
    if show:
        print(f"--- Theil's Decomposition Report ---")
        print(f"Total MSE: {mse:.4f}")
        print(f"Um (Bias Proportion):      {Um:.4f} (Ideal: close to 0)")
        print(f"Us (Variance Proportion):  {Us:.4f} (Ideal: close to 0)")
        print(f"Uc (Covariation Prop):     {Uc:.4f} (Ideal: close to 1)")
        print(f"Sum check (Should be 1.0): {Um + Us + Uc:.4f}")
    
    return {"Um": Um, "Us": Us, "Uc": Uc, "MSE": mse}

# --- How to use it in your pipeline ---
# actual_dryness = df['actual_score'].values
# simulated_dryness = results['average_dryness'].values
# metrics = calculate_theils_statistics(actual_dryness, simulated_dryness)