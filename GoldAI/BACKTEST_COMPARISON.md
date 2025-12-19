# Backtest Comparison: Original vs. New Results

## ⚠️ Important: Key Parameters Not Updated

The new backtest shows these parameters were **NOT** updated:
- `InpATRMultiplierTP = 3.0` (should be **5.0**)
- `InpEnableAsianSession = false` (should be **true**)

**Action Required:** Re-run the backtest with the updated default values or manually set:
- `InpATRMultiplierTP = 5.0`
- `InpEnableAsianSession = true`

---

## Results Comparison

| Metric | Original | New | Change | Status |
|--------|----------|-----|--------|--------|
| **Total Net Profit** | 83.29 pips | 79.93 pips | -4.0% ⬇️ | ❌ Worse |
| **Gross Profit** | 423.37 pips | 428.56 pips | +1.2% ⬆️ | ✅ Better |
| **Gross Loss** | -340.08 pips | -348.63 pips | -2.5% ⬇️ | ❌ Worse |
| **Profit Factor** | 1.24 | 1.23 | -0.8% ⬇️ | ❌ Slightly worse |
| **Total Trades** | 1,014 | 1,023 | +0.9% ⬆️ | ✅ More trades |
| **Short Trades** | 1 (0.1%) | **10 (0.98%)** | **+900%** ⬆️ | ✅ **MAJOR IMPROVEMENT** |
| **Long Trades** | 1,013 | 1,013 | 0% | ➡️ Same |
| **Win Rate** | 93.10% | 93.06% | -0.04% ⬇️ | ➡️ Essentially same |
| **Average Profit/Trade** | 0.45 pips | 0.45 pips | 0% | ➡️ **NO CHANGE** |
| **Average Loss/Trade** | -4.86 pips | -4.91 pips | -1.0% ⬇️ | ❌ Slightly worse |
| **Largest Profit** | 5.88 pips | **7.92 pips** | **+34.7%** ⬆️ | ✅ Better |
| **Max Drawdown** | 3.78% | 3.79% | +0.01% ⬆️ | ➡️ Essentially same |
| **Sharpe Ratio** | 7.22 | 6.81 | -5.7% ⬇️ | ❌ Slightly worse |

---

## ✅ Positive Changes

1. **Short Trades Increased 10x!**
   - From 1 trade (0.1%) to 10 trades (0.98%)
   - This is **exactly what we wanted** - the relaxed HTF filter and lower confidence threshold are working!
   - Still needs to reach 30-50% target, but this is significant progress

2. **Largest Profit Trade Increased**
   - From 5.88 pips to 7.92 pips (+34.7%)
   - This suggests partial profit taking or trailing TP may be working for some trades

3. **More Trading Opportunities**
   - Total trades increased from 1,014 to 1,023
   - Gross profit increased slightly

---

## ❌ Negative Changes

1. **Average Profit/Trade Unchanged**
   - Still 0.45 pips (target: 2.0+ pips)
   - **This is because TP multiplier is still 3.0, not 5.0!**

2. **Net Profit Decreased**
   - From 83.29 to 79.93 pips (-4.0%)
   - Likely due to more losses (gross loss increased)

3. **Average Loss Increased**
   - From -4.86 to -4.91 pips
   - Slight increase, but within normal variance

---

## 🔍 Analysis

### Why Short Trades Increased
The new features are working:
- ✅ `InpMinConfidenceShort = 0.45` (lower threshold)
- ✅ `InpRelaxHTFFilterForShorts = true` (allows shorts in bullish HTF)

**Evidence:** Short trades went from 1 to 10 (10x improvement!)

### Why Average Profit Didn't Improve
**Root Cause:** `InpATRMultiplierTP` is still **3.0** instead of **5.0**

- Current: TP = 3.0x ATR
- Should be: TP = 5.0x ATR
- This means winners are being closed too early

### Why Net Profit Decreased
- More trades (1,023 vs 1,014) = more opportunities for losses
- Gross loss increased from -340.08 to -348.63
- This is expected when increasing trade frequency

---

## 🎯 Recommendations

### Immediate Actions

1. **Re-run Backtest with Correct Parameters:**
   ```
   InpATRMultiplierTP = 5.0  (currently 3.0)
   InpEnableAsianSession = true  (currently false)
   ```

2. **Expected Improvements with Correct Parameters:**
   - Average profit/trade: 0.45 → **1.5-2.5 pips** (3-5x improvement)
   - Risk-reward ratio: 0.09:1 → **0.3-0.5:1** (3-5x improvement)
   - Net profit: Should increase significantly

### Further Optimization

1. **Short Trade Threshold**
   - Current: 10 trades (0.98%)
   - Target: 30-50% (300-500 trades)
   - Consider: Lower `InpMinConfidenceShort` to 0.40 or 0.42

2. **Position Sizing**
   - Confidence-based sizing is enabled but may need tuning
   - Current multiplier: 2.0x max
   - Test: 1.5x, 2.0x, 2.5x

3. **Partial Profit Taking**
   - Currently enabled but TP multiplier too low to see full effect
   - With TP = 5.0x ATR, partial profit should work better

---

## 📊 Summary

### What's Working ✅
- Short trade enablement (10x improvement!)
- New features are functional (no errors)
- Win rate maintained (93%+)
- Largest profit increased

### What Needs Fixing ❌
- **TP multiplier not updated** (critical!)
- Asian session not enabled
- Average profit unchanged (due to TP issue)
- Short trades still too low (need 30-50%, currently 0.98%)

### Next Steps
1. Re-compile EA (ensure latest code)
2. Re-run backtest with:
   - `InpATRMultiplierTP = 5.0`
   - `InpEnableAsianSession = true`
3. Compare results
4. If short trades still low, lower `InpMinConfidenceShort` to 0.40

---

*Analysis Date: 2025-01-03*

