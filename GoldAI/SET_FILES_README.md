# GoldAITrader - Risk Profile Set Files

## 📋 Available Set Files

### 1. **Conservative.set** - Low Risk
- **Risk:** 0.5% per trade
- **Lot Size:** Fixed 0.01
- **SL Multiplier:** 1.75 (tighter stops)
- **Max Drawdown:** 3.0%
- **Max Trades/Day:** 8
- **Confidence:** Higher thresholds (0.55/0.35)
- **Best For:** Beginners, small accounts ($500-$2,000), risk-averse traders

### 2. **Moderate.set** - Balanced (RECOMMENDED) ⭐
- **Risk:** 1.0% per trade
- **Lot Size:** Percentage-based (adapts to SL)
- **SL Multiplier:** 2.0
- **TP Multiplier:** 4.0
- **Max Drawdown:** 5.0%
- **Max Trades/Day:** 10
- **Confidence:** Optimized (0.5/0.32)
- **Best For:** Most traders, medium accounts ($1,000-$5,000)
- **Performance:** 166 pips profit, 93.78% win rate (backtested)

### 3. **Aggressive.set** - High Risk
- **Risk:** 2.0% per trade
- **Lot Size:** Percentage-based with higher multiplier
- **SL Multiplier:** 2.0
- **TP Multiplier:** 4.0
- **Max Drawdown:** 7.0%
- **Max Trades/Day:** 15
- **Confidence:** Lower thresholds (0.5/0.30) for more trades
- **Best For:** Experienced traders, larger accounts ($5,000+)
- **Warning:** Higher drawdowns, more volatility

### 4. **FixedLot_0.01.set** - Fixed Position Size
- **Risk:** Fixed 0.01 lot (very safe)
- **Lot Size:** Always 0.01 (consistent)
- **SL Multiplier:** 2.0
- **TP Multiplier:** 4.0
- **Best For:** Small accounts ($1,000), consistent sizing
- **Note:** Risk per trade varies with SL distance (~$0.30-$0.50)

---

## 🚀 How to Use Set Files

### Method 1: Load in Strategy Tester
1. Open MetaTrader 5
2. Go to **View → Strategy Tester** (Ctrl+R)
3. Select **GoldAITrader** EA
4. Click **Load** button (next to Inputs)
5. Select the desired `.set` file
6. Parameters will load automatically

### Method 2: Load on Chart
1. Attach EA to chart
2. Right-click on EA → **Properties**
3. Click **Load** button
4. Select the desired `.set` file
5. Click **OK**

### Method 3: Manual Copy
1. Open `.set` file in text editor
2. Copy parameter values
3. Paste into EA inputs manually

---

## 📊 Risk Profile Comparison

| Profile | Risk/Trade | Lot Size | Max DD | Trades/Day | Best For |
|---------|-----------|----------|--------|------------|----------|
| **Conservative** | 0.5% | Fixed 0.01 | 3.0% | 8 | Beginners |
| **Moderate** ⭐ | 1.0% | Adaptive | 5.0% | 10 | Most traders |
| **Aggressive** | 2.0% | Adaptive | 7.0% | 15 | Experienced |
| **Fixed 0.01** | ~0.03-0.05% | Fixed 0.01 | 5.0% | 10 | Small accounts |

---

## 💡 Recommendations

### For $1,000 Account:
- **Conservative.set** or **FixedLot_0.01.set**
- Very safe, low risk per trade

### For $2,000-$5,000 Account:
- **Moderate.set** (RECOMMENDED)
- Balanced risk/reward
- Proven configuration

### For $5,000+ Account:
- **Moderate.set** or **Aggressive.set**
- Depends on risk tolerance

---

## ⚠️ Important Notes

### Before Using:
1. **Test on demo account first**
2. **Understand the risk profile**
3. **Start with Conservative or Moderate**
4. **Monitor performance closely**
5. **Adjust as needed**

### Risk Warnings:
- **Past performance not indicative of future results**
- **Trading involves risk of loss**
- **Never risk more than you can afford to lose**
- **Use proper risk management**

### Account Size Guidelines:
- **$500-$1,000:** Conservative or Fixed 0.01
- **$1,000-$2,000:** Moderate (recommended)
- **$2,000-$5,000:** Moderate
- **$5,000+:** Moderate or Aggressive (based on risk tolerance)

---

## 📁 File Locations

### For Distribution:
Place `.set` files in the same folder as the EA or in a dedicated "Settings" folder.

### For Users:
Users should place `.set` files in:
- `MQL5/Presets/` (for easy access)
- Or any accessible folder

---

## 🔧 Customization

### To Create Your Own Set File:
1. Load EA with desired parameters
2. In Strategy Tester, click **Save** (next to Load)
3. Name your file (e.g., `MyCustom.set`)
4. File will be saved with all current parameters

### To Modify Existing Set File:
1. Open `.set` file in text editor
2. Modify parameter values
3. Save file
4. Load in MT5

---

## 📞 Support

If you have questions about which risk profile to use:
- Start with **Moderate.set** (recommended)
- Test on demo account
- Adjust based on your risk tolerance
- Monitor performance

---

*Set Files Created: 2025-01-03*

