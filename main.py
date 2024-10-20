import random

import pyautogui as pg

import time

check = ( 'budget', 'savings', 'debt', 'credit', 'loan', 'mortgage', 'expenses', 'income', 'credit card', 'interest rate', 
  'balance', 'net worth', 'cash flow', 'emergency fund', 'financial plan', 'spending', 'personal finance',

  'investment', 'stocks', 'bonds', 'mutual funds', 'etfs', 'dividends', 'capital gains', 'equity', 'portfolio', 
  'asset allocation', 'risk tolerance', 'stock market', 'shares', 'return on investment (ROI)', 'bull market', 
  'bear market', 'hedge funds', 'commodities', 'cryptocurrency', 'bitcoin', 'forex', 'options trading', 'real estate',


  'retirement', '401k', 'IRA', 'Roth IRA', 'pension', 'annuity', 'retirement savings', 'social security', 
  'retirement plan', 'retirement account', 'retirement age', 'early retirement', 'required minimum distribution (RMD)',


  'taxes', 'tax return', 'tax refund', 'income tax', 'capital gains tax', 'estate tax', 'property tax', 'sales tax', 
  'tax deduction', 'tax credit', 'tax filing', 'withholding',


  'bank', 'savings account', 'checking account', 'certificate of deposit (CD)', 'money market account', 
  'auto loan', 'home loan', 'refinancing', 'insurance', 'life insurance', 'health insurance', 'disability insurance', 
  'insurance premium', 'deductible', 'claim', 'liability insurance', 'homeowners insurance', 'auto insurance', 'policy',


  'financial advisor', 'wealth management', 'estate planning', 'financial goals', 'financial strategy', 
  'debt consolidation', 'financial independence', 'passive income', 'asset management',


  'inflation', 'deflation', 'interest rates', 'unemployment rate', 'GDP', 'economic growth', 'recession', 
  'economic indicators', 'business loan', 'business finance', 'venture capital', 'angel investor', 'small business loan',


  'currency exchange', 'forex trading', 'foreign investment', 'trade balance', 'import/export', 'international markets',
)

time.sleep(2)

for i in range(15):
    # pg.typewrite(random.choice(check), interval=0.01)
    pg.typewrite("Aise spam krunga😂", interval=0.01)

    pg.press('enter')