from  sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler

def unscale_coefficients(model: LinearRegression, x_scalers_list: list, y_scaler: MinMaxScaler, show: bool=True) -> tuple:
    """
        Transform scaled coefficients and intercept from a Linear Regression model back to their original unscaled values.

        Args:
            model (LinearRegression): A fitted Linear Regression model with scaled coefficients.
            x_scalers_list (list): A list of MinMaxScaler objects corresponding to each feature used in the model, in the same order as the features were fed into the model.
            y_scaler (MinMaxScaler): The MinMaxScaler object used to scale the target variable (Y) during model training.
            show (bool): If True, prints the unscaled coefficients and intercept. Default is True.

        Returns:
            A tuple containing:
                - m_unscaled_list (list): A list of unscaled coefficients corresponding to each feature.
                - c_unscaled (float): The unscaled intercept for the model.
    """

    # 1. Extract the scaled weights from your Multiple Linear Regression model
    # model.coef_ will be an array of coefficients [m1, m2, m3, ...]
    m_scaled_list = model.coef_  
    c_scaled = model.intercept_

    # 2. Retrieve the scaling parameters for your dependent target variable (Y)
    Y_min, Y_max = y_scaler.data_min_[0], y_scaler.data_max_[0]
    Y_range = Y_max - Y_min

    # 3. Create arrays to store your final unscaled constants
    m_unscaled_list = []
    intercept_shift_accumulation = 0.0

    # 4. Act as the Translator: Loop through each feature to unscale its coefficient
    # We assume x_scalers_list matches the exact order of features fed into the ML model
    for i, x_scaler in enumerate(x_scalers_list):
        # Retrieve the boundaries for the current feature X_i
        X_min = x_scaler.data_min_[0]
        X_max = x_scaler.data_max_[0]
        X_range = X_max - X_min
        
        # Calculate the unscaled slope for this specific feature
        m_unscaled_i = m_scaled_list[i] * (Y_range / X_range)
        m_unscaled_list.append(m_unscaled_i)
        
        # Accumulate the horizontal shift caused by this feature's non-zero baseline
        intercept_shift_accumulation += m_unscaled_i * X_min

    # 5. Calculate the final true real-world intercept
    # We unscale the abstract intercept baseline, then subtract the accumulated horizontal shifts
    c_unscaled_baseline = (c_scaled * Y_range) + Y_min
    c_unscaled = c_unscaled_baseline - intercept_shift_accumulation

    if show:
        # 6. (Optional) Display the inputs for your simulation constants
        print("--- Unscaled Simulation Parameters ---")
        for idx, m_val in enumerate(m_unscaled_list):
            print(f"Simulation Constant (Slope for Feature {idx+1}): {m_val}")
        print(f"Simulation Constant (Global Intercept): {c_unscaled}")

    return m_unscaled_list, c_unscaled