# ⚙️ Parameter Guide - GoldCruiseAI

Complete guide to all GoldCruiseAI input parameters.

---

## 📋 Parameter Categories

### 1. Trading Settings

| Parameter | Default | Description |
|-----------|---------|-------------|
| `InpEnableTrading` | `true` | Enable/disable trading. Set to `false` to disable all trades. |
| `InpTimeframe` | `15` | Trading timeframe in minutes. **Recommended: 15 (M15)** |
| `InpOnlyOnePosition` | `true` | Allow only one position at a time. Prevents over-trading. |

---

### 2. Trend Filter Settings

| Parameter | Default | Description |
|-----------|---------|-------------|
| `InpFastEMAPeriod` | `21` | Fast EMA period for trend detection. Lower = more sensitive. |
| `InpSlowEMAPeriod` | `50` | Slow EMA period for trend confirmation. |
| `InpTrendEMAPeriod` | `200` | Long-term trend EMA. Identifies major trend direction. |
| `InpUseHigherTimeframe` | `true` | Use higher timeframe filter for better accuracy. **Recommended: true** |
| `InpHigherTimeframe` | `H4` | Higher timeframe for trend confirmation. Options: H1, H4, D1 |

---

### 3. Momentum Filter Settings

| Parameter | Default | Description |
|-----------|---------|-------------|
| `InpRSIPeriod` | `14` | RSI indicator period. Standard: 14. |
| `InpCCIPeriod` | `14` | CCI indicator period. |
| `InpMomentumPeriod` | `10` | Momentum indicator period. |
| `InpRSIOversold` | `30.0` | RSI oversold level. Below this = potential buy signal. |
| `InpRSIOverbought` | `70.0` | RSI overbought level. Above this = potential sell signal. |

---

### 4. Volatility Filter Settings

| Parameter | Default | Description |
|-----------|---------|-------------|
| `InpATRPeriod` | `14` | ATR period for volatility calculation. Used for SL/TP. |
| `InpMinVolatility` | `0.0` | Minimum ATR (0 = disabled). Skip trades if volatility too low. |
| `InpMaxVolatility` | `0.0` | Maximum ATR (0 = disabled). Skip trades if volatility too high. |

---

### 5. Risk Management

| Parameter | Default | Description |
|-----------|---------|-------------|
| `InpRiskPercent` | `1.0` | Risk per trade as % of account balance. **Recommended: 0.5-2.0%** |
| `InpUseFixedLot` | `false` | Use fixed lot size instead of percentage-based. |
| `InpFixedLotSize` | `0.01` | Fixed lot size (if `InpUseFixedLot = true`). |
| `InpATRMultiplierSL` | `2.0` | ATR multiplier for stop loss. Higher = wider stops. |
| `InpATRMultiplierTP` | `4.0` | ATR multiplier for take profit. Higher = wider targets. |
| `InpMaxDailyDrawdown` | `5.0` | Maximum daily drawdown %. EA stops trading if exceeded. |
| `InpMaxTradesPerDay` | `10` | Maximum trades per day. Prevents over-trading. |
| `InpMaxLossStreak` | `5` | Maximum consecutive losses before auto-disable. |
| `InpUseConfidenceBasedSizing` | `true` | Adjust position size based on trade confidence. |
| `InpMinConfidenceForSizing` | `0.5` | Minimum confidence for base position size. |
| `InpMaxConfidenceMultiplier` | `2.0` | Maximum position size multiplier for high confidence. |

---

### 6. Break-Even & Trailing

| Parameter | Default | Description |
|-----------|---------|-------------|
| `InpEnableBreakEven` | `true` | Enable automatic break-even. Moves SL to entry when profit reached. |
| `InpBreakEvenTriggerPips` | `20.0` | Profit in pips to trigger break-even. |
| `InpBreakEvenPips` | `10.0` | Move SL to this many pips above/below entry. |
| `InpEnableTrailingStop` | `true` | Enable trailing stop loss. |
| `InpTrailingStopPips` | `30.0` | Trailing stop distance in pips. |
| `InpTrailingStepPips` | `10.0` | Trailing stop step in pips. How often to update. |
| `InpEnablePartialProfit` | `false` | Enable partial profit taking. **Currently disabled** |
| `InpUseTrailingTP` | `true` | Use trailing take profit. |

---

### 7. Session Filter

| Parameter | Default | Description |
|-----------|---------|-------------|
| `InpEnableLondonSession` | `true` | Enable trading during London session. **Recommended: true** |
| `InpEnableNewYorkSession` | `true` | Enable trading during New York session. **Recommended: true** |
| `InpEnableAsianSession` | `false` | Enable trading during Asian session. Usually lower volatility. |
| `InpAvoidRollover` | `true` | Avoid trading during rollover time. **Recommended: true** |

---

### 8. News Filter

| Parameter | Default | Description |
|-----------|---------|-------------|
| `InpEnableNewsFilter` | `false` | Enable news filter. **Currently disabled** |
| `InpNewsAvoidMinutesBefore` | `30` | Minutes before news to avoid trading. |
| `InpNewsAvoidMinutesAfter` | `30` | Minutes after news to avoid trading. |

---

### 9. AI Confidence Engine

| Parameter | Default | Description |
|-----------|---------|-------------|
| `InpMinConfidence` | `0.5` | Minimum confidence for long trades (0.0-1.0). Higher = fewer trades. |
| `InpMinConfidenceShort` | `0.32` | Minimum confidence for short trades. Lower threshold for shorts. |
| `InpConfidenceAgreementWeight` | `0.3` | Weight for indicator agreement in confidence calculation. |
| `InpConfidenceStrengthWeight` | `0.3` | Weight for signal strength in confidence calculation. |
| `InpConfidenceVolatilityWeight` | `0.2` | Weight for volatility in confidence calculation. |
| `InpConfidenceTrendWeight` | `0.2` | Weight for trend in confidence calculation. |
| `InpRelaxHTFFilterForShorts` | `true` | Relax higher timeframe filter for short trades. |

---

### 10. Logging

| Parameter | Default | Description |
|-----------|---------|-------------|
| `InpEnableFileLogging` | `true` | Enable logging to file. Creates logs in `GoldAI_Logs/` folder. |
| `InpEnableConsoleLogging` | `true` | Enable console logging. Shows messages in Experts tab. |

---

## 💡 Recommended Settings by Account Size

### Small Account ($500-$1,000):
```
InpRiskPercent = 0.5
InpUseFixedLot = true
InpFixedLotSize = 0.01
InpMaxDailyDrawdown = 3.0
InpMaxTradesPerDay = 8
```
**Use:** Conservative.set or FixedLot_0.01.set

---

### Medium Account ($1,000-$5,000):
```
InpRiskPercent = 1.0
InpUseFixedLot = false
InpATRMultiplierSL = 2.0
InpATRMultiplierTP = 4.0
InpMaxDailyDrawdown = 5.0
InpMaxTradesPerDay = 10
```
**Use:** Moderate.set ⭐ **RECOMMENDED**

---

### Large Account ($5,000+):
```
InpRiskPercent = 2.0
InpMaxDailyDrawdown = 7.0
InpMaxTradesPerDay = 15
```
**Use:** Aggressive.set or MaxProfit variants

---

## ⚙️ Advanced Configuration

### Confidence Tuning:

**For More Trades:**
- Lower `InpMinConfidence` (e.g., 0.45)
- Lower `InpMinConfidenceShort` (e.g., 0.30)
- Lower confidence weights

**For Fewer, Higher Quality Trades:**
- Higher `InpMinConfidence` (e.g., 0.55)
- Higher `InpMinConfidenceShort` (e.g., 0.35)
- Higher confidence weights

### Risk Tuning:

**More Conservative:**
- Lower `InpRiskPercent` (0.5%)
- Higher `InpATRMultiplierSL` (2.5)
- Lower `InpMaxDailyDrawdown` (3.0%)

**More Aggressive:**
- Higher `InpRiskPercent` (2.0%)
- Lower `InpATRMultiplierSL` (1.75)
- Higher `InpMaxDailyDrawdown` (7.0%)

---

## 📊 Parameter Impact Summary

| Parameter | Impact on Trades | Impact on Risk |
|-----------|------------------|---------------|
| `InpMinConfidence` | Lower = more trades | Higher = safer |
| `InpRiskPercent` | No impact | Higher = more risk |
| `InpATRMultiplierSL` | No impact | Higher = wider stops |
| `InpATRMultiplierTP` | No impact | Higher = wider targets |
| `InpMaxTradesPerDay` | Limits trade count | Limits exposure |
| `InpMaxDailyDrawdown` | Stops trading if exceeded | Protects account |

---

## ⚠️ Important Notes

1. **Never change parameters without testing:**
   - Always test on demo first
   - Use Strategy Tester to validate changes
   - Monitor performance after changes

2. **Start with defaults:**
   - Use provided set files
   - Only adjust if you understand the impact
   - Document your changes

3. **Risk management is critical:**
   - Never risk more than you can afford
   - Use appropriate `InpRiskPercent`
   - Set proper `InpMaxDailyDrawdown`

---

## 📞 Need Help?

- 📖 [Quick Start Guide](quick-start.html)
- ❓ [Support & FAQ](support.html)
- 📁 [Set Files](../setfiles/)

---

*Parameter Guide - Updated 2025-12-19*

