"""
Pydantic models for request/response validation
"""

from pydantic import BaseModel, Field, field_validator
from typing import Optional, Literal
from datetime import datetime
import uuid


class TransferRequest(BaseModel):
    """Request model for creating a payment transfer"""
    
    amount: float = Field(
        ..., 
        gt=0, 
        le=100000, 
        description="Amount between 0.01 and 100,000"
    )
    currency: Literal["USD", "EUR", "GBP", "HKD", "SGD"] = Field(
        ..., 
        description="Currency code"
    )
    recipient: str = Field(
        ..., 
        min_length=5, 
        max_length=20, 
        description="Phone number with country code"
    )
    sender_name: Optional[str] = Field(None, max_length=100)
    reference_id: Optional[str] = Field(None, max_length=50)
    
    @field_validator("amount")
    @classmethod
    def validate_precision(cls, v: float) -> float:
        if round(v, 2) != v:
            raise ValueError(f"Amount {v} has more than 2 decimal places")
        return v
    
    @field_validator("recipient")
    @classmethod
    def validate_phone(cls, v: str) -> str:
        cleaned = v.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
        
        if cleaned.startswith("+"):
            if not cleaned[1:].isdigit():
                raise ValueError("Phone number must contain digits after +")
        elif not cleaned.isdigit():
            raise ValueError("Phone number must be digits or start with +")
        
        return cleaned


class TransferResponse(BaseModel):
    """Response model for transfer operations"""
    
    id: str = Field(default_factory=lambda: f"TRF_{uuid.uuid4().hex[:8].upper()}")
    amount: float
    currency: str
    status: Literal["PENDING", "PROCESSING", "COMPLETED", "FAILED"] = "PENDING"
    recipient: str
    created_at: str = Field(default_factory=lambda: datetime.utcnow().isoformat())
    completed_at: Optional[str] = None
    
    def complete(self):
        self.status = "COMPLETED"
        self.completed_at = datetime.utcnow().isoformat()
    
    def fail(self, reason: str = None):
        self.status = "FAILED"