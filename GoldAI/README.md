# GoldAI Trader - Expert Advisor Backtest Results

## Overview

This repository contains backtesting results and analysis tools for the **GoldAITrader** Expert Advisor (EA) trading on XAUUSD (Gold).

## Backtest Summary

### Period
- **Timeframe**: M15 (15-minute)
- **Start Date**: 2024.01.01
- **End Date**: 2025.01.03
- **History Quality**: 100%

### Results Highlights

- **Total Net Profit**: 83.29 pips
- **Win Rate**: 93.10% (944 winning trades out of 1014)
- **Profit Factor**: 1.24
- **Sharpe Ratio**: 7.22 (excellent)
- **Max Drawdown**: 3.78% (balance), 3.87% (equity)
- **Recovery Factor**: 1.98

### Key Statistics

- **Total Trades**: 1,014
- **Winning Trades**: 944 (93.10%)
- **Losing Trades**: 70 (6.90%)
- **Average Profit Trade**: 0.45 pips
- **Average Loss Trade**: -4.86 pips
- **Largest Profit**: 5.88 pips
- **Largest Loss**: -12.84 pips
- **Max Consecutive Wins**: 54
- **Max Consecutive Losses**: 2

## Strategy Parameters

### Trading Settings
- Enable Trading: `true`
- Timeframe: `15` minutes
- Only One Position: `true`

### Indicators
- Fast EMA Period: `21`
- Slow EMA Period: `50`
- Trend EMA Period: `200`
- Use Higher Timeframe: `true`
- Higher Timeframe: `16388` (H4)

### Oscillators
- RSI Period: `14`
- CCI Period: `14`
- Momentum Period: `10`
- RSI Oversold: `30.0`
- RSI Overbought: `70.0`

### Risk Management
- Risk Percent: `1.0%`
- Use Fixed Lot: `false`
- Fixed Lot Size: `0.01`
- ATR Multiplier SL: `2.0x`
- ATR Multiplier TP: `3.0x`
- Max Daily Drawdown: `5.0%`
- Max Trades Per Day: `10`
- Max Loss Streak: `5`

### Trailing & Break Even
- Enable Break Even: `true`
- Break Even Trigger: `20.0` pips
- Break Even Pips: `10.0` pips
- Enable Trailing Stop: `true`
- Trailing Stop: `30.0` pips
- Trailing Step: `10.0` pips

### Trading Sessions
- London Session: `enabled`
- New York Session: `enabled`
- Asian Session: `disabled`
- Avoid Rollover: `true`

### Confidence System
- Min Confidence: `0.5`
- Agreement Weight: `0.3`
- Strength Weight: `0.3`
- Volatility Weight: `0.2`
- Trend Weight: `0.2`

## Analysis

### Strengths
1. **Excellent Win Rate**: 93.10% win rate is exceptional
2. **Low Drawdown**: Maximum drawdown of 3.78% is very manageable
3. **Strong Sharpe Ratio**: 7.22 indicates excellent risk-adjusted returns
4. **Consistent Performance**: High number of trades (1,014) with consistent results
5. **Good Recovery Factor**: 1.98 shows the strategy can recover from drawdowns

### Areas for Improvement
1. **Profit Factor**: 1.24 is positive but could be improved
2. **Average Risk-Reward**: Average loss (-4.86 pips) is larger than average win (0.45 pips)
3. **Limited Short Trades**: Only 1 short trade suggests potential bias or missed opportunities

### Recommendations
1. Consider optimizing the risk-reward ratio to improve profit factor
2. Review why short trades are so limited - may indicate bias or filter issues
3. The strategy shows strong performance but low average profit per trade - consider position sizing optimization
4. With such a high win rate, focus on maximizing profit on winning trades

## Files

- `backtest_results.json` - Structured JSON data of all backtest results
- `analyze_results.py` - Python script to analyze and visualize results
- `backtest_summary.csv` - CSV export of key metrics (generated)
- `charts/backtest_analysis.png` - Visualization charts (generated)

## Usage

### Analyze Results

```bash
python analyze_results.py
```

This will:
- Print a detailed summary of the backtest
- Generate visualization charts
- Export key metrics to CSV

### Requirements

```bash
pip install matplotlib pandas
```

## Broker Information

- **Company**: Pepperstone Limited
- **Initial Deposit**: $1,000.00
- **Leverage**: 1:100
- **Currency**: Profit measured in pips

## Notes

- Results are based on 100% quality historical data
- 23,819 bars and 37,488,020 ticks were processed
- Strategy uses a confidence-based entry system
- Multiple risk management features are enabled (break-even, trailing stop, daily limits)

---

*Last Updated: 2025-01-03*
