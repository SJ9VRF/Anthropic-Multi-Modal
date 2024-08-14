# Pydantic models for structured output parsing.
from pydantic import BaseModel, Field
from typing import List

class TickerInfo(BaseModel):
    direction: str
    ticker: str
    company: str
    shares_traded: int
    percent_of_total_etf: float = Field(..., gt=0, lt=1)

class TickerList(BaseModel):
    fund: str
    tickers: List[TickerInfo]
