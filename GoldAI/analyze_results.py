#!/usr/bin/env python3
"""
GoldAITrader Backtest Results Analyzer
Analyzes and visualizes backtesting results for the GoldAI trading expert advisor.
"""

import json
from datetime import datetime
from pathlib import Path

# Optional imports with graceful fallback
try:
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False

try:
    import pandas as pd
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False


def load_results(file_path="backtest_results.json"):
    """Load backtesting results from JSON file."""
    with open(file_path, 'r') as f:
        return json.load(f)


def print_summary(data):
    """Print a formatted summary of the backtesting results."""
    results = data['results']
    inputs = data['inputs']
    
    print("=" * 80)
    print(f"BACKTEST SUMMARY: {data['expert']}")
    print("=" * 80)
    print(f"\nSymbol: {data['symbol']}")
    print(f"Period: {data['period']['start_date']} to {data['period']['end_date']}")
    print(f"Timeframe: {data['period']['timeframe']}")
    print(f"Broker: {data['broker']['company']}")
    print(f"Initial Deposit: ${data['broker']['initial_deposit']:,.2f}")
    print(f"Leverage: {data['broker']['leverage']}")
    
    print("\n" + "-" * 80)
    print("PROFIT & LOSS")
    print("-" * 80)
    pl = results['profit_loss']
    print(f"Total Net Profit: {pl['total_net_profit']:.2f} pips")
    print(f"Gross Profit: {pl['gross_profit']:.2f} pips")
    print(f"Gross Loss: {pl['gross_loss']:.2f} pips")
    print(f"Profit Factor: {pl['profit_factor']:.2f}")
    print(f"Expected Payoff: {pl['expected_payoff']:.2f} pips")
    
    print("\n" + "-" * 80)
    print("RISK METRICS")
    print("-" * 80)
    dd = results['drawdown']
    print(f"Max Balance Drawdown: {dd['balance_drawdown_maximal']:.2f} pips ({dd['balance_drawdown_maximal_percent']:.2f}%)")
    print(f"Max Equity Drawdown: {dd['equity_drawdown_maximal']:.2f} pips ({dd['equity_drawdown_maximal_percent']:.2f}%)")
    rm = results['risk_metrics']
    print(f"Recovery Factor: {rm['recovery_factor']:.2f}")
    print(f"Sharpe Ratio: {rm['sharpe_ratio']:.2f}")
    print(f"Z-Score: {rm['z_score']:.2f} ({rm['z_score_percentile']:.2f}%)")
    
    print("\n" + "-" * 80)
    print("TRADE STATISTICS")
    print("-" * 80)
    trades = results['trades']
    print(f"Total Trades: {trades['total_trades']}")
    print(f"Win Rate: {trades['profit_trades_percent']:.2f}%")
    print(f"Winning Trades: {trades['profit_trades']}")
    print(f"Losing Trades: {trades['loss_trades']}")
    print(f"Long Trades: {trades['long_trades']} ({trades['long_trades_win_percent']:.2f}% win rate)")
    print(f"Short Trades: {trades['short_trades']} ({trades['short_trades_win_percent']:.2f}% win rate)")
    
    ts = results['trade_statistics']
    print(f"\nAverage Profit Trade: {ts['average_profit_trade']:.2f} pips")
    print(f"Average Loss Trade: {ts['average_loss_trade']:.2f} pips")
    print(f"Largest Profit: {ts['largest_profit_trade']:.2f} pips")
    print(f"Largest Loss: {ts['largest_loss_trade']:.2f} pips")
    print(f"Max Consecutive Wins: {ts['maximum_consecutive_wins']}")
    print(f"Max Consecutive Losses: {ts['maximum_consecutive_losses']}")
    
    print("\n" + "-" * 80)
    print("KEY PARAMETERS")
    print("-" * 80)
    print(f"Risk per Trade: {inputs['risk_management']['InpRiskPercent']:.1f}%")
    print(f"ATR SL Multiplier: {inputs['risk_management']['InpATRMultiplierSL']:.1f}x")
    print(f"ATR TP Multiplier: {inputs['risk_management']['InpATRMultiplierTP']:.1f}x")
    print(f"Fast EMA: {inputs['indicators']['InpFastEMAPeriod']}")
    print(f"Slow EMA: {inputs['indicators']['InpSlowEMAPeriod']}")
    print(f"Trend EMA: {inputs['indicators']['InpTrendEMAPeriod']}")
    print(f"RSI Period: {inputs['oscillators']['InpRSIPeriod']}")
    print(f"Min Confidence: {inputs['confidence']['InpMinConfidence']:.2f}")
    
    print("\n" + "=" * 80)
    
    # Calculate additional metrics
    print("\nANALYSIS:")
    print("-" * 80)
    
    # Risk-Reward Analysis
    avg_win = ts['average_profit_trade']
    avg_loss = abs(ts['average_loss_trade'])
    risk_reward = avg_win / avg_loss if avg_loss > 0 else 0
    print(f"Average Risk-Reward Ratio: {risk_reward:.2f}:1")
    
    # Win rate vs Profit Factor analysis
    win_rate = trades['profit_trades_percent'] / 100
    pf = pl['profit_factor']
    print(f"Win Rate: {win_rate*100:.2f}% | Profit Factor: {pf:.2f}")
    
    if win_rate > 0.9 and pf > 1.2:
        print("✓ Excellent: High win rate with good profit factor")
    elif win_rate > 0.8 and pf > 1.1:
        print("✓ Good: Solid win rate with positive profit factor")
    else:
        print("⚠ Review: Consider optimizing strategy parameters")
    
    # Drawdown analysis
    if dd['balance_drawdown_maximal_percent'] < 5:
        print(f"✓ Low Drawdown: {dd['balance_drawdown_maximal_percent']:.2f}% is acceptable")
    else:
        print(f"⚠ High Drawdown: {dd['balance_drawdown_maximal_percent']:.2f}% may need attention")
    
    # Sharpe Ratio analysis
    if rm['sharpe_ratio'] > 3:
        print(f"✓ Excellent Sharpe Ratio: {rm['sharpe_ratio']:.2f} indicates strong risk-adjusted returns")
    elif rm['sharpe_ratio'] > 1:
        print(f"✓ Good Sharpe Ratio: {rm['sharpe_ratio']:.2f} indicates acceptable risk-adjusted returns")
    else:
        print(f"⚠ Low Sharpe Ratio: {rm['sharpe_ratio']:.2f} may need improvement")
    
    print("=" * 80)


def create_visualizations(data, output_dir="charts"):
    """Create visualization charts for the backtesting results."""
    if not HAS_MATPLOTLIB:
        print("\n⚠ Matplotlib not available. Skipping visualizations.")
        print("   Install with: pip install matplotlib")
        return
    
    Path(output_dir).mkdir(exist_ok=True)
    results = data['results']
    
    # Create a figure with subplots
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle(f"{data['expert']} - Backtest Analysis", fontsize=16, fontweight='bold')
    
    # 1. Win/Loss Distribution
    ax1 = axes[0, 0]
    trades = results['trades']
    labels = ['Winning Trades', 'Losing Trades']
    sizes = [trades['profit_trades'], trades['loss_trades']]
    colors = ['#2ecc71', '#e74c3c']
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
    ax1.set_title('Win/Loss Distribution')
    
    # 2. Trade Statistics Comparison
    ax2 = axes[0, 1]
    ts = results['trade_statistics']
    categories = ['Avg Profit', 'Avg Loss', 'Largest Profit', 'Largest Loss']
    values = [
        ts['average_profit_trade'],
        ts['average_loss_trade'],
        ts['largest_profit_trade'],
        ts['largest_loss_trade']
    ]
    colors_bar = ['#2ecc71', '#e74c3c', '#27ae60', '#c0392b']
    bars = ax2.bar(categories, values, color=colors_bar)
    ax2.set_title('Trade Statistics (pips)')
    ax2.set_ylabel('Pips')
    ax2.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    ax2.grid(axis='y', alpha=0.3)
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.2f}',
                ha='center', va='bottom' if height > 0 else 'top')
    
    # 3. Key Metrics
    ax3 = axes[1, 0]
    metrics = ['Profit\nFactor', 'Sharpe\nRatio', 'Recovery\nFactor', 'Win Rate\n(%)']
    values_metrics = [
        results['profit_loss']['profit_factor'],
        results['risk_metrics']['sharpe_ratio'],
        results['risk_metrics']['recovery_factor'],
        results['trades']['profit_trades_percent'] / 10  # Scale down for visualization
    ]
    bars2 = ax3.bar(metrics, values_metrics, color=['#3498db', '#9b59b6', '#f39c12', '#1abc9c'])
    ax3.set_title('Key Performance Metrics')
    ax3.set_ylabel('Value')
    ax3.grid(axis='y', alpha=0.3)
    
    # Add value labels
    for i, (bar, val) in enumerate(zip(bars2, values_metrics)):
        if i == 3:  # Win rate needs different scaling
            val_label = results['trades']['profit_trades_percent']
        else:
            val_label = val
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height,
                f'{val_label:.2f}',
                ha='center', va='bottom')
    
    # 4. Drawdown Analysis
    ax4 = axes[1, 1]
    dd = results['drawdown']
    dd_types = ['Balance\nDrawdown', 'Equity\nDrawdown']
    dd_values = [
        dd['balance_drawdown_maximal_percent'],
        dd['equity_drawdown_maximal_percent']
    ]
    bars3 = ax4.bar(dd_types, dd_values, color=['#e67e22', '#d35400'])
    ax4.set_title('Maximum Drawdown (%)')
    ax4.set_ylabel('Percentage')
    ax4.grid(axis='y', alpha=0.3)
    
    # Add value labels
    for bar, val in zip(bars3, dd_values):
        height = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width()/2., height,
                f'{val:.2f}%',
                ha='center', va='bottom')
    
    plt.tight_layout()
    output_path = f"{output_dir}/backtest_analysis.png"
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"\n✓ Charts saved to: {output_path}")
    plt.close()


def export_to_csv(data, output_file="backtest_summary.csv"):
    """Export key metrics to CSV for further analysis."""
    if not HAS_PANDAS:
        print("\n⚠ Pandas not available. Skipping CSV export.")
        print("   Install with: pip install pandas")
        return
    
    results = data['results']
    
    summary_data = {
        'Metric': [
            'Total Net Profit (pips)',
            'Gross Profit (pips)',
            'Gross Loss (pips)',
            'Profit Factor',
            'Win Rate (%)',
            'Total Trades',
            'Winning Trades',
            'Losing Trades',
            'Average Profit (pips)',
            'Average Loss (pips)',
            'Largest Profit (pips)',
            'Largest Loss (pips)',
            'Max Drawdown (%)',
            'Sharpe Ratio',
            'Recovery Factor',
            'Z-Score'
        ],
        'Value': [
            results['profit_loss']['total_net_profit'],
            results['profit_loss']['gross_profit'],
            results['profit_loss']['gross_loss'],
            results['profit_loss']['profit_factor'],
            results['trades']['profit_trades_percent'],
            results['trades']['total_trades'],
            results['trades']['profit_trades'],
            results['trades']['loss_trades'],
            results['trade_statistics']['average_profit_trade'],
            results['trade_statistics']['average_loss_trade'],
            results['trade_statistics']['largest_profit_trade'],
            results['trade_statistics']['largest_loss_trade'],
            results['drawdown']['balance_drawdown_maximal_percent'],
            results['risk_metrics']['sharpe_ratio'],
            results['risk_metrics']['recovery_factor'],
            results['risk_metrics']['z_score']
        ]
    }
    
    df = pd.DataFrame(summary_data)
    df.to_csv(output_file, index=False)
    print(f"✓ Summary exported to: {output_file}")


def main():
    """Main function to run the analysis."""
    print("GoldAITrader Backtest Results Analyzer")
    print("=" * 80)
    
    try:
        data = load_results()
        print_summary(data)
        
        # Create visualizations if matplotlib is available
        create_visualizations(data)
        
        # Export to CSV if pandas is available
        export_to_csv(data)
            
    except FileNotFoundError:
        print("Error: backtest_results.json not found!")
    except json.JSONDecodeError:
        print("Error: Invalid JSON in backtest_results.json!")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

