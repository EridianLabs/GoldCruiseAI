# 🚀 Quick Start Guide - GoldCruiseAI

Welcome to GoldCruiseAI! This guide will help you get started in just a few minutes.

---

## 📋 Prerequisites

Before you begin, make sure you have:

- ✅ MetaTrader 5 installed
- ✅ A demo or live trading account
- ✅ GoldCruiseAI.ex5 file (purchased from MQL5)
- ✅ At least $500 recommended account balance

---

## 🎯 Step 1: Purchase & Download

1. **Purchase GoldCruiseAI:**
   - Visit: [MQL5 Marketplace](https://www.mql5.com/en/market/product/158880)
   - Choose: Unlimited ($599) or 1 Month Rent ($99)
   - Complete purchase

2. **Download the EA:**
   - After purchase, the EA will be available in your MQL5 account
   - Download `GoldCruiseAI.ex5` file

---

## 📥 Step 2: Install the EA

### Method 1: Automatic Installation (Recommended)

1. Open MetaTrader 5
2. Go to **Tools → Options → Expert Advisors**
3. Enable **"Allow automated trading"**
4. Enable **"Allow DLL imports"** (if needed)
5. Go to **View → Navigator** (Ctrl+N)
6. Find **GoldCruiseAI** in Expert Advisors
7. Drag and drop onto XAUUSD M15 chart

### Method 2: Manual Installation

1. Open MetaTrader 5
2. Go to **File → Open Data Folder**
3. Navigate to `MQL5 → Experts`
4. Copy `GoldCruiseAI.ex5` to this folder
5. Restart MetaTrader 5
6. The EA will appear in Navigator under Expert Advisors

---

## ⚙️ Step 3: Configure the EA

### Basic Setup:

1. **Attach EA to Chart:**
   - Open XAUUSD chart
   - Set timeframe to **M15** (15 minutes)
   - Drag GoldCruiseAI from Navigator onto chart

2. **Load Risk Profile:**
   - Click **"Inputs"** tab in EA settings
   - Click **"Load"** button
   - Select a set file from [Set Files page](../setfiles/)
   - Recommended: **Moderate.set** for most traders

3. **Enable AutoTrading:**
   - Click **"AutoTrading"** button in toolbar (or press F7)
   - Ensure button is green/enabled
   - EA will start trading automatically

---

## 📊 Step 4: Choose Your Risk Profile

### For Beginners / Small Accounts ($500-$2,000):
- **Conservative.set** or **FixedLot_0.01.set**
- Very safe, low risk per trade

### For Most Traders ($1,000-$5,000):
- **Moderate.set** ⭐ **RECOMMENDED**
- Balanced risk/reward
- Proven configuration

### For Experienced Traders ($5,000+):
- **Moderate.set** or **Aggressive.set**
- Depends on your risk tolerance

[Download Set Files →](../setfiles/)

---

## ✅ Step 5: Verify Setup

Check these items to ensure everything is working:

- [ ] EA attached to XAUUSD M15 chart
- [ ] AutoTrading enabled (green button)
- [ ] Risk profile loaded
- [ ] No errors in Experts tab
- [ ] EA shows "smiley face" icon on chart

---

## 🎓 First Trade Checklist

Before your first live trade:

1. **Test on Demo First:**
   - Always test on demo account first
   - Run for at least 1 week
   - Verify performance matches expectations

2. **Check Settings:**
   - Verify risk percentage is appropriate
   - Confirm lot size settings
   - Review max drawdown limits

3. **Monitor Initial Trades:**
   - Watch first few trades closely
   - Check execution quality
   - Verify stop loss and take profit levels

---

## 📈 Monitoring Your EA

### Daily Checks:

- **Check Terminal Tab:**
  - View open positions
  - Monitor pending orders
  - Review trade history

- **Check Journal Tab:**
  - Look for any errors
  - Review EA messages
  - Check for warnings

- **Review Performance:**
  - Track win rate
  - Monitor drawdown
  - Check daily profit/loss

### Weekly Reviews:

- Analyze trade performance
- Review risk metrics
- Adjust settings if needed
- Check account balance

---

## ⚠️ Important Notes

### Before Going Live:

1. **Always test on demo first**
2. **Start with Conservative or Moderate profile**
3. **Use proper risk management**
4. **Never risk more than you can afford**
5. **Monitor regularly**

### Risk Warnings:

- ⚠️ Trading involves substantial risk
- ⚠️ Past performance doesn't guarantee future results
- ⚠️ Use proper position sizing
- ⚠️ Monitor your account regularly

---

## 🆘 Troubleshooting

### EA Not Trading?

1. **Check AutoTrading:**
   - Ensure AutoTrading button is green
   - Check Tools → Options → Expert Advisors

2. **Check Inputs:**
   - Verify `InpEnableTrading = true`
   - Check risk settings are valid

3. **Check Symbol:**
   - Ensure chart is XAUUSD
   - Verify timeframe is M15

4. **Check Account:**
   - Ensure sufficient margin
   - Verify account is enabled for trading

### EA Shows Errors?

1. **Check Journal tab** for error messages
2. **Verify EA is compiled** (should be .ex5 file)
3. **Check MT5 version** (should be latest)
4. **Restart MT5** if needed

---

## 📞 Need Help?

- 📖 [Full Documentation](../docs/)
- ❓ [Support & FAQ](support.html)
- 📁 [Set Files](../setfiles/)
- ⚙️ [Parameter Guide](parameters.html)

---

## 🎉 You're Ready!

Your GoldCruiseAI EA is now set up and ready to trade. Remember:

- ✅ Start with demo account
- ✅ Use recommended risk profile
- ✅ Monitor performance regularly
- ✅ Adjust settings as needed

**Happy Trading!** 🚀

---

*Quick Start Guide - Updated 2025-12-19*

