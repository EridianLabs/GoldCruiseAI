# MQL5 Upload and Update Guide - Complete Instructions

## 📤 How to Upload Product to MQL5

### Step 1: Prepare Your EA File

1. **Rename EA:**
   - Current: `GoldAITrader.mq5`
   - New: `GoldCruiseAI.mq5`
   - Update file name in MetaEditor

2. **Update Copyright:**
   ```mql5
   #property copyright "Copyright 2025, GoldCruiseAI"
   #property link      "https://www.mql5.com"
   #property version   "1.00"
   #property description "GoldCruiseAI - Premium Gold Trading EA"
   ```

3. **Compile EA:**
   - Open `GoldCruiseAI.mq5` in MetaEditor
   - Press F7 or click Compile
   - Verify no errors
   - Get `GoldCruiseAI.ex5` file

4. **Test Compilation:**
   - Check for errors
   - Verify .ex5 file created
   - File location: `MQL5/Experts/GoldCruiseAI/GoldCruiseAI.ex5`

---

### Step 2: Create Product Listing

1. **Go to MQL5 Marketplace:**
   - Visit: https://www.mql5.com/en/market
   - Login to your account
   - Click "My Products" → "Create Product"

2. **Fill Product Form:**

   **Basic Information:**
   - **Product Name:** GoldCruiseAI
   - **Product Type:** Expert Advisor
   - **Category:** Currency → Gold
   - **Account Type:** Any (already selected)

   **Expert Advisor Type:**
   - ✅ Check: **Trend** (ONLY THIS ONE)
   - ❌ Uncheck: All others

   **Pricing:**
   - Row 1: **$599** USD - "for unlimited use" ✅
   - Row 2: **$99** USD - "1 month rent" ✅
   - Rows 3-5: Leave at $0.00 or remove

3. **Upload EA File:**
   - Click "Add product file"
   - Select `GoldCruiseAI.ex5`
   - Wait for upload
   - Verify file appears

4. **Add Product Description:**
   - Copy from `MQL5_PRODUCT_DESCRIPTION.md`
   - Paste into description field
   - Format with emojis and sections

5. **Upload Screenshots:**
   - Minimum 3, recommended 5+
   - Images should show:
     - Equity curve (smooth, impressive)
     - Backtest summary (key metrics)
     - Risk metrics (profit factor, Sharpe)
     - Trade distribution (long/short)
     - EA settings panel

6. **Add Tags/Keywords:**
   - Gold, XAUUSD, Expert Advisor, AI, Trend Following
   - High Win Rate, Low Drawdown, Risk Management
   - Automated Trading, Gold Trading, M15, EMA

7. **Review and Submit:**
   - Review all information
   - Check requirements checklist
   - Click "Submit for Review"
   - Wait for MQL5 approval (1-3 days)

---

## 🔄 How to Update Product Versions

### When to Update:
- Bug fixes
- New features
- Performance improvements
- Parameter adjustments

### Update Process:

1. **Modify Code:**
   ```mql5
   #property version "1.01"  // Increment version
   ```
   - Make your changes
   - Update version number
   - Add comments for changes

2. **Compile:**
   - Compile in MetaEditor
   - Get new `GoldCruiseAI.ex5`
   - Test on demo account

3. **Upload Update:**
   - Go to MQL5 → My Products
   - Select "GoldCruiseAI"
   - Click "Update Product"
   - Upload new `GoldCruiseAI.ex5` file

4. **Add Changelog:**
   ```
   Version 1.01 (2025-01-10)
   - Fixed: Minor bug in confidence calculation
   - Improved: Trailing stop logic
   - Added: Additional risk profile
   ```

5. **Submit Update:**
   - Review changes
   - Submit for review
   - Usually approved within 24 hours

---

## 📦 Including Set Files and Documentation

### Option 1: As Resources (Embedded in EX5)

**Add to GoldCruiseAI.mq5:**
```mql5
#resource "\\Files\\Conservative.set"
#resource "\\Files\\Moderate.set"
#resource "\\Files\\Aggressive.set"
// ... etc
```

**Then in code, access via:**
```mql5
ResourceCreate("Conservative.set", "\\Files\\Conservative.set");
```

**Pros:**
- Everything in one file
- Users get all files automatically
- No separate downloads

**Cons:**
- EX5 file size increases
- More complex to implement

### Option 2: Separate Download (RECOMMENDED)

**Provide download link in:**
- Product description
- Support forum
- Email to buyers

**Pros:**
- Simple
- Easy to update
- No code changes needed

**Cons:**
- Users need to download separately
- Requires hosting/download link

### Option 3: MQL5 Resources (Best)

**Use MQL5's Resource system:**
1. Upload set files as Resources in product
2. MQL5 handles distribution
3. Users get files automatically

**How:**
- In product page → Resources tab
- Upload .set files
- MQL5 distributes with EA

---

## ✅ MQL5 Requirements - Final Check

### Code Requirements:
- ✅ **No DLL calls** - Verified
- ✅ **No account limitations** - Verified
- ✅ **No symbol restrictions** - Only warning (acceptable)
- ✅ **No time limitations** - Verified
- ✅ **Latin characters only** - All parameters in English
- ✅ **Single EX5 file** - Will compile to one file

### File Requirements:
- ✅ **EX5 file name** - GoldCruiseAI.ex5 (Latin)
- ✅ **Input parameters** - All in Latin characters
- ✅ **No additional files** - Only EX5 (set files as Resources)

### Product Requirements:
- ✅ **Product name** - GoldCruiseAI
- ✅ **Description** - Provided
- ✅ **Screenshots** - Need 5+ images
- ✅ **Price** - $599/$99 set
- ✅ **Type** - Trend (only)

---

## 🎯 Pre-Upload Action Items

### Code Changes Needed:
1. [ ] Rename `GoldAITrader.mq5` → `GoldCruiseAI.mq5`
2. [ ] Update copyright to "Copyright 2025, GoldCruiseAI"
3. [ ] Update description in #property
4. [ ] Compile to `GoldCruiseAI.ex5`
5. [ ] Verify no compilation errors

### Files to Prepare:
1. [ ] `GoldCruiseAI.ex5` (compiled)
2. [ ] 5+ screenshots (backtest results)
3. [ ] Set files (6 files - for Resources or download)
4. [ ] Documentation (PDF guides - optional)

### Marketplace Listing:
1. [ ] Product name: GoldCruiseAI
2. [ ] Type: Trend (only)
3. [ ] Price: $599/$99
4. [ ] Description: Copy from template
5. [ ] Screenshots: Upload 5+
6. [ ] EA file: Upload GoldCruiseAI.ex5

---

## 📋 Upload Checklist

### Before Upload:
- [ ] EA renamed to GoldCruiseAI
- [ ] Copyright updated to 2025
- [ ] Compiled successfully (no errors)
- [ ] Tested on demo (quick test)
- [ ] Screenshots prepared (5+)
- [ ] Product description written
- [ ] Set files organized
- [ ] Documentation ready (optional)

### During Upload:
- [ ] Product form filled correctly
- [ ] Type: Trend (only) selected
- [ ] Price: $599/$99 set
- [ ] Description pasted
- [ ] Screenshots uploaded
- [ ] EA file uploaded
- [ ] All information reviewed

### After Upload:
- [ ] Submitted for review
- [ ] Waiting for approval
- [ ] Ready to respond to questions
- [ ] Marketing materials prepared

---

## 🚨 Important Notes

### Symbol Check (Line 138):
```mql5
if(_Symbol != "XAUUSD" && _Symbol != "GOLD")
{
   g_logger.LogWarning("EA is optimized for XAUUSD. Current symbol: " + _Symbol);
}
```

**Status:** ✅ **ACCEPTABLE**
- Only logs warning
- Does NOT block trading
- Does NOT restrict symbol
- MQL5 allows this (informational)

**No changes needed.**

### Version Updates:
- **Version 1.00** - Initial release
- Increment for each update (1.01, 1.02, etc.)
- Major updates: 2.00, 3.00, etc.
- Always add changelog

### File Size:
- EX5 file should be reasonable size
- If too large, optimize includes
- Set files can be Resources (separate)

---

## 🎉 You're Ready!

**Everything is compliant and ready for upload!**

**Next Steps:**
1. Rename EA to GoldCruiseAI
2. Update copyright
3. Compile to .ex5
4. Upload to MQL5
5. Submit for review

**Good luck with your launch!** 🚀

---

*Upload Guide: 2025-01-03*

