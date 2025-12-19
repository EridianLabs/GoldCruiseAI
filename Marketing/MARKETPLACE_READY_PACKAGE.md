# Marketplace Ready Package - GoldCruiseAI

## ✅ MQL5 Requirements Checklist

### Code Requirements
- ✅ **No DLL calls** - Verified (no DllImport, LoadLibrary, etc.)
- ✅ **No account limitations** - Verified (no AccountNumber checks)
- ✅ **No symbol restrictions** - Only warning log (doesn't block trading)
- ✅ **No time limitations** - Verified (no expiration checks)
- ✅ **Latin characters only** - All parameter names are in English
- ✅ **Single EX5 file** - Will compile to one file

### File Requirements
- ✅ **EX5 file name** - Must be in Latin (GoldCruiseAI.ex5)
- ✅ **Input parameters** - All in Latin characters
- ✅ **No additional files** - Only EX5 allowed (set files go in Resources or separate download)

---

## 📦 Package Structure

### For MQL5 Marketplace:

```
GoldCruiseAI/
├── GoldCruiseAI.ex5          (Main EA file - UPLOAD THIS)
├── Documentation/            (Separate download or Resources)
│   ├── QuickStartGuide.pdf
│   ├── ParameterGuide.pdf
│   └── PerformanceSummary.pdf
└── SetFiles/                 (Separate download or Resources)
    ├── Conservative.set
    ├── Moderate.set
    ├── Aggressive.set
    ├── MaxProfit_2Percent.set
    ├── MaxProfit_3Percent.set
    └── FixedLot_0.01.set
```

**Note:** MQL5 only allows ONE EX5 file. Set files and documentation must be:
- Added as Resources (embedded in EX5)
- OR provided as separate download links
- OR included in product description with instructions

---

## 🔧 Pre-Upload Checklist

### Code Verification
- [ ] **Rename EA** from GoldAITrader to GoldCruiseAI
- [ ] **Update copyright** to "Copyright 2025, GoldCruiseAI"
- [ ] **Update version** to "1.00" (already set)
- [ ] **Update description** in #property
- [ ] **Verify no DLL calls** (✅ Done - none found)
- [ ] **Verify no limitations** (✅ Done - only symbol warning, doesn't block)
- [ ] **Compile EA** - Ensure no errors
- [ ] **Test compilation** - Verify .ex5 file created

### File Preparation
- [ ] **Compile to .ex5** (GoldCruiseAI.ex5)
- [ ] **Verify file name** is in Latin characters
- [ ] **Prepare set files** (6 files ready)
- [ ] **Create documentation** (PDF guides)
- [ ] **Prepare screenshots** (5+ images)

### Marketplace Listing
- [ ] **Product name:** GoldCruiseAI
- [ ] **Category:** Expert Advisors → Currency → Gold
- [ ] **Type:** Trend (only this one)
- [ ] **Price:** $599 unlimited, $99/month rent
- [ ] **Description:** Use provided template
- [ ] **Screenshots:** Upload 5+ images
- [ ] **EA file:** Upload GoldCruiseAI.ex5

---

## 🚨 Important: Symbol Check Fix

### Current Code (Line 138):
```mql5
if(_Symbol != "XAUUSD" && _Symbol != "GOLD")
{
   g_logger.LogWarning("EA is optimized for XAUUSD. Current symbol: " + _Symbol);
}
```

**Status:** ✅ **OK for Marketplace**
- Only logs a warning
- Does NOT block trading
- Does NOT restrict symbol
- MQL5 allows this (informational only)

**No changes needed** - This is acceptable.

---

## 📋 How to Upload Product to MQL5

### Step 1: Prepare EA File
1. Rename `GoldAITrader.mq5` to `GoldCruiseAI.mq5`
2. Update copyright and descriptions
3. Compile in MetaEditor
4. Get `GoldCruiseAI.ex5` file

### Step 2: Create Product Listing
1. Go to MQL5.com → Market → My Products
2. Click "Create Product"
3. Select "Expert Advisor"
4. Fill in product form:
   - Name: GoldCruiseAI
   - Type: Trend (only)
   - Price: $599 unlimited, $99/month
   - Description: Use provided template

### Step 3: Upload Files
1. **Main File:** Upload `GoldCruiseAI.ex5`
2. **Screenshots:** Upload 5+ images
3. **Set Files:** Add as Resources OR provide download link
4. **Documentation:** Add as Resources OR provide download link

### Step 4: Submit for Review
1. Review all information
2. Check requirements checklist
3. Submit for MQL5 review
4. Wait for approval (usually 1-3 days)

---

## 🔄 How to Update Product Versions

### Updating Your EA:

1. **Modify Code:**
   - Make changes to `GoldCruiseAI.mq5`
   - Update version number: `#property version "1.01"` (increment)

2. **Compile:**
   - Compile in MetaEditor
   - Get new `GoldCruiseAI.ex5`

3. **Upload Update:**
   - Go to MQL5 → Market → My Products
   - Select your product
   - Click "Update Product"
   - Upload new .ex5 file
   - Add changelog/description of changes
   - Submit update

### Version Numbering:
- **1.00** - Initial release
- **1.01** - Bug fixes
- **1.10** - Minor features
- **2.00** - Major update

### Update Notes Format:
```
Version 1.01 (2025-01-03)
- Fixed: [Issue description]
- Improved: [Enhancement description]
- Added: [New feature description]
```

---

## 📁 Organized Folder Structure

### Recommended Organization:

```
GoldAI/
├── Source/                          (Development files)
│   └── GoldCruiseAI.mq5            (Source code)
│
├── Marketplace/                     (Ready for upload)
│   ├── GoldCruiseAI.ex5            (Compiled EA)
│   ├── Screenshots/                 (5+ images)
│   ├── SetFiles/                    (6 .set files)
│   └── Documentation/               (PDF guides)
│
├── Backtests/                       (Test results)
│   ├── 1_Year_Backtest/
│   ├── 4_Year_Backtest/
│   └── 25_Year_Backtest/
│
├── Analysis/                        (Analysis documents)
│   ├── Performance_Analysis/
│   └── Optimization_Reports/
│
└── Marketing/                       (Sales materials)
    ├── Product_Description.md
    ├── Sales_Strategy.md
    └── Branding/
```

---

## ✅ Final Pre-Upload Checklist

### Code Ready:
- [x] No DLL calls
- [x] No account limitations
- [x] No symbol restrictions (only warning)
- [x] No time limitations
- [x] All parameters in Latin
- [ ] EA renamed to GoldCruiseAI
- [ ] Copyright updated
- [ ] Version set to 1.00
- [ ] Compiled successfully

### Files Ready:
- [ ] GoldCruiseAI.ex5 compiled
- [ ] 6 set files prepared
- [ ] Documentation created
- [ ] 5+ screenshots ready
- [ ] Product description written

### Marketplace Ready:
- [ ] MQL5 account created/verified
- [ ] Product form filled
- [ ] Price set ($599/$99)
- [ ] Description uploaded
- [ ] Screenshots uploaded
- [ ] EA file uploaded
- [ ] Ready to submit

---

## 🎯 Action Items

### Immediate (Before Upload):
1. **Rename EA** to GoldCruiseAI
2. **Update copyright** to 2025
3. **Compile EA** to .ex5
4. **Verify no errors**
5. **Test on demo** (quick test)

### Before Submission:
1. **Prepare screenshots** (5+ images)
2. **Write product description** (use template)
3. **Organize set files** (6 files)
4. **Create documentation** (PDF guides)
5. **Review all requirements**

---

*Marketplace Ready Package Guide: 2025-01-03*

