NORTHSTAR INDUSTRIAL COMPONENTS LTD.
FINANCIAL DUE DILIGENCE DATA ROOM — COMPACT EDITION
====================================================

Company:        Northstar Industrial Components Ltd.
Industry:       Industrial manufacturing and distribution
Revenue:        USD 19–21M (2024–2025)
Employees:      ~120
Currency:       USD
Periods:        January 2024 – December 2025
Fiscal Year:    December 31
Accounting:     Accrual basis

INPUT FILES (upload to Colab for analysis)
------------------------------------------
1. general_ledger.csv           - All transactions Jan 2024 – Dec 2025
2. monthly_financials.csv       - Monthly P&L Jan 2024 – Dec 2025
3. accounts_receivable_aging.csv - AR aging by customer and invoice
4. management_adjustments.csv   - Management EBITDA adjustment proposals

NOTEBOOK
--------
notebook/northstar_due_diligence.ipynb
  - Execute from top to bottom in Google Colab
  - Upload the four input CSVs to Colab before running
  - Estimated demonstration time: 23–26 minutes

REFERENCE FILES (instructor only — do NOT share with participants)
------------------------------------------------------------------
INSTRUCTOR_SOLUTION_GUIDE.md   - Complete answer key with 5 findings
ANALYSIS_ROADMAP.md            - 4-phase timeline with time estimates

SCRIPTS
-------
scripts/generate_financial_data.py  - Reproducible data generation (seed=42)

NOTE: This dataset contains 5 deliberately engineered financial due diligence
findings. All findings are traceable and verifiable using pandas.
See INSTRUCTOR_SOLUTION_GUIDE.md for the complete answer key.
