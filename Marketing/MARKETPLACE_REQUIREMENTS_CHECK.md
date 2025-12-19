# MQL5 Marketplace Requirements - Compliance Check

## ✅ Code Compliance

### 1. DLL Calls - PROHIBITED
**Status:** ✅ **COMPLIANT**
- No `DllImport` statements found
- No `LoadLibrary` calls found
- No `GetProcAddress` calls found
- No external DLL dependencies

### 2. Limitations - PROHIBITED
**Status:** ✅ **COMPLIANT**
- ❌ No account number restrictions
- ❌ No account name restrictions
- ❌ No account type restrictions
- ❌ No time limitations (expiration dates)
- ❌ No symbol restrictions (only warning log, doesn't block)
- ❌ No broker restrictions

**Note:** Line 138 has symbol check but only logs warning - **ACCEPTABLE** (doesn't block trading)

### 3. File Requirements
**Status:** ✅ **COMPLIANT**
- ✅ Single EX5 file (will compile to one file)
- ✅ All parameter names in Latin characters
- ✅ EA name will be in Latin (GoldCruiseAI)

### 4. Naming Requirements
**Status:** ⚠️ **NEEDS UPDATE**
- Current: `GoldAITrader.mq5`
- Required: `GoldCruiseAI.mq5` (rename before upload)
- All input parameters: Already in Latin ✅

---

## 📋 Required Actions Before Upload

### 1. Rename EA (REQUIRED)
- Current: `GoldAITrader.mq5`
- New: `GoldCruiseAI.mq5`
- Update all internal references

### 2. Update Copyright (RECOMMENDED)
- Current: "Copyright 2024, GoldAI Trader"
- New: "Copyright 2025, GoldCruiseAI"
- Update in #property copyright

### 3. Update Version (CHECK)
- Current: `#property version "1.00"`
- Status: ✅ Already set correctly

### 4. Update Description (RECOMMENDED)
- Current: "AI-Enhanced Gold Trading Expert Advisor"
- New: "GoldCruiseAI - Premium Gold Trading EA"
- Update in #property description

### 5. Compile EA (REQUIRED)
- Compile in MetaEditor
- Verify no errors
- Get `GoldCruiseAI.ex5` file

---

## 🚨 Critical: Symbol Check Review

### Current Code (Line 138-141):
```mql5
if(_Symbol != "XAUUSD" && _Symbol != "GOLD")
{
   g_logger.LogWarning("EA is optimized for XAUUSD. Current symbol: " + _Symbol);
}
```

**MQL5 Compliance:** ✅ **ACCEPTABLE**
- Only logs a warning
- Does NOT block trading
- Does NOT restrict symbol
- Does NOT prevent use on other symbols
- This is informational only

**No changes needed** - MQL5 allows informational warnings.

---

## 📦 File Upload Requirements

### Main File:
- **File:** `GoldCruiseAI.ex5` (compiled)
- **Type:** Expert Advisor
- **Format:** EX5 only
- **Name:** Must be in Latin characters ✅

### Additional Files:
- **Set Files:** Can be added as Resources OR separate download
- **Documentation:** Can be added as Resources OR separate download
- **Screenshots:** Upload as images (5+ recommended)

**Note:** MQL5 allows Resources to be embedded in EX5 file using `#resource` directive.

---

## 🔄 Version Update Process

### How to Update Product:

1. **Make Changes:**
   - Edit `GoldCruiseAI.mq5`
   - Update version: `#property version "1.01"`

2. **Compile:**
   - MetaEditor → Compile
   - Get new `GoldCruiseAI.ex5`

3. **Upload:**
   - MQL5 → My Products → Select Product
   - Click "Update Product"
   - Upload new .ex5 file
   - Add changelog
   - Submit

### Version Changelog Format:
```
Version 1.01 (2025-01-10)
- Fixed: Minor bug in confidence calculation
- Improved: Trailing stop logic
- Added: Additional risk profile

Version 1.00 (2025-01-03)
- Initial release
- 25-year backtest validation
- 6 risk profiles included
```

---

## ✅ Final Compliance Checklist

### Code:
- [x] No DLL calls
- [x] No account limitations
- [x] No symbol restrictions (only warning)
- [x] No time limitations
- [x] All parameters in Latin
- [ ] EA renamed to GoldCruiseAI
- [ ] Copyright updated
- [ ] Compiled successfully

### Files:
- [ ] GoldCruiseAI.ex5 ready
- [ ] Set files organized
- [ ] Documentation prepared
- [ ] Screenshots ready

### Marketplace:
- [ ] Product form completed
- [ ] Description uploaded
- [ ] Files uploaded
- [ ] Ready to submit

---

*Compliance Check: 2025-01-03*

