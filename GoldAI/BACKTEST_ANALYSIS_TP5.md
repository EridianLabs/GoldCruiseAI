# Backtest Analysis: TP=5.0 + Asian Session Enabled

## ⚠️ Unexpected Results - Performance Degraded

### Key Findings

The wider TP (5.0) and Asian session actually **worsened** performance:

| Metric | Original | TP=3.0 (Previous) | TP=5.0 (Current) | Change vs Original |
|--------|----------|-------------------|-------------------|---------------------|
| **Total Net Profit** | 83.29 | 79.93 | **67.54** | **-18.9%** ❌ |
| **Gross Profit** | 423.37 | 428.56 | **479.41** | **+13.2%** ✅ |
| **Gross Loss** | -340.08 | -348.63 | **-411.87** | **-21.1%** ❌ |
| **Profit Factor** | 1.24 | 1.23 | **1.16** | **-6.5%** ❌ |
| **Total Trades** | 1,014 | 1,023 | **1,260** | **+24.2%** ⚠️ |
| **Short Trades** | 1 (0.1%) | 10 (0.98%) | **13 (1.03%)** | Still too low |
| **Win Rate** | 93.10% | 93.06% | **91.98%** | **-1.1%** ❌ |
| **Avg Profit/Trade** | 0.45 | 0.45 | **0.41** | **-8.9%** ❌ |
| **Avg Loss/Trade** | -4.86 | -4.91 | **-4.08** | **+16.0%** ✅ |
| **Max Drawdown** | 3.78% | 3.79% | **4.17%** | **+10.3%** ❌ |
| **Sharpe Ratio** | 7.22 | 6.81 | **4.62** | **-36.0%** ❌ |

---

## 🔍 Root Cause Analysis

### Why Average Profit Decreased (0.45 → 0.41)?

**Expected:** Wider TP (5.0) should increase average profit  
**Reality:** Average profit decreased

**Possible Reasons:**

1. **More Trades = More Small Wins**
   - Total trades: 1,014 → 1,260 (+246 trades)
   - Asian session added many marginal trades
   - These trades may be hitting TP1 (2x ATR) but not TP2 (4x ATR)
   - Partial profit taking closes at 2x ATR, reducing average

2. **Partial Profit Taking Too Aggressive**
   - TP1 at 2x ATR closes 50% of position
   - This locks in small profits early
   - Remaining 50% may not reach TP2 (4x ATR)
   - Result: Average profit decreases

3. **Win Rate Decreased**
   - 93.10% → 91.98% (-1.1%)
   - More trades = more opportunities for losses
   - Asian session may have lower quality setups

4. **TP Too Wide - Trades Reversing**
   - TP at 5x ATR may be too far
   - Price reaches 2-3x ATR, then reverses
   - Partial profit takes 50% at 2x, but remaining 50% hits SL
   - Net result: Lower average profit

### Why Gross Loss Increased?

- **More trades** (1,260 vs 1,014) = more losing trades
- **Lower win rate** (91.98% vs 93.10%) = more losses
- **Average loss improved** (-4.08 vs -4.86), but volume of losses increased

### Why Short Trades Still Low?

- Only 13 shorts out of 1,260 (1.03%)
- Target: 30-50% (378-630 trades)
- **Still 30x below target!**

**Possible Issues:**
1. Confidence threshold still too high (0.45)
2. Trend filter still too restrictive
3. Momentum filter biased toward longs
4. Market was mostly bullish in 2024

---

## 💡 Solutions

### Option 1: Adjust Partial Profit Taking

**Problem:** Partial profit at 2x ATR is too aggressive  
**Solution:** Adjust levels

```
Current:
- TP1: 2.0x ATR (close 50%)
- TP2: 4.0x ATR (close 30%)

Test:
- TP1: 3.0x ATR (close 30%)  ← Less aggressive
- TP2: 5.0x ATR (close 20%)  ← Let more run
- Remaining 50%: Trailing TP
```

### Option 2: Reduce TP Multiplier

**Problem:** TP at 5.0x ATR may be too wide  
**Solution:** Test intermediate values

```
Test: 4.0, 4.5, 5.0, 5.5
Expected: Find sweet spot between 3.0 and 5.0
```

### Option 3: Disable Partial Profit for Now

**Problem:** Partial profit may be hurting more than helping  
**Solution:** Test without partial profit

```
InpEnablePartialProfit = false
InpATRMultiplierTP = 4.0 or 4.5
```

### Option 4: Increase Short Trade Threshold

**Problem:** Only 13 short trades (1.03%)  
**Solution:** Lower confidence threshold further

```
Current: InpMinConfidenceShort = 0.45
Test: 0.40, 0.42, 0.43
```

### Option 5: Disable Asian Session

**Problem:** Asian session added 246 trades but decreased quality  
**Solution:** Test without Asian session

```
InpEnableAsianSession = false
Keep TP = 5.0
```

---

## 🎯 Recommended Test Sequence

### Test 1: Disable Partial Profit + TP=4.5
```
InpEnablePartialProfit = false
InpATRMultiplierTP = 4.5
InpEnableAsianSession = true
```
**Expected:** Better average profit, fewer early exits

### Test 2: Adjust Partial Profit Levels
```
InpEnablePartialProfit = true
InpPartialProfit1Multiplier = 3.0  (was 2.0)
InpPartialProfit2Multiplier = 5.0  (was 4.0)
InpATRMultiplierTP = 5.0
```
**Expected:** Less aggressive profit taking, higher average

### Test 3: Lower Short Confidence
```
InpMinConfidenceShort = 0.40  (was 0.45)
InpRelaxHTFFilterForShorts = true
```
**Expected:** More short trades (target: 30-50%)

### Test 4: Disable Asian Session
```
InpEnableAsianSession = false
InpATRMultiplierTP = 4.5
InpEnablePartialProfit = false
```
**Expected:** Fewer but higher quality trades

---

## 📊 Key Insights

### What's Working ✅
1. **Average loss improved** (-4.08 vs -4.86) - SL management better
2. **Gross profit increased** (479.41 vs 423.37) - More winning trades
3. **Largest profit** (7.92) - Some trades are running well

### What's Not Working ❌
1. **Average profit decreased** - Partial profit too aggressive?
2. **Net profit decreased** - Too many marginal trades?
3. **Short trades still too low** - Need to lower threshold more
4. **Win rate decreased** - Quality vs quantity issue

### Critical Issue
**Partial profit taking at 2x ATR may be the problem:**
- Closes 50% too early
- Remaining 50% often hits SL before reaching TP2
- Net result: Lower average profit per trade

---

## 🚨 Immediate Action

**Test this configuration first:**

```
InpATRMultiplierTP = 4.5
InpEnablePartialProfit = false  ← Disable to test
InpEnableAsianSession = true
InpMinConfidenceShort = 0.40  ← Lower for more shorts
```

**Expected Results:**
- Average profit: 0.41 → 0.6-0.8 pips
- Net profit: Should improve
- Short trades: 13 → 50-100 (still low but better)

---

*Analysis Date: 2025-01-03*

