# Systematic Testing Plan - Parameter Optimization

## Current Best Configuration (Test 4B)
- `InpATRMultiplierTP = 3.5`
- `InpMinConfidenceShort = 0.32`
- `InpEnableAsianSession = false`
- **Net Profit: 165.08 pips** 🏆

---

## Testing Strategy

### Phase 1: Optimize Take-Profit (TP) Multiplier
**Goal:** Improve average profit (currently 0.48, target: 2.0+)

**Current:** TP = 3.5  
**Test Range:** 3.0 to 5.0  
**Step Size:** 0.5

#### Test Sequence:
```
Test 1: TP = 3.0  (baseline - already tested)
Test 2: TP = 3.5  (current best - already tested)
Test 3: TP = 4.0  ← Next test
Test 4: TP = 4.5
Test 5: TP = 5.0  (already tested - was bad with Asian session)
```

**Fixed Parameters:**
- `InpMinConfidenceShort = 0.32` (keep optimal)
- `InpEnableAsianSession = false` (keep disabled)
- `InpEnablePartialProfit = false` (keep disabled)

**Expected Results:**
- Average profit should increase: 0.48 → 0.6-0.9 pips
- Win rate may decrease slightly (acceptable if profit increases)
- Net profit should improve if average profit increases enough

---

### Phase 2: Fine-tune Short Confidence
**Goal:** Increase short trades to 30-50% (currently 23.4%)

**Current:** Short Conf = 0.32  
**Test Range:** 0.30 to 0.35  
**Step Size:** 0.01 (fine-grained)

#### Test Sequence:
```
Test 1: Short Conf = 0.30  (already tested - FAILED)
Test 2: Short Conf = 0.31  ← Test this
Test 3: Short Conf = 0.32  (current best - already tested)
Test 4: Short Conf = 0.33  ← Test this
Test 5: Short Conf = 0.34  ← Test this
Test 6: Short Conf = 0.35  (already tested - good but fewer shorts)
```

**Fixed Parameters:**
- `InpATRMultiplierTP = 3.5` (or best from Phase 1)
- `InpEnableAsianSession = false` (keep disabled)
- `InpEnablePartialProfit = false` (keep disabled)

**Expected Results:**
- Short trades: 308 → 350-450 (26-34% of total)
- Short win rate should stay >95%
- Net profit should improve if more quality shorts

---

### Phase 3: Combined Optimization
**Goal:** Find best combination of TP and Short Confidence

**Test Matrix:**

| TP | Short Conf | Priority | Notes |
|----|-----------|----------|-------|
| 3.5 | 0.31 | High | Current best + more shorts |
| 3.5 | 0.33 | High | Current best + more shorts |
| 4.0 | 0.32 | High | Better avg profit + current shorts |
| 4.0 | 0.31 | Medium | Better avg profit + more shorts |
| 4.0 | 0.33 | Medium | Better avg profit + more shorts |
| 4.5 | 0.32 | Medium | Aggressive TP + current shorts |
| 4.5 | 0.31 | Low | Aggressive TP + more shorts |

**Test Order:**
1. **TP=4.0, Short=0.32** (most likely to improve average profit)
2. **TP=3.5, Short=0.31** (most likely to increase shorts)
3. **TP=4.0, Short=0.31** (combined improvement)
4. **TP=3.5, Short=0.33** (more shorts, maintain TP)
5. **TP=4.0, Short=0.33** (both improvements)
6. **TP=4.5, Short=0.32** (aggressive TP)
7. **TP=4.5, Short=0.31** (aggressive both)

---

## Recommended Testing Sequence

### Step 1: Test TP = 4.0 (HIGHEST PRIORITY)
```
InpATRMultiplierTP = 4.0
InpMinConfidenceShort = 0.32
InpEnableAsianSession = false
InpEnablePartialProfit = false
```
**Why:** Most likely to improve average profit (0.48 → 0.6-0.7)
**Expected:** Net profit: 165 → 180-200 pips

---

### Step 2: Test Short Conf = 0.31
```
InpATRMultiplierTP = 3.5
InpMinConfidenceShort = 0.31
InpEnableAsianSession = false
InpEnablePartialProfit = false
```
**Why:** Fine-tune for more shorts (308 → 350-400)
**Expected:** Short %: 23.4% → 26-30%

---

### Step 3: Test Combined (TP=4.0, Short=0.31)
```
InpATRMultiplierTP = 4.0
InpMinConfidenceShort = 0.31
InpEnableAsianSession = false
InpEnablePartialProfit = false
```
**Why:** Both improvements together
**Expected:** Better average profit AND more shorts

---

### Step 4: Test TP = 4.5 (if Step 1 succeeds)
```
InpATRMultiplierTP = 4.5
InpMinConfidenceShort = 0.32
InpEnableAsianSession = false
InpEnablePartialProfit = false
```
**Why:** Further improve average profit
**Expected:** Average profit: 0.48 → 0.7-0.9 pips

---

### Step 5: Test Short Conf = 0.33 (if Step 2 succeeds)
```
InpATRMultiplierTP = 3.5 (or best from Phase 1)
InpMinConfidenceShort = 0.33
InpEnableAsianSession = false
InpEnablePartialProfit = false
```
**Why:** Even more shorts while maintaining quality
**Expected:** Short %: 23.4% → 28-32%

---

## Parameter Value Ranges

### Take-Profit Multiplier (InpATRMultiplierTP)
**Current Best:** 3.5  
**Test Range:** 3.0 to 5.0  
**Step Size:** 0.5  
**Values to Test:**
- ✅ 3.0 (baseline - tested)
- ✅ 3.5 (current best - tested)
- ⏳ **4.0** ← Next priority
- ⏳ **4.5** ← Test if 4.0 works
- ⏳ **5.0** ← Test if 4.5 works (was bad before, but without Asian session)

### Short Confidence (InpMinConfidenceShort)
**Current Best:** 0.32  
**Test Range:** 0.30 to 0.35  
**Step Size:** 0.01 (fine-grained)  
**Values to Test:**
- ❌ 0.30 (tested - FAILED)
- ⏳ **0.31** ← Next priority
- ✅ 0.32 (current best - tested)
- ⏳ **0.33** ← Test if 0.31 works
- ⏳ **0.34** ← Test if 0.33 works
- ✅ 0.35 (tested - good but fewer shorts)

---

## Testing Checklist

### Phase 1: TP Optimization
- [ ] Test TP = 4.0, Short = 0.32
- [ ] Test TP = 4.5, Short = 0.32
- [ ] Test TP = 5.0, Short = 0.32 (if 4.5 works)

### Phase 2: Short Confidence Optimization
- [ ] Test TP = 3.5, Short = 0.31
- [ ] Test TP = 3.5, Short = 0.33
- [ ] Test TP = 3.5, Short = 0.34

### Phase 3: Combined Optimization
- [ ] Test TP = 4.0, Short = 0.31
- [ ] Test TP = 4.0, Short = 0.33
- [ ] Test TP = 4.5, Short = 0.31
- [ ] Test TP = 4.5, Short = 0.33

---

## Success Criteria

### For Each Test, Check:
1. **Net Profit:** Should be >165 pips (current best)
2. **Average Profit:** Should be >0.48 pips (current best)
3. **Short Trades:** Should be >308 (23.4% of total)
4. **Win Rate:** Should be >93% (maintain quality)
5. **Profit Factor:** Should be >1.38 (current best)
6. **Max Drawdown:** Should be <5% (risk management)

### Target Goals:
- **Net Profit:** 200+ pips (from 165)
- **Average Profit:** 0.6-0.8 pips (from 0.48)
- **Short Trades:** 30-50% of total (from 23.4%)
- **Profit Factor:** 1.5+ (from 1.38)

---

## Quick Reference: Test Values

### Take-Profit Multiplier
```
3.0  ← Baseline (tested)
3.5  ← Current best (tested)
4.0  ← NEXT TEST (highest priority)
4.5  ← Test if 4.0 works
5.0  ← Test if 4.5 works
```

### Short Confidence
```
0.30  ← Too low (tested - FAILED)
0.31  ← NEXT TEST (fine-tune)
0.32  ← Current best (tested)
0.33  ← Test if 0.31 works
0.34  ← Test if 0.33 works
0.35  ← Good but fewer shorts (tested)
```

---

## Recommended First 3 Tests

### Test 1: TP = 4.0 (Improve Average Profit)
```
InpATRMultiplierTP = 4.0
InpMinConfidenceShort = 0.32
InpEnableAsianSession = false
InpEnablePartialProfit = false
```
**Expected:** Average profit 0.48 → 0.6-0.7 pips

### Test 2: Short = 0.31 (More Shorts)
```
InpATRMultiplierTP = 3.5
InpMinConfidenceShort = 0.31
InpEnableAsianSession = false
InpEnablePartialProfit = false
```
**Expected:** Short trades 308 → 350-400 (26-30%)

### Test 3: Combined (Both Improvements)
```
InpATRMultiplierTP = 4.0
InpMinConfidenceShort = 0.31
InpEnableAsianSession = false
InpEnablePartialProfit = false
```
**Expected:** Better average profit AND more shorts

---

*Testing Plan Created: 2025-01-03*

