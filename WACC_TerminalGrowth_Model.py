import numpy as np
import pandas as pd

class FinancialModels:
    def __init__(self):
        pass
    
    def calculate_wacc(self, equity_value, debt_value, cost_of_equity, cost_of_debt, tax_rate):
        """
        Calculate the Weighted Average Cost of Capital (WACC)
        
        Parameters:
        equity_value (float): Market value of equity
        debt_value (float): Market value of debt
        cost_of_equity (float): Cost of equity (in decimal form, e.g., 0.10 for 10%)
        cost_of_debt (float): Cost of debt (in decimal form)
        tax_rate (float): Corporate tax rate (in decimal form)
        
        Returns:
        float: WACC value
        """
        total_value = equity_value + debt_value
        equity_weight = equity_value / total_value
        debt_weight = debt_value / total_value
        
        wacc = (equity_weight * cost_of_equity) + (debt_weight * cost_of_debt * (1 - tax_rate))
        return wacc
    
    def calculate_cost_of_equity(self, risk_free_rate, beta, market_risk_premium):
        """
        Calculate Cost of Equity using CAPM
        """
        return risk_free_rate + (beta * market_risk_premium)
    
    def calculate_terminal_growth_gdp(self, real_gdp_growth, inflation_rate, adjustment_factor=1.0):
        """
        Calculate terminal growth rate using GDP method
        
        Parameters:
        real_gdp_growth (float): Real GDP growth rate
        inflation_rate (float): Expected inflation rate
        adjustment_factor (float): Company-specific adjustment (default 1.0)
        
        Returns:
        float: Terminal growth rate
        """
        return (real_gdp_growth + inflation_rate) * adjustment_factor
    
    def calculate_terminal_growth_reinvestment(self, return_on_capital, reinvestment_rate):
        """
        Calculate terminal growth rate using reinvestment method
        
        Parameters:
        return_on_capital (float): Return on invested capital
        reinvestment_rate (float): Reinvestment rate
        
        Returns:
        float: Terminal growth rate
        """
        return return_on_capital * reinvestment_rate
    
    def calculate_reinvestment_rate(self, capex, depreciation, working_capital_change, ebit, tax_rate):
        """
        Calculate reinvestment rate
        """
        return (capex - depreciation + working_capital_change) / (ebit * (1 - tax_rate))
    
    def calculate_terminal_value(self, final_cash_flow, terminal_growth_rate, discount_rate):
        """
        Calculate terminal value using Gordon Growth Model
        """
        return final_cash_flow * (1 + terminal_growth_rate) / (discount_rate - terminal_growth_rate)
    
    def historical_growth_analysis(self, historical_data, periods=5):
        """
        Analyze historical growth rates
        
        Parameters:
        historical_data (list/array): Historical values
        periods (int): Number of periods to analyze
        
        Returns:
        dict: Growth statistics
        """
        data = np.array(historical_data)
        growth_rates = (data[1:] - data[:-1]) / data[:-1]
        
        return {
            'mean_growth': np.mean(growth_rates),
            'median_growth': np.median(growth_rates),
            'std_dev': np.std(growth_rates),
            'min_growth': np.min(growth_rates),
            'max_growth': np.max(growth_rates)
        }

# Example usage
def main():
    # Initialize the financial models
    fm = FinancialModels()
    
    # Example 1: Calculate WACC
    wacc = fm.calculate_wacc(
        equity_value=1000000,
        debt_value=500000,
        cost_of_equity=0.10,
        cost_of_debt=0.05,
        tax_rate=0.25
    )
    print(f"WACC: {wacc:.2%}")
    
    # Example 2: Calculate terminal growth rate using GDP method
    terminal_growth = fm.calculate_terminal_growth_gdp(
        real_gdp_growth=0.02,
        inflation_rate=0.015
    )
    print(f"Terminal Growth Rate (GDP method): {terminal_growth:.2%}")
    
    # Example 3: Calculate terminal growth rate using reinvestment method
    reinvestment_growth = fm.calculate_terminal_growth_reinvestment(
        return_on_capital=0.15,
        reinvestment_rate=0.20
    )
    print(f"Terminal Growth Rate (Reinvestment method): {reinvestment_growth:.2%}")
    
    # Example 4: Historical growth analysis
    historical_data = [100, 110, 125, 135, 150, 172]
    growth_stats = fm.historical_growth_analysis(historical_data)
    print("\nHistorical Growth Analysis:")
    for key, value in growth_stats.items():
        print(f"{key}: {value:.2%}")

if __name__ == "__main__":
    main()
    
    