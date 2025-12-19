# Fixed Lot Size Recommendation for $1,000 Account

## 🎯 Quick Answer

**Recommended Fixed Lot Size: 0.01 (1 micro lot)**

**Why:**
- Safe for $1,000 account
- Allows multiple trades
- Matches 1% risk per trade
- Easy to scale up later

---

## 📊 Risk Calculation

### Account Details
- **Balance:** $1,000 USD
- **Risk Per Trade:** 1% (current setting)
- **Risk Amount:** $10 per trade

### XAUUSD Lot Size Basics
- **1 Standard Lot** = 100 oz of gold
- **1 Mini Lot** = 10 oz (0.1 lot)
- **1 Micro Lot** = 1 oz (0.01 lot)

### Stop Loss Distance
Based on your EA settings:
- **SL Multiplier:** 2.0x ATR
- **Typical ATR:** ~$15-25 for XAUUSD on M15
- **Typical SL Distance:** 30-50 pips (points)

---

## 💰 Lot Size vs Risk Analysis

### For 0.01 Lot (1 micro lot)
- **1 pip movement** = ~$0.01
- **30 pip SL** = ~$0.30 risk
- **50 pip SL** = ~$0.50 risk
- **Risk per trade:** $0.30-$0.50 (0.03-0.05% of account)
- **Very safe** ✅

### For 0.02 Lot (2 micro lots)
- **1 pip movement** = ~$0.02
- **30 pip SL** = ~$0.60 risk
- **50 pip SL** = ~$1.00 risk
- **Risk per trade:** $0.60-$1.00 (0.06-0.1% of account)
- **Still safe** ✅

### For 0.05 Lot (5 micro lots)
- **1 pip movement** = ~$0.05
- **30 pip SL** = ~$1.50 risk
- **50 pip SL** = ~$2.50 risk
- **Risk per trade:** $1.50-$2.50 (0.15-0.25% of account)
- **Acceptable** ✅

### For 0.10 Lot (1 mini lot)
- **1 pip movement** = ~$0.10
- **30 pip SL** = ~$3.00 risk
- **50 pip SL** = ~$5.00 risk
- **Risk per trade:** $3.00-$5.00 (0.3-0.5% of account)
- **Moderate risk** ⚠️

---

## 🎯 Recommended Settings

### Option 1: Conservative (Recommended)
```
InpUseFixedLot = true
InpFixedLotSize = 0.01
InpRiskPercent = 1.0  (ignored when fixed lot is used)
```
**Risk:** ~$0.30-$0.50 per trade (0.03-0.05%)
**Pros:** Very safe, allows many trades
**Cons:** Smaller profits per trade

### Option 2: Moderate
```
InpUseFixedLot = true
InpFixedLotSize = 0.02
InpRiskPercent = 1.0  (ignored when fixed lot is used)
```
**Risk:** ~$0.60-$1.00 per trade (0.06-0.1%)
**Pros:** Better profit potential, still safe
**Cons:** Slightly higher risk

### Option 3: Aggressive (Not Recommended)
```
InpUseFixedLot = true
InpFixedLotSize = 0.05
InpRiskPercent = 1.0  (ignored when fixed lot is used)
```
**Risk:** ~$1.50-$2.50 per trade (0.15-0.25%)
**Pros:** Higher profit potential
**Cons:** Higher risk, fewer trades before drawdown

---

## 📊 Comparison: Fixed vs Percentage-Based

### Percentage-Based (Current)
- **Risk:** 1% per trade = $10
- **Lot size:** Varies based on SL distance
- **Typical lot:** 0.01-0.02 (depending on SL)
- **Pros:** Adapts to volatility
- **Cons:** Lot size varies

### Fixed Lot (Recommended)
- **Lot size:** 0.01 (fixed)
- **Risk:** ~$0.30-$0.50 per trade
- **Pros:** Consistent position size, easier to manage
- **Cons:** Lower risk per trade (but safer)

---

## 💡 Recommendation for $1,000 Account

### Best Choice: 0.01 Fixed Lot

**Configuration:**
```
InpUseFixedLot = true
InpFixedLotSize = 0.01
```

**Why:**
1. ✅ **Very safe** - Only 0.03-0.05% risk per trade
2. ✅ **Allows many trades** - Can take 20-30 losing trades before 10% drawdown
3. ✅ **Easy to scale** - Can increase to 0.02 or 0.05 as account grows
4. ✅ **Consistent** - Same position size every trade
5. ✅ **Matches your EA's conservative approach** (93.78% win rate)

### Expected Performance
- **Average profit per trade:** ~$0.48 (0.48 pips × $0.01)
- **Average loss per trade:** ~$5.24 (5.24 pips × $0.01)
- **Net profit per year:** ~$16.60 (166 pips × $0.01)
- **With 1,319 trades:** ~$166 profit potential

---

## 📈 Scaling Plan

### As Account Grows
- **$1,000:** 0.01 lot (current)
- **$2,000:** 0.02 lot (double)
- **$5,000:** 0.05 lot (5x)
- **$10,000:** 0.10 lot (10x)

**Rule:** Keep risk per trade at 0.03-0.05% when using fixed lots

---

## ⚠️ Important Notes

### Fixed Lot vs Percentage-Based
- **Fixed lot:** Same size every trade (simpler)
- **Percentage-based:** Adapts to SL distance (more complex)
- **For $1,000:** Fixed 0.01 is recommended (simpler, safer)

### Risk Management
- **With 0.01 lot:** Very low risk per trade
- **Max drawdown:** 4.38% = ~$44 (manageable)
- **Loss streak protection:** Built into EA (max 5 losses)

### Profit Expectations
- **Per trade:** ~$0.48 average profit
- **Per day:** ~$0.45 (1 trade/day average)
- **Per month:** ~$13.50 (30 trades)
- **Per year:** ~$166 (1,319 trades)

**Note:** These are based on backtest. Real results may vary.

---

## 🎯 Final Recommendation

### For $1,000 Account:
```
InpUseFixedLot = true
InpFixedLotSize = 0.01
```

**This gives you:**
- ✅ Very safe risk management
- ✅ Consistent position sizing
- ✅ Room to grow account
- ✅ Matches EA's conservative approach

**Alternative (if you want slightly more risk):**
```
InpUseFixedLot = true
InpFixedLotSize = 0.02
```

---

## 📋 Quick Setup

1. **Enable Fixed Lot:**
   ```
   InpUseFixedLot = true
   InpFixedLotSize = 0.01
   ```

2. **Keep other settings:**
   ```
   InpATRMultiplierSL = 2.0
   InpATRMultiplierTP = 4.0
   InpMinConfidenceShort = 0.32
   ```

3. **Monitor:**
   - Track profit/loss per trade
   - Adjust lot size as account grows
   - Keep risk per trade low

---

*Recommendation Created: 2025-01-03*

