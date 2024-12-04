import pandas as pd
import numpy as np

class ImpliedPECalculator:
    def __init__(self):
        pass
        
    def calculate_implied_pe(self, current_price, current_eps, growth_rate, payout_ratio=0):
        """
        Calculate implied 12-month forward P/E multiple
        
        Parameters:
        current_price (float): Current stock price
        current_eps (float): Current earnings per share
        growth_rate (float): Expected earnings growth rate (decimal)
        payout_ratio (float): Dividend payout ratio (decimal)
        
        Returns:
        float: Implied forward P/E multiple
        """
        # Calculate forward EPS
        retention_ratio = 1 - payout_ratio
        forward_eps = current_eps * (1 + growth_rate)
        
        # Calculate implied PE
        implied_pe = current_price / forward_eps
        
        return implied_pe
    
    def calculate_industry_implied_pe(self, peer_data):
        """
        Calculate industry implied PE using peer comparison
        
        Parameters:
        peer_data (dict): Dictionary with company names as keys and tuples of 
                         (price, eps, growth_rate) as values
        
        Returns:
        dict: Dictionary with individual and median PE multiples
        """
        pe_multiples = {}
        
        for company, (price, eps, growth) in peer_data.items():
            pe_multiples[company] = self.calculate_implied_pe(price, eps, growth)
            
        median_pe = np.median(list(pe_multiples.values()))
        
        return {
            'individual_multiples': pe_multiples,
            'median_pe': median_pe
        }
    
    def sensitivity_analysis(self, current_price, current_eps, 
                           growth_rates, payout_ratios):
        """
        Perform sensitivity analysis on implied PE
        
        Parameters:
        current_price (float): Current stock price
        current_eps (float): Current earnings per share
        growth_rates (list): List of growth rate scenarios
        payout_ratios (list): List of payout ratio scenarios
        
        Returns:
        pandas.DataFrame: Sensitivity matrix of implied PEs
        """
        sensitivity_matrix = []
        
        for growth in growth_rates:
            row = []
            for payout in payout_ratios:
                pe = self.calculate_implied_pe(current_price, current_eps, 
                                            growth, payout)
                row.append(pe)
            sensitivity_matrix.append(row)
            
        return pd.DataFrame(sensitivity_matrix, 
                          index=[f'{g:.1%}' for g in growth_rates],
                          columns=[f'{p:.1%}' for p in payout_ratios])

# Example usage
def main():
    calculator = ImpliedPECalculator()
    
    # Basic PE calculation
    price = 100
    eps = 5
    growth_rate = 0.10
    payout_ratio = 0.30
    
    implied_pe = calculator.calculate_implied_pe(price, eps, growth_rate, payout_ratio)
    print(f"Implied Forward P/E: {implied_pe:.2f}x")
    
    # Industry comparison
    peer_data = {
        'Company A': (100, 5, 0.10),
        'Company B': (80, 4, 0.08),
        'Company C': (120, 6, 0.12)
    }
    
    industry_pe = calculator.calculate_industry_implied_pe(peer_data)
    print("\nIndustry Analysis:")
    for company, pe in industry_pe['individual_multiples'].items():
        print(f"{company} P/E: {pe:.2f}x")
    print(f"Median Industry P/E: {industry_pe['median_pe']:.2f}x")
    
    # Sensitivity analysis
    growth_rates = [0.05, 0.10, 0.15, 0.20]
    payout_ratios = [0.20, 0.30, 0.40, 0.50]
    
    sensitivity = calculator.sensitivity_analysis(price, eps, growth_rates, payout_ratios)
    print("\nSensitivity Analysis:")
    print(sensitivity)

if __name__ == "__main__":
    main()