# GoldCruiseAI - AI-Enhanced Gold Trading Expert Advisor

<div align="center">

![GoldCruiseAI Logo](duplicate-reference-image.svg)

**Historical Backtest Results (2000-2025)**

[![MQL5 Marketplace](https://img.shields.io/badge/MQL5-Marketplace-00AEEF?style=for-the-badge&logo=metatrader)](https://www.mql5.com/en/market/product/158880)
[![Version](https://img.shields.io/badge/Version-1.0-green?style=for-the-badge)](https://github.com/EridianLabs/GoldCruiseAI)
[![License](https://img.shields.io/badge/License-Commercial-red?style=for-the-badge)](LICENSE)

[Documentation](docs/) • [Set Files](setfiles/) • [Support](docs/support.md) • [Purchase on MQL5](https://www.mql5.com/en/market/product/158880)

</div>

---

## Historical Backtest Results (2000-2025)

**Disclaimer:** All metrics shown are from historical backtesting. Past performance does not guarantee future results. Trading involves substantial risk of loss.

| Metric | Value | Source |
|--------|-------|--------|
| **Profit Factor** | 5.60 | Backtest (2000-2025) |
| **Win Rate** | 93.93% | Backtest (2000-2025) |
| **Sharpe Ratio** | 65.94 | Backtest (2000-2025) |
| **Max Drawdown** | 0.68% | Backtest (2000-2025) |
| **Recovery Factor** | 62.62 | Backtest (2000-2025) |
| **Total Profit** | 775.85 pips | Backtest period |
| **Average Profit** | 1.61 pips per trade | Backtest period |

---

## 🎯 Key Features

### Confidence Scoring System
Evaluates trade setups using weighted technical indicators (RSI, CCI, Momentum, EMA trends). Only trades above configured confidence thresholds are executed.

### Risk Management Controls
Configurable risk management features:
- Daily drawdown limits
- Loss streak protection
- Position sizing (percentage-based or fixed lot)
- Break-even and trailing stop options

### Long and Short Trading
Trades both directions. In backtesting, 44.7% of trades were short positions. Performance varies with market conditions.

### Session Filtering
Trading can be limited to London and New York sessions. Asian session trading is optional. Rollover periods can be avoided.

### Position Sizing Options
Supports percentage-based risk (e.g., 1% of account per trade) or fixed lot sizes. Optional confidence-based multiplier adjusts size based on trade quality score.

### 📦 Multiple Risk Profiles Included
6 pre-configured set files for different risk levels (Conservative, Moderate, Aggressive, Maximum Profit variants).

---

## 🔧 Technical Specifications

- **Symbol:** XAUUSD (Gold)
- **Timeframe:** M15 (15-minute charts)
- **Minimum Deposit:** $500 recommended
- **Account Type:** Any (Standard, ECN, etc.)
- **Leverage:** Works with any leverage (1:100 recommended)
- **No External Dependencies:** No API keys, no internet required, works offline

---

## 📈 Strategy Overview

GoldCruiseAI uses a multi-layered approach combining:

- **Trend Analysis:** Fast EMA (21), Slow EMA (50), Trend EMA (200)
- **Momentum Confirmation:** RSI, CCI, Momentum indicators
- **Higher Timeframe Filter:** H4 trend confirmation for better accuracy
- **Volatility Assessment:** ATR-based stop loss and take profit
- **Confidence Scoring:** Weighted evaluation of multiple factors

Trades are only executed when multiple conditions meet configured thresholds. All parameters are adjustable.

---

## 🚀 Quick Start

### 1. Purchase & Download
- [Purchase on MQL5 Marketplace](https://www.mql5.com/en/market/product/158880)
- Download the EA file (`GoldCruiseAI.ex5`)

### 2. Install
1. Open MetaTrader 5
2. Go to `File → Open Data Folder`
3. Navigate to `MQL5 → Experts`
4. Copy `GoldCruiseAI.ex5` to this folder
5. Restart MT5

### 3. Configure
1. Attach EA to XAUUSD M15 chart
2. [Download a risk profile set file](setfiles/)
3. Load the set file in EA inputs
4. Enable AutoTrading

### 4. Monitor
- Monitor trades in the Terminal
- Check logs (if file logging enabled)
- Review performance regularly

---

## 📦 What's Included

- ✅ **GoldCruiseAI.ex5** (Compiled Expert Advisor)
- ✅ **6 Risk Profile Set Files:**
  - Conservative (0.5% risk, very safe)
  - Moderate (1.0% risk, recommended)
  - Aggressive (2.0% risk, higher returns)
  - MaxProfit_2Percent (2% risk, 2x profit)
  - MaxProfit_3Percent (3% risk, 3x profit)
  - FixedLot_0.01 (Fixed 0.01 lot, for small accounts)
- ✅ **Documentation:**
  - [Quick Start Guide](docs/quick-start.md)
  - [Parameter Guide](docs/parameters.md)
  - [Performance Summary](docs/performance.md)
  - [Support & FAQ](docs/support.md)

---

## 📊 Backtest Results Summary

**Period:** 2000-2025 (25 years)  
**Total Trades:** 626 (quality over quantity)  
**Win Rate:** 93.93%  
**Profit Factor:** 5.60  
**Max Drawdown:** 0.68%  
**Sharpe Ratio:** 65.94  
**Total Net Profit:** 775.85 pips  
**Average Profit:** 1.61 pips per trade  
**Average Loss:** -4.44 pips per trade  

**Long Trades:** 346 (55.3%) - Win Rate: 92.20%  
**Short Trades:** 280 (44.7%) - Win Rate: 96.07%

The strategy has been validated across multiple market cycles including bull markets, bear markets, and ranging conditions, proving its robustness and reliability.

---

## 💡 Perfect For

- ✅ Traders interested in automated gold trading
- ✅ Risk-averse investors wanting low drawdown strategies
- ✅ Gold (XAUUSD) traders looking for automation
- ✅ Those who value high win rates over high frequency
- ✅ Traders wanting a "set and forget" solution
- ✅ Anyone looking for proven, long-term strategies

---

## 🎓 Suitable For All Experience Levels

- **Beginners:** Conservative set file with fixed 0.01 lot
- **Intermediate Traders:** Moderate set file (recommended)
- **Advanced Traders:** Aggressive or Maximum Profit set files
- **All Experience Levels:** Multiple risk profiles included

---

## ⚠️ Important Risk Warnings

- ⚠️ Trading involves substantial risk of loss
- ⚠️ Past performance does not guarantee future results
- ⚠️ Always test on demo account before live trading
- ⚠️ Never risk more than you can afford to lose
- ⚠️ Results may vary based on broker, spread, and market conditions
- ⚠️ Use proper risk management and position sizing
- ⚠️ Monitor your account regularly

---

## 📞 Support & Resources

- 📖 [Full Documentation](docs/)
- ❓ [Support & FAQ](docs/support.md)
- 📁 [Set Files Download](setfiles/)
- 🎯 [Quick Start Guide](docs/quick-start.md)
- ⚙️ [Parameter Guide](docs/parameters.md)

---

## 🔒 No Hidden Requirements

- ✅ No API keys needed
- ✅ No external services required
- ✅ No internet connection needed (works offline)
- ✅ No monthly fees (one-time purchase)
- ✅ No restrictions on account type or broker

---

## 💰 Pricing

- **Unlimited Use:** $599 (one-time purchase)
- **1 Month Rent:** $99 (try before you buy)
- **All set files and documentation included**

[👉 Purchase on MQL5 Marketplace](https://www.mql5.com/en/market/product/158880)

---

## 📝 License

This is a commercial product. See [LICENSE](LICENSE) for details.

---

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=EridianLabs/GoldCruiseAI&type=Date)](https://star-history.com/#EridianLabs/GoldCruiseAI&Date)

---

<div align="center">

**GoldCruiseAI is available on the MQL5 Marketplace. Always test on a demo account before live trading.**

[![MQL5 Marketplace](https://img.shields.io/badge/Buy_on_MQL5-00AEEF?style=for-the-badge&logo=metatrader)](https://www.mql5.com/en/market/product/158880)

Made with ❤️ by [EridianLabs](https://github.com/EridianLabs)

</div>

