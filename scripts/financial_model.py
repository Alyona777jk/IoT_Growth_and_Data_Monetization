# scripts/financial_model.py

def calculate_data_monetization():
    months = 24
    core_hardware_saas_rev = [20000 + i * 2500 for i in range(months)] # Core revenue growth
    
    # Data Revenue Stream Assumptions
    oem_insights_rev = [0 if i < 6 else (i - 5) * 1200 for i in range(months)]
    api_access_rev = [0 if i < 8 else (i - 7) * 800 for i in range(months)]
    benchmarking_rev = [0 if i%3 != 0 or i < 6 else 5000 for i in range(months)]
    
    total_data_revenue = []
    infra_costs = [1500 + i * 200 for i in range(months)] # Storage, API gateways, anonymization pipelines
    
    for i in range(months):
        data_rev = oem_insights_rev[i] + api_access_rev[i] + benchmarking_rev[i]
        total_data_revenue.append(data_rev)
        
    sum_core = sum(core_hardware_saas_rev)
    sum_data = sum(total_data_revenue)
    sum_infra = sum(infra_costs)
    
    gross_margin = ((sum_data - sum_infra) / sum_data) * 100 if sum_data > 0 else 0
    data_share = (sum_data / (sum_core + sum_data)) * 100
    roi = ((sum_data - sum_infra) / sum_infra) * 100

    print("=== FINANCIAL MODEL RESULTS (24 MONTHS) ===")
    print(f"Total Core Revenue: ${sum_core:,.2f}")
    print(f"Total Data Revenue: ${sum_data:,.2f}")
    print(f"Data Infra Costs:   ${sum_infra:,.2f}")
    print(f"Data Share of Total: {data_share:.2f}%")
    print(f"Data Gross Margin:  {gross_margin:.2f}%")
    print(f"Data Product ROI:   {roi:.2f}%")

if __name__ == "__main__":
    calculate_data_monetization()