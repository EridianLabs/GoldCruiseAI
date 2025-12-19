# Code Audit Checklist - Find Validation Issues

## 🔍 How to Find Issues in Your .mq5 File

Use this checklist to systematically find and fix validation issues.

---

## 📋 Search Patterns (Use Find/Replace in MetaEditor)

### 1. File Operations - Search For:

**Pattern 1: FileOpen without error check**
```
FileOpen(
```
**What to look for:**
- `FileOpen()` without checking `INVALID_HANDLE`
- `FileOpen()` without checking `InpEnableFileLogging`

**Fix needed:**
```mql5
// BEFORE:
int handle = FileOpen("log.txt", FILE_WRITE|FILE_READ|FILE_TXT);
FileWrite(handle, message);

// AFTER:
if(!InpEnableFileLogging) return;
int handle = FileOpen("log.txt", FILE_WRITE|FILE_READ|FILE_TXT|FILE_COMMON);
if(handle == INVALID_HANDLE) return;
FileWrite(handle, message);
```

---

**Pattern 2: FileWrite without error check**
```
FileWrite(
```
**What to look for:**
- `FileWrite()` called without checking if handle is valid
- `FileWrite()` called without checking if file logging is enabled

---

**Pattern 3: FileRead without error check**
```
FileRead(
```
**What to look for:**
- `FileRead()` without error handling
- `FileRead()` that could break EA if file doesn't exist

---

### 2. Trade Operations - Search For:

**Pattern 1: OrderSend without return check**
```
OrderSend(
```
**What to look for:**
- `OrderSend()` called without checking return value
- `OrderSend()` where result is not checked

**Fix needed:**
```mql5
// BEFORE:
MqlTradeRequest request = {};
MqlTradeResult result = {};
// ... fill request ...
OrderSend(request, result);
// Continue without checking

// AFTER:
MqlTradeRequest request = {};
MqlTradeResult result = {};
// ... fill request ...

if(!OrderSend(request, result))
{
   if(InpEnableConsoleLogging)
      Print("OrderSend failed: ", GetLastError());
   return false;
}

if(result.retcode != TRADE_RETCODE_DONE)
{
   if(InpEnableConsoleLogging)
      Print("Trade result: ", result.retcode);
   return false;
}
```

---

**Pattern 2: OrderModify without return check**
```
OrderModify(
```
**What to look for:**
- `OrderModify()` without checking return value
- `OrderModify()` that doesn't handle failures

---

**Pattern 3: OrderClose without return check**
```
OrderClose(
```
**What to look for:**
- `OrderClose()` without checking return value
- `OrderClose()` that doesn't handle failures

---

### 3. Input Validation - Search For:

**Pattern 1: OnInit with INIT_FAILED**
```
INIT_FAILED
```
**What to look for:**
- `OnInit()` that returns `INIT_FAILED` for non-critical errors
- `OnInit()` that fails on invalid inputs instead of using defaults

**Fix needed:**
```mql5
// BEFORE:
int OnInit()
{
   if(InpRiskPercent <= 0) return INIT_FAILED;
   return INIT_SUCCEEDED;
}

// AFTER:
int OnInit()
{
   if(InpRiskPercent <= 0 || InpRiskPercent > 100)
   {
      if(InpEnableConsoleLogging)
         Print("Warning: InpRiskPercent invalid, using default 1.0");
      // Use default - don't fail
   }
   return INIT_SUCCEEDED;
}
```

---

**Pattern 2: Missing input validation**
```
OnInit()
```
**What to look for:**
- `OnInit()` that doesn't validate critical inputs
- Missing validation for risk parameters, lot sizes, etc.

---

### 4. Error Handling - Search For:

**Pattern 1: Functions without return checks**
```
void FunctionName(
```
**What to look for:**
- Functions that should return `bool` but return `void`
- Functions that don't check for errors
- Functions that don't return error codes

---

**Pattern 2: Missing error logging**
```
GetLastError()
```
**What to look for:**
- `GetLastError()` called but not logged
- Errors that should be logged but aren't

---

## ✅ Systematic Review Process

### Step 1: Open Your .mq5 File in MetaEditor

### Step 2: Search for Each Pattern Above

For each pattern:
1. **Find all occurrences** (Ctrl+F or Cmd+F)
2. **Review each occurrence**
3. **Check if it needs fixing**
4. **Apply fix if needed**

### Step 3: Document What You Find

Create a list:
```
Found Issues:
1. FileOpen() at line 123 - no error check
2. OrderSend() at line 456 - no return check
3. OnInit() at line 50 - fails on invalid input
...
```

### Step 4: Apply Fixes One by One

1. **Fix file operations first**
2. **Fix trade operations second**
3. **Fix input validation third**
4. **Test after each fix**

---

## 🎯 Quick Fix Template

### For File Operations:

```mql5
// Template - Copy and adapt:
void SafeFileLog(string message)
{
   // Step 1: Check if enabled
   if(!InpEnableFileLogging) return;
   
   // Step 2: Try to open
   int handle = FileOpen("YourLogFile.txt", 
                        FILE_WRITE|FILE_READ|FILE_TXT|FILE_COMMON);
   
   // Step 3: Check for errors
   if(handle == INVALID_HANDLE) return;
   
   // Step 4: Perform operation
   FileSeek(handle, 0, SEEK_END);
   FileWrite(handle, TimeToString(TimeCurrent()), message);
   
   // Step 5: Close
   FileClose(handle);
}
```

### For Trade Operations:

```mql5
// Template - Copy and adapt:
bool SafeOrderSend(MqlTradeRequest &request, MqlTradeResult &result)
{
   // Step 1: Validate inputs
   if(request.volume <= 0) return false;
   if(!InpEnableTrading) return false;
   
   // Step 2: Try to send
   if(!OrderSend(request, result))
   {
      // Step 3: Log error (if enabled)
      if(InpEnableConsoleLogging)
         Print("OrderSend failed: ", GetLastError());
      return false;
   }
   
   // Step 4: Check result
   if(result.retcode != TRADE_RETCODE_DONE)
   {
      // Step 5: Log result (if enabled)
      if(InpEnableConsoleLogging)
         Print("Trade result: ", result.retcode, " - ", result.comment);
      return false;
   }
   
   // Step 6: Success
   return true;
}
```

### For Input Validation:

```mql5
// Template - Copy and adapt:
int OnInit()
{
   // Validate risk parameters
   if(InpRiskPercent <= 0 || InpRiskPercent > 100)
   {
      if(InpEnableConsoleLogging)
         Print("Warning: InpRiskPercent invalid (", InpRiskPercent, 
               "), using default 1.0");
      // Use default - don't fail initialization
   }
   
   // Validate lot size
   if(InpFixedLotSize <= 0)
   {
      if(InpEnableConsoleLogging)
         Print("Warning: InpFixedLotSize invalid (", InpFixedLotSize, 
               "), using default 0.01");
      // Use default - don't fail initialization
   }
   
   // Only fail on truly critical errors
   // (e.g., can't initialize indicators)
   
   return INIT_SUCCEEDED;
}
```

---

## 📝 What to Check After Each Fix

### After Fixing File Operations:
- [ ] File logging still works when enabled
- [ ] EA doesn't crash when file logging disabled
- [ ] EA doesn't crash when file operations fail
- [ ] Trading logic unchanged

### After Fixing Trade Operations:
- [ ] Trades still execute normally
- [ ] Errors are logged (if logging enabled)
- [ ] EA continues after trade failures
- [ ] Trading logic unchanged

### After Fixing Input Validation:
- [ ] EA initializes with valid inputs
- [ ] EA initializes with invalid inputs (uses defaults)
- [ ] Warnings are logged (if logging enabled)
- [ ] Trading logic unchanged

---

## 🧪 Final Verification

### Run These Tests:

1. **Backtest with same settings:**
   - [ ] Results match previous backtest
   - [ ] Same number of trades
   - [ ] Same profit/loss
   - [ ] Same win rate

2. **Test with file logging enabled:**
   - [ ] Logs are created
   - [ ] No errors

3. **Test with file logging disabled:**
   - [ ] EA runs normally
   - [ ] No file errors
   - [ ] Trading continues

4. **Test with invalid inputs:**
   - [ ] EA initializes
   - [ ] Uses defaults
   - [ ] Warnings logged (if enabled)

5. **Test error scenarios:**
   - [ ] Trade failures handled gracefully
   - [ ] File failures handled gracefully
   - [ ] EA continues normally

---

## 🚀 Ready to Fix?

1. **Open your .mq5 file**
2. **Search for each pattern** listed above
3. **Apply fixes** using templates
4. **Test thoroughly**
5. **Verify backtest results unchanged**

**Remember:** Only add error handling - don't change trading logic!

---

*Code Audit Checklist - Created 2025-01-03*

